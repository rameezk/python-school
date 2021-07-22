"""Super advanced employee system using composition"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Contract(ABC):
    """A Contract for an Employee at a company"""

    @abstractmethod
    def calculate_pay(self) -> float:
        """Calculates the pay for an employee"""


@dataclass
class Commission(ABC):
    """Representation of a Commission structure"""

    @abstractmethod
    def calculate_pay(self) -> float:
        """Calculates the commission an employee should be paid"""


@dataclass
class ContractCommission(Commission):
    """Representation of a Commission structure"""

    commission: float = 100
    contracts_landed: int = 0

    def calculate_pay(self) -> float:
        pay = self.contracts_landed * self.commission
        return pay


@dataclass
class Employee:
    """Representation of an Employee at a company"""

    name: str
    contract: Contract
    commission: Optional[Commission] = None

    def calculate_pay(self) -> float:
        """Calculate pay for employee"""
        pay = self.contract.calculate_pay()
        if self.commission is not None:
            pay += self.commission.calculate_pay()
        return pay


@dataclass
class Company:
    "Representation of a Company"

    name: str
    employees: List[Employee] = field(default_factory=list)

    def calculate_pay(self) -> float:
        total_pay = 0
        for employee in self.employees:
            total_pay += employee.calculate_pay()
        return total_pay


@dataclass
class HourlyContract(Contract):
    """Represents an hourly employee"""

    hourly_rate: float
    hours_worked: int

    def calculate_pay(self) -> float:
        pay = self.hourly_rate * self.hours_worked
        return pay


@dataclass
class SalaryContract(Contract):
    """Represents a salaried employee"""

    annual_salary: int

    def calculate_pay(self) -> float:
        pay = self.annual_salary / 12
        return pay


@dataclass
class FreelancerContract(Contract):
    """Represents a freelancer employee"""

    hourly_rate: float
    hours_worked: int
    vat_number: str = ""

    def calculate_pay(self) -> float:
        pay = self.hourly_rate * self.hours_worked
        return pay


def main() -> None:
    sally = Employee(
        name="Sally",
        contract=HourlyContract(hourly_rate=200, hours_worked=100),
        commission=ContractCommission(contracts_landed=10),
    )
    sally_pay = sally.calculate_pay()
    print(f"{sally.name} should be paid {sally_pay:.2f}")
    assert sally_pay == 21000, "Sally's pay is incorrect"

    bob = Employee(
        name="Bob",
        contract=SalaryContract(annual_salary=120000),
        commission=ContractCommission(contracts_landed=10),
    )
    bob_pay = bob.calculate_pay()
    print(f"{bob.name} should be paid {bob_pay:.2f}")
    assert bob_pay == 11000, "Bob's pay is incorrect"

    alice = Employee(
        name="Alice", contract=FreelancerContract(hourly_rate=100, hours_worked=160)
    )
    alice_pay = alice.calculate_pay()
    print(f"{alice.name} should be paid {alice_pay:.2f}")
    assert alice_pay == 16000, "Alice's pay is incorrect"

    acme_corp = Company(name="ACME Corp", employees=[sally, bob, alice])
    total_pay = acme_corp.calculate_pay()
    print(f"{acme_corp.name} owes it's employees {total_pay:.2f}")


if __name__ == "__main__":
    main()
