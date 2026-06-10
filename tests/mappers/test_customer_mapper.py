from pennylane_python.domain.customer import BillingLanguage, CustomerId
from pennylane_python.mappers.customer_mapper import CustomerMapper


def test_customer_mapper_from_payload() -> None:
    payload = {
        "id": 123,
        "first_name": "Samuel",
        "last_name": "Martin",
        "billing_address": {
            "address": "1 rue des tests",
            "postal_code": "37000",
            "city": "Tours",
            "country_alpha2": "FR",
        },
        "emails": ["samuel@example.com"],
        "billing_language": "fr_FR",
    }

    customer = CustomerMapper.from_payload(payload)

    assert customer.id == CustomerId("123")
    assert customer.first_name == "Samuel"
    assert customer.last_name == "Martin"
    assert customer.full_name == "Samuel Martin"
    assert customer.billing_address.city == "Tours"
    assert customer.billing_address.country_alpha2 == "FR"
    assert customer.emails[0].value == "samuel@example.com"
    assert customer.billing_language == BillingLanguage.FR


def test_customer_mapper_handles_missing_optional_fields() -> None:
    payload = {
        "id": 123,
        "first_name": "Samuel",
        "last_name": "Martin",
    }

    customer = CustomerMapper.from_payload(payload)

    assert customer.id == CustomerId("123")
    assert customer.billing_address.address is None
    assert customer.billing_address.city is None
    assert customer.emails == []
    assert customer.billing_language == BillingLanguage.FR