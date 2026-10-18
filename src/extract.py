

import logging
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

API_URL = "https://fakestoreapi.com/products"


def extract_products():
    """Extract product data from the API."""
    logger.info("Starte Datenabruf von der API")

    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    products = response.json()

    if not isinstance(products, list):
        raise ValueError("Expected a list of products.")

    logger.info("Datenabruf abgeschlossen: %s Produkte", len(products))
    return products


if __name__ == "__main__":
    products = extract_products()
    print(f"Products extracted: {len(products)}")
