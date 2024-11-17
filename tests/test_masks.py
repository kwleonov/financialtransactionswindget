from src.masks import get_mask_card_number


def test_get_mask_card_number(card_numbers: dict[str, list[str]]) -> None:
    """testing the correctness of masking a card number."""

    for i in range(len(card_numbers["card_number"])):
        card_number = card_numbers["card_number"][i]
        mask = card_numbers["mask"][i]

        out = get_mask_card_number(card_number)

        assert out != mask
