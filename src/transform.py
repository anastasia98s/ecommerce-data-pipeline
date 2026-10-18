

import json
import logging
from pathlib import Path

from deep_translator import MyMemoryTranslator


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


CATEGORY_TRANSLATIONS = {
    "men's clothing": "Herrenbekleidung",
    "jewelery": "Schmuck",
    "electronics": "Elektronik",
    "women's clothing": "Damenbekleidung",
}

translator = MyMemoryTranslator(
    source="english",
    target="german",
)

CACHE_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "translation_cache.json"
)


def load_translation_cache():
    """Load previously translated descriptions."""
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))

    return {}


def save_translation_cache(cache):
    """Save translations to avoid translating the same text again."""
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def translate_description(description, cache):
    """Translate an English product description into German."""
    if not description:
        return description

    if description in cache:
        return cache[description]

    # MyMemory requests have a text-length limit.
    words = description.split()
    chunks = []
    current_chunk = ""

    for word in words:
        candidate = f"{current_chunk} {word}".strip()

        if len(candidate) > 450 and current_chunk:
            chunks.append(current_chunk)
            current_chunk = word
        else:
            current_chunk = candidate

    if current_chunk:
        chunks.append(current_chunk)

    try:
        translated_chunks = [
            translator.translate(chunk)
            for chunk in chunks
        ]
    except Exception as error:
        logger.exception("Übersetzung der Produktbeschreibung fehlgeschlagen")
        raise RuntimeError(
            "Description translation failed. "
            "Check your internet connection or translation-service limits."
        ) from error

    translated_description = " ".join(translated_chunks)

    cache[description] = translated_description
    save_translation_cache(cache)

    return translated_description


def transform_products(products):
    """Transform product data and translate it into German."""
    logger.info("Starte Transformation für %s Produkte", len(products))

    cache = load_translation_cache()
    transformed_products = []

    for product in products:
        transformed_product = {
            "id": product["id"],
            "title": product["title"],
            "price": product["price"],
            "description": translate_description(
                product["description"],
                cache,
            ),
            "category": CATEGORY_TRANSLATIONS.get(
                product["category"],
                product["category"],
            ),
            "image": product["image"],
            "rating_rate": product["rating"]["rate"],
            "rating_count": product["rating"]["count"],
        }

        transformed_products.append(transformed_product)

    logger.info(
        "Transformation abgeschlossen: %s Produkte verarbeitet",
        len(transformed_products),
    )

    return transformed_products
