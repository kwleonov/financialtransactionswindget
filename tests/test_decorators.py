# tests for the decorators module.

from typing import Any

from pytest import CaptureFixture

from src.decorators import log


def test_log(capsys: CaptureFixture[Any]) -> None:
    """the test of logging the execution of the wrapped function, the call of which ended without errors."""

    @log()
    def myfunc(s: str) -> str:
        return s

    myfunc("Hello")
    captured = capsys.readouterr()
    result = "myfunc ok"
    answer = captured.out.rstrip()

    assert answer == result


def test_log_error(capsys: CaptureFixture[Any]) -> None:
    """the test for the log decorator when an error is called as a result of executing the wrapped function."""

    @log()
    def myfunc(a: int, b: int) -> int:
        return a + b

    myfunc(1, b="2")  # type: ignore
    captured = capsys.readouterr()
    result = "myfunc error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1,) {'b': '2'}."
    answer = captured.out.rstrip()

    assert result == answer
