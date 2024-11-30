# tests for the decorators module.

from src.decorators import log


def test_log(capsys):
    """test log myfunc returned string."""

    @log()
    def myfunc(s):
        return s

    myfunc("Hello")
    captured = capsys.readouterr()
    result = "myfunc ok"
    answer = captured.out.rstrip()
    assert answer == result


def test_log_error(capsys):
    """test log myfunc with exception error."""

    @log()
    def myfunc(a, b):
        return a + b

    myfunc(1, b="2")
    captured = capsys.readouterr()
    result = "myfunc error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1,) {'b': '2'}."
    answer = captured.out.rstrip()

    assert result == answer
