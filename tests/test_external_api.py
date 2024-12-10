# the test_external_api module

from unittest.mock import Mock, patch

from src.external_api import convert_amount


def test_convert_amount():
    """testing convert currency with external API."""

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "result": 999.0
    }

    with patch('requests.get', return_value=mock_response):
        result = convert_amount(100.0, "USD", "2024-12-08")
        assert result == 999.0
