import pytest
from unittest.mock import Mock, patch
from fourjawaly_sms import SMSGateway, SMSGatewayError

@pytest.fixture
def client():
    return SMSGateway('test_key', 'test_secret', 'TEST')

@pytest.fixture
def mock_response():
    mock = Mock()
    mock.ok = True
    return mock

def test_send_single_sms_success(client, mock_response):
    mock_response.json.return_value = {
        'success': True,
        'total_success': 1,
        'total_failed': 0,
        'job_ids': ['123']
    }
    
    with patch('requests.Session.post', return_value=mock_response):
        response = client.send_single_sms('966500000000', 'Test message')
        
        assert response.success
        assert response.total_success == 1
        assert response.total_failed == 0
        assert response.job_ids == ['123']

def test_send_sms_failure(client, mock_response):
    mock_response.ok = False
    mock_response.status_code = 400
    
    with patch('requests.Session.post', return_value=mock_response):
        with pytest.raises(SMSGatewayError) as exc_info:
            client.send_single_sms('966500000000', 'Test message')
        
        assert 'API request failed with status: 400' in str(exc_info.value)

def test_get_balance_success(client, mock_response):
    mock_response.json.return_value = {
        'balance': 100.0,
        'packages': [{
            'id': 1,
            'package_points': 1000,
            'current_points': 500,
            'expire_at': '2024-12-31',
            'is_active': True
        }]
    }
    
    with patch('requests.Session.get', return_value=mock_response):
        response = client.get_balance(is_active=1)
        
        assert response.balance == 100.0
        assert len(response.packages) == 1
        
        package = response.packages[0]
        assert package.package_points == 1000
        assert package.current_points == 500
        assert package.expire_at == '2024-12-31'
        assert package.is_active

def test_get_balance_failure(client, mock_response):
    mock_response.ok = False
    mock_response.status_code = 400
    
    with patch('requests.Session.get', return_value=mock_response):
        with pytest.raises(SMSGatewayError) as exc_info:
            client.get_balance()
        
        assert 'API request failed with status: 400' in str(exc_info.value)

def test_context_manager(client):
    with patch('requests.Session.close') as mock_close:
        with client:
            pass
        mock_close.assert_called_once()
