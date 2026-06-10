from unittest.mock import Mock

from pennylane_python.client import PennylaneClient


def test_client_get_individual_customer(monkeypatch) -> None:
    http_client_mock = Mock()
    http_client_mock.get.return_value = {
        "id": 123,
        "first_name": "Samuel",
        "last_name": "Martin",
        "billing_address": {
            "city": "Tours",
        },
        "emails": ["samuel@example.com"],
        "billing_language": "fr_FR",
    }

    monkeypatch.setattr(
        "pennylane_python.client.HttpClient",
        Mock(return_value=http_client_mock),
    )

    client = PennylaneClient(api_key="fake-api-key")

    customer = client.get_individual_customer("123")

    assert customer.full_name == "Samuel Martin"
    assert customer.billing_address.city == "Tours"

    http_client_mock.get.assert_called_once_with(
        "/individual_customers/123"
    )