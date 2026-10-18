
from extract import extract_products
from transform import transform_products


products = extract_products()
transformed_products = transform_products(products)

print(f"Products transformed: {len(transformed_products)}")
print("\nFirst transformed product:")
print(transformed_products[0])
