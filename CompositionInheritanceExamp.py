"""
Basic Employee management system
"""

from dataClasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


@dataclass
class Commission:
    """Represents a commission"""

    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        """Compute the commission to be paid our"""
        return self.commission * self.contracts_landed


class Contract(ABC):
    """Represents a contract and payment process for a particular employee"""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay and employee under this contract."""


@dataclass
class Employee:
    """Basic representation of an Employee"""

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout



@dataclass
class HourlyContract(Contract):
    """Contract type for an employee that's paid based on the number of worked hours"""

    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return (
            self.pay_rate * self.hours_worked +
            self.employer_cost
        )


@dataclass
class SalariedContract(Contract):
    """Contract type for an employee that;s paid based on fixed monthly salary"""

    monthly_salary: float = 0
    percentage: float = 1

    def get_payment(self) -> float:
        return (
                self.monthly_salary * self.percentage
        )


@dataclass
class FreelancerContract(Contract):
    """Contract type for an employee that;s paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return (
                self.pay_rate * self.hours_worked
        )

#
# @dataclass
# class SalariedEmployeeWithCommission(SalariedEmployee):
#     """Employee that;s paid based on fixed monthly salary and that gets a commission"""
#
#     commission: float = 100
#     contracts_landed: float = 0
#
#     def compute_pay(self) -> float:
#         """Compute how much the employee should be paid."""
#         return (
#                 super(SalariedEmployeeWithCommission, self).compute_pay()
#                 + self.commission * self.contracts_landed
#         )


# @dataclass
# class Freelancer(Employee):
#     """Freelancer that's paid based on number of worked hours."""
#
#     commission: float = 100
#     contracts_landed: float = 0
#     pay_rate: float = 0
#     hours_worked: int = 0
#     vat_number: str = ""
#
#     def compute_pay(self) -> float:
#         """Compute how much the employee should be paid."""
#         return (
#                 self.pay_rate * self.hours_worked
#         )

#
# @dataclass
# class FreelancerWithCommission(Freelancer):
#     """Freelancer that's paid based on number of worked hours and that gets a commission"""
#
#     commission: float = 100
#     contracts_landed: float = 0
#
#     def compute_pay(self) -> float:
#         """Compute how much the employee should be paid."""
#         return (
#                 super(FreelancerWithCommission, self).compute_pay()
#                 + self.commission * self.contracts_landed
#         )
#

def main() -> None:
    """Main function"""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=1234, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours and earned ${henry.compute_pay()}."
    )
    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = Commission(contracts_landed=10)
    sarah = Employee(name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission)
    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()