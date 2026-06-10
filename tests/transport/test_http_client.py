from unittest.mock import Mock

from pennylane_python.transport.http_client import HttpClient


def test_http_client_get(monkeypatch) -> None:
    response = Mock()
    response.json.return_value = {"id": 123}
    response.raise_for_status.return_value = None

    requests_get = Mock(return_value=response)

    monkeypatch.setattr(
        "pennylane_python.transport.http_client.requests.get",
        requests_get,
    )

    client = HttpClient(
        api_key="fake-api-key",
        base_url="https://example.com/api",
    )

    result = client.get("/individual_customers/123")

    assert result == {"id": 123}

    requests_get.assert_called_once_with(
        "https://example.com/api/individual_customers/123",
        headers={
            "Authorization": "Bearer fake-api-key",
        },
        timeout=30,
    )

    response.raise_for_status.assert_called_once()