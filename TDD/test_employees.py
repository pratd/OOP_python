"""
Employee class Test.
"""

import unittest

from employees import Employee

Name: str = "PratD"
Employee_ID: int = 12345


class TestEmployeeComputePayout(unittest.TestCase):
    """Test the compute_payout method of the Employee class."""

    def setUp(self):
        """Setup the test fixtures."""
        self.prat = Employee(name=Name, employee_id=Employee_ID)

    def test_employee_payout_returns_a_float(self):
        """Whether payout returns a float or not"""
        self.assertIsInstance(self.prat.compute_payout(), float)

    def test_employee_payout_no_commission_no_hours(self):
        """Whether payout is correctly computed in case of no commission and no hours worked."""
        self.assertAlmostEqual(self.prat.compute_payout(), 1000.0)

    def test_employee_payout_no_commission(self):
        """whether payout is correctly computed in case of no commission and 10 hours worked"""
        self.prat.hours_worked = 10.0
        self.assertAlmostEqual(self.prat.compute_payout(), 2000.0)

    def test_employee_payout_with_commission(self):
        """Whether payout is correctly computed in case of 10 contracts landed and 10 hours of work done"""
        self.prat.hours_worked = 10.0
        self.prat.contracts_landed = 10
        self.assertAlmostEqual(self.prat.compute_payout(), 3000.0)

    def test_employee_payout_with_commission_disabled(self):
        """Whether payout is correctly computed in case of 10 contracts landed
        and 10 hours of work done but with commission disabled"""
        self.prat.hours_worked = 10.0
        self.prat.contracts_landed = 10
        self.prat.has_commission = False
        self.assertAlmostEqual(self.prat.compute_payout(), 2000.0)


if __name__ == "__main__":
    unittest.main()