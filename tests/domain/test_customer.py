import pytest

from pennylane_python.domain.customer import (
    Address,
    EmailAddress,
    IndividualCustomer,
)


def test_email_address_accepts_valid_email() -> None:
    email = EmailAddress("samuel@example.com")

    assert email.value == "samuel@example.com"


def test_email_address_rejects_invalid_email() -> None:
    with pytest.raises(ValueError, match="Invalid email address"):
        EmailAddress("invalid-email")


def test_individual_customer_full_name() -> None:
    customer = IndividualCustomer(
        first_name="Samuel",
        last_name="Martin",
        billing_address=Address(),
    )

    assert customer.full_name == "Samuel Martin"


def test_individual_customer_add_email() -> None:
    customer = IndividualCustomer(
        first_name="Samuel",
        last_name="Martin",
        billing_address=Address(),
    )

    email = EmailAddress("samuel@example.com")

    customer.add_email(email)

    assert customer.emails == [email]


def test_individual_customer_does_not_add_duplicate_email() -> None:
    customer = IndividualCustomer(
        first_name="Samuel",
        last_name="Martin",
        billing_address=Address(),
    )

    email = EmailAddress("samuel@example.com")

    customer.add_email(email)
    customer.add_email(email)

    assert customer.emails == [email]