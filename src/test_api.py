
import requests

API_URL = "https://fakestoreapi.com/products"


def extract_products():
    """Extract product data from the API."""
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    products = response.json()

    if not isinstance(products, list):
        raise ValueError("Expected a list of products.")

    return products


def main():
    products = extract_products()

    print(f"Products extracted: {len(products)}")
    print("\nFull structure of the first product:")
    print(products[0])
    print()

    for product in products[:5]:
        print(f"ID: {product['id']}")
        print(f"Title: {product['title']}")
        print(f"Price: {product['price']}")
        print(f"Category: {product['category']}")
        print("-" * 40)


if __name__ == "__main__":
    main()
