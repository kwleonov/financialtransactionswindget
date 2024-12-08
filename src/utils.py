# the utils module.
import json
from json import JSONDecodeError


def load_operations_json(filename: str) -> list[dict[str, any]]:
    """Loading list of financial transactions. filename - path to json file.
    Returns list of dict with financial transaction data."""

    transaction_data = []

    with open(filename, "r") as f:
        try:
            transaction_data = json.load(f)
        except JSONDecodeError:
            pass
        except TypeError:
            pass
        except ValueError:
            pass

    return transaction_data
