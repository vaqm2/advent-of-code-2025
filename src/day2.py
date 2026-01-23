#!/usr/bin/env python3

def is_invalid(product_id: int) -> bool:
    """
    Check if the product ID is valid.
    """
    product_id_str = str(product_id)
    product_id_str_length = len(product_id_str)
    for i in range(1, product_id_str_length//2 + 1):
        if product_id_str_length % i != 0:
            continue
        step = i
        while step < product_id_str_length:
            if product_id_str[0:i] != product_id_str[step:step + i]:
                break
            step += i
            if step >= product_id_str_length:
                return True
    return False


def main() -> None:
    with open("/input/input_day_2_1.txt", "r") as f:
        product_id_ranges = f.read().strip()
    product_id_ranges_list = product_id_ranges.split(',')
    sum = 0
    for product_id_range in product_id_ranges_list:
        start_id, end_id = product_id_range.split('-')
        for product_id_num in range(int(start_id), int(end_id) + 1):
            if is_invalid(product_id_num):
                sum += product_id_num
    print(f"Sum of invalid product IDs: {sum}")

if __name__ == "__main__":
    main()