# tests for the decorators module.

from src.decorators import log


def test_log(capsys):
    """test"""

    @log()
    def myfunc(s):
        return s

    myfunc("Hello")
    captured = capsys.readouterr()
    result = "myfunc ok"
    answer = captured.out.rstrip()
    assert answer == result
