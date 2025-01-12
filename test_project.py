from project import add_expense, view_expenses, calculate_total

def test_add_expense():
    expenses = []
    add_expense(expenses)
    assert len(expenses) == 1
    assert "item" in expenses[0] and "cost" in expenses[0]

def test_view_expenses(capsys):
    expenses = [{"item": "Coffee", "cost": 3.5}]
    view_expenses(expenses)
    captured = capsys.readouterr()
    assert "1. Coffee - $3.50" in captured.out

def test_calculate_total():
    expenses = [{"item": "Coffee", "cost": 3.5}, {"item": "Book", "cost": 15.0}]
    assert calculate_total(expenses) == 18.5
