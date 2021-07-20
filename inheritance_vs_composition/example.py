"""Super advanced employee system"""

from dataclasses import dataclass


@dataclass
class HourlyEmployee:
    """Represents an hourly employee"""

    name: str
    hourly_rate: float
    hours_worked: int
    commission: float = 100
    contracts_landed: int = 0

    def calculate_pay(self) -> float:
        pay = (
            self.hourly_rate * self.hours_worked
            + self.contracts_landed * self.commission
        )
        return pay


@dataclass
class SalariedEmployee:
    """Represents a salaried employee"""

    name: str
    annual_salary: int
    commission: float = 100
    contracts_landed: int = 0

    def calculate_pay(self) -> float:
        pay = self.annual_salary / 12 + self.commission * self.contracts_landed
        return pay


@dataclass
class Freelancer:
    """Represents a freelancer employee"""

    name: str
    hourly_rate: float
    hours_worked: int
    commission: float = 100
    contracts_landed: int = 0
    vat_number: str = ""

    def calculate_pay(self) -> float:
        pay = (
            self.hourly_rate * self.hours_worked
            + self.contracts_landed * self.commission
        )
        return pay


def main() -> None:
    sally = HourlyEmployee(
        name="Sally", hourly_rate=200, hours_worked=100, contracts_landed=10
    )
    sally_pay = sally.calculate_pay()
    print(f"{sally.name} should be paid {sally_pay:.2f}")
    assert sally_pay == 21000, "Sally's pay is incorrect"

    bob = SalariedEmployee(name="Bob", annual_salary=120000, contracts_landed=10)
    bob_pay = bob.calculate_pay()
    print(f"{bob.name} should be paid {bob_pay:.2f}")
    assert bob_pay == 11000, "Bob's pay is incorrect"

    alice = Freelancer(name="Alice", hourly_rate=100, hours_worked=160)
    alice_pay = alice.calculate_pay()
    print(f"{alice.name} should be paid {alice_pay:.2f}")
    assert alice_pay == 16000, "Alice's pay is incorrect"


if __name__ == "__main__":
    main()
