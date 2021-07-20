"""Super advanced employee system using inheritance"""

import abc
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Employee(ABC):
    name: str

    @abstractmethod
    def calculate_pay(self) -> float:
        """Calculate pay for employee"""


@dataclass
class HourlyEmployee(Employee):
    """Represents an hourly employee"""

    hourly_rate: float
    hours_worked: int

    def calculate_pay(self) -> float:
        pay = self.hourly_rate * self.hours_worked
        return pay


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """Represents an hourly employee with commission"""

    commission: float = 100
    contracts_landed: int = 0

    def calculate_pay(self) -> float:
        pay = super().calculate_pay() + self.contracts_landed * self.commission
        return pay


@dataclass
class SalariedEmployee(Employee):
    """Represents a salaried employee"""

    annual_salary: int

    def calculate_pay(self) -> float:
        pay = self.annual_salary / 12
        return pay


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Represents a salaried employee with commission"""

    commission: float = 100
    contracts_landed: int = 0

    def calculate_pay(self) -> float:
        pay = super().calculate_pay() + self.commission * self.contracts_landed
        return pay


@dataclass
class Freelancer(Employee):
    """Represents a freelancer employee"""

    hourly_rate: float
    hours_worked: int
    vat_number: str = ""

    def calculate_pay(self) -> float:
        pay = self.hourly_rate * self.hours_worked
        return pay


@dataclass
class FreelancerWithCommission(Freelancer):
    """Represents a freelancer employee with commission"""

    commission: float = 100
    contracts_landed: int = 0

    def calculate_pay(self) -> float:
        pay = super().calculate_pay() + self.contracts_landed * self.commission
        return pay


def main() -> None:
    sally = HourlyEmployeeWithCommission(
        name="Sally", hourly_rate=200, hours_worked=100, contracts_landed=10
    )
    sally_pay = sally.calculate_pay()
    print(f"{sally.name} should be paid {sally_pay:.2f}")
    assert sally_pay == 21000, "Sally's pay is incorrect"

    bob = SalariedEmployeeWithCommission(
        name="Bob", annual_salary=120000, contracts_landed=10
    )
    bob_pay = bob.calculate_pay()
    print(f"{bob.name} should be paid {bob_pay:.2f}")
    assert bob_pay == 11000, "Bob's pay is incorrect"

    alice = Freelancer(name="Alice", hourly_rate=100, hours_worked=160)
    alice_pay = alice.calculate_pay()
    print(f"{alice.name} should be paid {alice_pay:.2f}")
    assert alice_pay == 16000, "Alice's pay is incorrect"


if __name__ == "__main__":
    main()
