import json
import requests
import pandas as pd

from typing import List
from models.actual_product import ActualProduct
from models.expected_product import ExpectedProduct
from decouple import config


def get_products_list_from_url() -> List[ActualProduct]:
    """
    Fetches data from the API and returns a list of Actual Product objects.

    Returns:
        List[actual_product]: A list of actual_product objects.
    """
    try:
        response = (requests.get
                    (config('URL'), params={'limit': config('PAYLOAD')}))
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        products_list = data.get('products', [])
        products = [
            ActualProduct(
                product['id'],
                product['title'],
                product['price'],
                product['discountPercentage']
            ) for product in products_list
        ]
        return products
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []


def get_products_list_from_file() -> List[ExpectedProduct]:
    """
    Reads product data from a parquet file and
    returns a list of expected_product objects.

    Returns:
        List[expected_product]: A list of expected_product objects.
    """
    df = pd.read_parquet(config('EXPECTED_DATA_FILE_PATH'))
    json_string = df.to_json(orient='records')
    json_object = json.loads(json_string)
    products = [
        ExpectedProduct(
            product['id'],
            product['title'],
            product['final_price']
        ) for product in json_object
    ]
    return products


def show_product_with_highest_price(
        actual_products_list: List[ActualProduct]
) -> None:
    """
    Finds and displays the actual product with the highest calculated price.

    Args:
        products_list (List[actual_product]): A list of actual_product objects.
    """
    product_with_highest_price = (
        max(actual_products_list, key=lambda x: x.calculated_price))
    print("===================================================")
    print(f"Product in actual data with Highest Price is ==>> ID: "
          f"{product_with_highest_price.id} || "
          f" Title: {product_with_highest_price.title} || "
          f"Price: {product_with_highest_price.price}")


def show_details_of_products_that_are_missing_in_expected_data(
        actual_products_list: List[ActualProduct],
        expected_products_list: List[ExpectedProduct]
) -> None:
    """
    Finds and displays the products in the actual list
    that are missing in the expected list.

    Args:
        actual_products_list (List[actual_product]):
        A list of actual_product objects.
        expected_products_list (List[expected_product]):
        A list of expected_product objects.
    """
    difference = [
        actual for actual in actual_products_list
        if not any(expected.title == actual.title
                   for expected in expected_products_list)
    ]

    print("===================================================")
    print("Details of Products that are missing in expected data:")
    print("===================================================")

    for diff in difference:
        print(f'ID: {diff.id} || '
              f'Title: {diff.title} || '
              f'Final Price: {diff.calculated_price}')
        print("--------------------------------------------------------")

    print("===================================================")


def show_details_of_products_that_have_matching_price(
        actual_products_list: List[ActualProduct],
        expected_products_list: List[ExpectedProduct]
) -> None:
    """
    Finds and displays the products in the actual list
    that have matching final prices in the expected list.

    Args:
        actual_products_list (List[actual_product]):
        A list of actual Product objects.
        expected_products_list (List[expected_product]):
        A list of expected Product objects.
    """
    intersection = [
        actual for actual in actual_products_list
        if any(expected.final_price == actual.calculated_price
               for expected in expected_products_list)
    ]

    print(f"{intersection.__len__()} Products have matching price.")

    print("===================================================")
