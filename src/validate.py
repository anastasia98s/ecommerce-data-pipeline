
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def validate_products(products):
    """Validate product data before loading it into PostgreSQL."""

    logger.info("Starte Datenvalidierung")

    if not products:
        logger.error("Keine Produkte zur Validierung vorhanden")
        raise ValueError("No products to validate.")

    seen_ids = set()

    for product in products:
        # Check required fields
        required_fields = [
            "id",
            "title",
            "price",
            "description",
            "category",
        ]

        for field in required_fields:
            if product.get(field) is None or product.get(field) == "":
                logger.error("Pflichtfeld fehlt: %s", field)
                raise ValueError(
                    f"Product has a missing field: {field}"
                )

        # Check for duplicate IDs
        product_id = product["id"]

        if product_id in seen_ids:
            logger.error("Doppelte Produkt-ID gefunden: %s", product_id)
            raise ValueError(
                f"Duplicate product ID: {product_id}"
            )

        seen_ids.add(product_id)

        # Check price
        if product["price"] < 0:
            logger.error(
                "Produkt %s hat einen negativen Preis",
                product_id,
            )
            raise ValueError(
                f"Product {product_id} has a negative price."
            )

        # Check rating
        rating = product.get("rating_rate")

        if rating is not None and not 0 <= rating <= 5:
            logger.error(
                "Produkt %s hat eine ungültige Bewertung",
                product_id,
            )
            raise ValueError(
                f"Product {product_id} has an invalid rating."
            )

    logger.info(
        "Datenvalidierung erfolgreich: %s Produkte geprüft",
        len(products),
    )

    return True
