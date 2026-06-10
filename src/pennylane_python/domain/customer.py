# domain/customer.py

from dataclasses import dataclass, field
from enum import Enum
from typing import NewType


CustomerId = NewType("CustomerId", str)
ExternalReference = NewType("ExternalReference", str)


class BillingLanguage(str, Enum):
    FR = "fr_FR"
    EN = "en_GB"
    DE = "de_DE"


class PaymentCondition(str, Enum):
    UPON_RECEIPT = "upon_receipt"
    DAYS_7 = "7_days"
    DAYS_15 = "15_days"
    DAYS_30 = "30_days"
    DAYS_30_END_OF_MONTH = "30_days_end_of_month"
    DAYS_45 = "45_days"
    DAYS_45_END_OF_MONTH = "45_days_end_of_month"
    DAYS_60 = "60_days"


@dataclass(frozen=True)
class EmailAddress:
    value: str

    def __post_init__(self) -> None:
        if "@" not in self.value:
            raise ValueError("Invalid email address")


@dataclass(frozen=True)
class Address:
    address: str | None = None
    postal_code: str | None = None
    city: str | None = None
    country_alpha2: str | None = None


@dataclass(frozen=True)
class LedgerAccount:
    id: str
    number: str | None = None
    label: str | None = None


@dataclass
class IndividualCustomer:
    first_name: str
    last_name: str
    billing_address: Address

    id: CustomerId | None = None
    phone: str | None = None
    delivery_address: Address | None = None
    payment_condition: PaymentCondition = PaymentCondition.DAYS_30
    billing_iban: str | None = None
    recipient: str | None = None
    reference: str | None = None
    ledger_account: LedgerAccount | None = None
    notes: str | None = None
    emails: list[EmailAddress] = field(default_factory=list)
    external_reference: ExternalReference | None = None
    billing_language: BillingLanguage = BillingLanguage.FR

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def add_email(self, email: EmailAddress) -> None:
        if email not in self.emails:
            self.emails.append(email)