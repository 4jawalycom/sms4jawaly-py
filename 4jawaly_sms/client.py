import requests
import base64
from typing import List, Dict, Union
from concurrent.futures import ThreadPoolExecutor

class SMS4JawalyClient:
    """4jawaly SMS Gateway client"""
    
    def __init__(self, api_key: str, api_secret: str, sender: str):
        """Initialize the client with API credentials and default sender"""
        self.api_key = api_key
        self.api_secret = api_secret
        self.sender = sender
        self.base_url = "https://api-sms.4jawaly.com/api/v1"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {self._get_auth_token()}"
        }
    
    def _get_auth_token(self) -> str:
        """Generate authentication token"""
        return base64.b64encode(
            f"{self.api_key}:{self.api_secret}".encode()
        ).decode()
    
    def _chunk_numbers(self, numbers: List[str], chunk_size: int) -> List[List[str]]:
        """Split numbers into chunks for parallel processing"""
        return [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    def _send_chunk(self, message: str, numbers: List[str], sender: str) -> Dict:
        """Send a chunk of numbers"""
        try:
            payload = {
                "messages": [{
                    "text": message,
                    "numbers": numbers,
                    "sender": sender
                }]
            }
            
            response = requests.post(
                f"{self.base_url}/account/area/sms/send",
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "chunk": numbers,
                    "response": response.json()
                }
            else:
                return {
                    "success": False,
                    "chunk": numbers,
                    "error": response.json().get("message", f"HTTP Error: {response.status_code}")
                }
        except Exception as e:
            return {
                "success": False,
                "chunk": numbers,
                "error": str(e)
            }
    
    def send_sms(self, message: str, numbers: Union[List[str], str]) -> Dict:
        """
        Send SMS messages with parallel sending support
        
        Args:
            message (str): Message text
            numbers (Union[List[str], str]): Number or list of numbers
            
        Returns:
            Dict: Sending result containing success status, job IDs, and any errors
        """
        if isinstance(numbers, str):
            numbers = [numbers]
        
        # Determine chunk size based on total numbers
        if len(numbers) <= 5:
            chunk_size = len(numbers)
        elif len(numbers) <= 100:
            chunk_size = len(numbers) // 5 + (1 if len(numbers) % 5 else 0)
        else:
            chunk_size = 100
        
        # Split numbers into chunks
        chunks = self._chunk_numbers(numbers, chunk_size)
        
        # Send chunks in parallel
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(
                lambda chunk: self._send_chunk(message, chunk, self.sender),
                chunks
            ))
        
        # Aggregate results
        aggregated = {
            "success": True,
            "total_success": 0,
            "total_failed": 0,
            "job_ids": [],
            "errors": {}
        }
        
        for result in results:
            if result["success"] and "err_text" not in result["response"].get("messages", [{}])[0]:
                aggregated["total_success"] += len(result["chunk"])
                if "job_id" in result["response"]:
                    aggregated["job_ids"].append(result["response"]["job_id"])
            else:
                aggregated["total_failed"] += len(result["chunk"])
                error_msg = (
                    result["response"].get("messages", [{}])[0].get("err_text")
                    or result.get("error", "Unknown error")
                )
                if error_msg not in aggregated["errors"]:
                    aggregated["errors"][error_msg] = []
                aggregated["errors"][error_msg].extend(result["chunk"])
        
        aggregated["success"] = aggregated["total_failed"] == 0
        return aggregated

    def get_balance(self) -> Dict:
        """Get account balance and package information"""
        try:
            response = requests.get(
                f"{self.base_url}/account/area/me/packages",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f'Failed to get balance: {str(e)}') from e

    def get_senders(self) -> Dict:
        """Get list of approved sender names"""
        try:
            response = requests.get(
                f"{self.base_url}/account/area/senders",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise Exception(f'Failed to get senders: {str(e)}') from e
