
import logging

from extract import extract_products
from transform import transform_products
from load import load_products
from validate import validate_products


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# 1. Extract
logging.info("Fetching products from API")
raw_products = extract_products()
logging.info(f"Extracted: {len(raw_products)} products")


# 2. Transform
logging.info("Transforming products")
transformed_products = transform_products(raw_products)
logging.info(f"Transformed: {len(transformed_products)} products")


# 3. Validate
logging.info("Validating products")
validate_products(transformed_products)
logging.info("Data quality checks passed!")


# 4. Load
logging.info("Loading products into PostgreSQL")

try:
    load_products(transformed_products)
    logging.info(
        f"Loaded: {len(transformed_products)} products into PostgreSQL"
    )
except Exception:
    logging.exception("Failed to load products into PostgreSQL")
    raise
