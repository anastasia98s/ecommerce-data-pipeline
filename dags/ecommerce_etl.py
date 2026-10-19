

from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="ecommerce_etl",
    schedule= None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["ecommerce", "etl"],
)
def ecommerce_etl():

    @task
    def extract():
        from extract import extract_products

        products = extract_products()
        print(f"Extracted {len(products)} products")
        return products

    @task
    def transform(products):
        from transform import transform_products

        transformed_products = transform_products(products)
        print(f"Transformed {len(transformed_products)} products")
        return transformed_products

    @task
    def validate(products):
        from validate import validate_products

        validate_products(products)
        print("Data quality checks passed!")
        return products

    @task
    def load(products):
        from load import load_products

        load_products(products)
        print(f"Loaded {len(products)} products into PostgreSQL")

    raw_products = extract()
    transformed_products = transform(raw_products)
    validated_products = validate(transformed_products)
    load(validated_products)


ecommerce_etl()
