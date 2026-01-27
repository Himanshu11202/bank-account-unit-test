import pytest
from bank import BankAccount

def test_initial_balance_is_zero():
    acc = BankAccount()
    assert acc.balance == 0

def test_deposit_increases_balance():
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.balance == 150

def test_withdraw_more_than_balance_raises_error():
    acc = BankAccount(100)
    with pytest.raises(ValueError):
        acc.withdraw(200)
