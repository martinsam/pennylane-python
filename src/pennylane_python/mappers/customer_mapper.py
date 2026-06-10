from pennylane_python.domain.customer import (
    Address,
    BillingLanguage,
    CustomerId,
    EmailAddress,
    IndividualCustomer,
)


class CustomerMapper:
    @staticmethod
    def from_payload(payload: dict) -> IndividualCustomer:
        return IndividualCustomer(
            id=CustomerId(str(payload["id"])),
            first_name=payload.get("first_name", ""),
            last_name=payload.get("last_name", ""),
            billing_address=Address(
                address=(payload.get("billing_address") or {}).get("address"),
                postal_code=(payload.get("billing_address") or {}).get("postal_code"),
                city=(payload.get("billing_address") or {}).get("city"),
                country_alpha2=(payload.get("billing_address") or {}).get("country_alpha2"),
            ),
            emails=[
                EmailAddress(email)
                for email in payload.get("emails", [])
                if email
            ],
            billing_language=BillingLanguage(
                payload.get("billing_language", "fr_FR")
            ),
        )