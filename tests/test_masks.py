import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"

    with pytest.raises(ValueError):
        get_mask_card_number("1234 5678 9012 34")

    with pytest.raises(ValueError):
        get_mask_card_number("1234 5678 9012 34567")

    with pytest.raises(ValueError):
        get_mask_card_number("")

    with pytest.raises(ValueError):
        get_mask_card_number("abcd efgh ijkl mnop")


def test_get_mask_account() -> None:
    assert get_mask_account("1234567890") == "**7890"
    assert get_mask_account("987654321") == "**4321"

    with pytest.raises(ValueError):
        get_mask_account("123")

    with pytest.raises(ValueError):
        get_mask_account("abcd")

    with pytest.raises(ValueError):
        get_mask_account("")
