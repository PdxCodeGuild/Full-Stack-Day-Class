"""Behavioral tests for the Account class."""

import pytest

from account import Account


class TestAccountBehavior:
    """Tests the Account class for the correct interface behavior."""

    def test_initial_funds_zero(self):
        a = Account()
        assert a.get_funds() == 0.0

    def test_deposit_get_funds(self):
        a = Account()
        a.deposit(100.0)
        assert a.get_funds() == 100.0

    def test_check_withdrawal_enough(self):
        a = Account()
        a.deposit(100.0)
        assert a.check_withdrawal(50.0)

    def test_check_withdrawal_not_enough(self):
        a = Account()
        a.deposit(10.0)
        assert not a.check_withdrawal(50.0)

    def test_withdraw_enough(self):
        a = Account()
        a.deposit(100.0)
        a.withdraw(50.0)
        assert a.get_funds() == 50.0

    def test_withdraw_not_enough(self):
        a = Account()
        a.deposit(10.0)
        with pytest.raises(ValueError):
            a.withdraw(50.0)

    def test_calc_interest(self):
        a = Account()
        a.deposit(100.0)
        assert a.calc_interest() == 0.1
