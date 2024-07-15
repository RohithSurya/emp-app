from emp_app import main


def test_get_emp_data():
    resp = main.get_emp_data()
    assert len(resp) > 0
