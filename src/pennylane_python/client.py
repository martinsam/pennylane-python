from pennylane_python.mappers.customer_mapper import CustomerMapper
from pennylane_python.domain.customer import IndividualCustomer
from pennylane_python.transport.http_client import HttpClient


class PennylaneClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://app.pennylane.com/api/external/v2",
    ) -> None:
        self.http = HttpClient(api_key=api_key, base_url=base_url)

    def get_individual_customer(self, customer_id: str) -> IndividualCustomer:
        payload = self.http.get(f"/individual_customers/{customer_id}")
        return CustomerMapper.from_payload(payload)