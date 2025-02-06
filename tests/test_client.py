import pytest
from unittest.mock import patch
from _4jawaly_sms import SMSGateway, SMSGatewayException

@pytest.fixture
def client():
    return SMSGateway('test_key', 'test_secret', 'TEST')

def test_send_single_number(client):
    with patch('requests.Session.post') as mock_post:
        mock_post.return_value.json.return_value = {'success': True}
        mock_post.return_value.raise_for_status.return_value = None
        
        response = client.send('966500000000', 'Test message')
        assert response['success'] is True
        
        mock_post.assert_called_once()
        args = mock_post.call_args
        assert args[1]['json']['numbers'] == ['966500000000']

def test_send_multiple_numbers(client):
    with patch('requests.Session.post') as mock_post:
        mock_post.return_value.json.return_value = {'success': True}
        mock_post.return_value.raise_for_status.return_value = None
        
        numbers = ['966500000000', '966500000001']
        response = client.send(numbers, 'Test message')
        assert response['success'] is True
        
        mock_post.assert_called_once()
        args = mock_post.call_args
        assert args[1]['json']['numbers'] == numbers

def test_get_balance(client):
    with patch('requests.Session.get') as mock_get:
        mock_get.return_value.json.return_value = {'balance': 100}
        mock_get.return_value.raise_for_status.return_value = None
        
        response = client.get_balance()
        assert response['balance'] == 100
        
        mock_get.assert_called_once()
