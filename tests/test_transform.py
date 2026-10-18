
from unittest.mock import patch

from src.transform import transform_products


def test_transform_products():
    products = [
        {
            "id": 1,
            "title": "Test Backpack",
            "price": 29.99,
            "description": "A backpack for everyday use.",
            "category": "men's clothing",
            "image": "https://example.com/image.jpg",
            "rating": {
                "rate": 4.5,
                "count": 10,
            },
        }
    ]

    with patch(
        "src.transform.translate_description",
        return_value="Ein Rucksack für den Alltag.",
    ):
        transformed = transform_products(products)

    assert len(transformed) == 1
    assert transformed[0]["id"] == 1
    assert transformed[0]["price"] == 29.99
    assert transformed[0]["description"] == "Ein Rucksack für den Alltag."
    assert transformed[0]["category"] == "Herrenbekleidung"
    assert transformed[0]["rating_rate"] == 4.5
    assert transformed[0]["rating_count"] == 10
