
import logging
import os

import psycopg
from dotenv import load_dotenv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

load_dotenv()


def load_products(products):
    """Load transformed products into PostgreSQL."""

    logger.info(
        "Starte Laden von %s Produkten in PostgreSQL",
        len(products),
    )

    connection_settings = {
        "host": os.getenv("ETL_DB_HOST"),
        "port": os.getenv("ETL_DB_PORT"),
        "dbname": os.getenv("ETL_DB_NAME"),
        "user": os.getenv("ETL_DB_USER"),
        "password": os.getenv("ETL_DB_PASSWORD"),
    }

    try:
        with psycopg.connect(**connection_settings) as connection:
            with connection.cursor() as cursor:
                for product in products:
                    cursor.execute(
                        """
                        INSERT INTO products (
                            id,
                            title,
                            price,
                            description,
                            category,
                            image,
                            rating_rate,
                            rating_count
                        )
                        VALUES (
                            %(id)s,
                            %(title)s,
                            %(price)s,
                            %(description)s,
                            %(category)s,
                            %(image)s,
                            %(rating_rate)s,
                            %(rating_count)s
                        )
                        ON CONFLICT (id) DO UPDATE SET
                            title = EXCLUDED.title,
                            price = EXCLUDED.price,
                            description = EXCLUDED.description,
                            category = EXCLUDED.category,
                            image = EXCLUDED.image,
                            rating_rate = EXCLUDED.rating_rate,
                            rating_count = EXCLUDED.rating_count;
                        """,
                        product,
                    )

        logger.info(
            "Laden erfolgreich abgeschlossen: %s Produkte gespeichert",
            len(products),
        )

    except Exception:
        logger.exception("Fehler beim Laden der Produkte in PostgreSQL")
        raise
