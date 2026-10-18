
import pytest

from src.validate import validate_products


def test_valid_products_pass():
    products = [
        {
            "id": 1,
            "title": "Test Backpack",
            "price": 29.99,
            "description": "Ein Rucksack",
            "category": "Herrenbekleidung",
            "rating_rate": 4.5,
        }
    ]

    assert validate_products(products) is True


def test_empty_products_fail():
    with pytest.raises(ValueError, match="No products"):
        validate_products([])


def test_negative_price_fails():
    products = [
        {
            "id": 1,
            "title": "Test Backpack",
            "price": -10,
            "description": "Ein Rucksack",
            "category": "Herrenbekleidung",
            "rating_rate": 4.5,
        }
    ]

    with pytest.raises(ValueError, match="negative price"):
        validate_products(products)


def test_duplicate_ids_fail():
    product = {
        "id": 1,
        "title": "Test Backpack",
        "price": 29.99,
        "description": "Ein Rucksack",
        "category": "Herrenbekleidung",
        "rating_rate": 4.5,
    }

    with pytest.raises(ValueError, match="Duplicate product ID"):
        validate_products([product, product])
