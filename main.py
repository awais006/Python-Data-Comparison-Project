from helper_methods.helper_methods import (
    get_products_list_from_url, get_products_list_from_file,
    show_product_with_highest_price,
    show_details_of_products_that_are_missing_in_expected_data,
    show_details_of_products_that_have_matching_price)


def main() -> None:
    actual_products_list = get_products_list_from_url()
    expected_products_list = get_products_list_from_file()

    show_product_with_highest_price(actual_products_list)
    (show_details_of_products_that_are_missing_in_expected_data
     (actual_products_list, expected_products_list))
    (show_details_of_products_that_have_matching_price
     (actual_products_list, expected_products_list))


if __name__ == '__main__':
    main()
