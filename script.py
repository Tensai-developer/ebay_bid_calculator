def calculate_total_cost(item_price, shipping_cost):
    fee_cost = (item_price * 0.12) + .30
    after_fees = item_price - fee_cost - shipping_cost
    return after_fees

def calculate_budget(item_price_listed):
    return item_price_listed * 0.7

def main():
    auction_items = []
    item_cost = 0

    while True:
        item_name = input("Enter the name of the item (or press Enter to finish): ")
        if item_name == "":
            break

        list_item_price = float(input("Enter the price of the average item price: "))
        shipping_cost = float(input("Enter the shipping cost for the item: "))

        total_cost = calculate_total_cost(list_item_price, shipping_cost)
        item_budget = calculate_budget(total_cost)
        item_cost += item_budget

        auction_items.append((item_name, list_item_price, shipping_cost, total_cost, item_budget))

    print("\nAuction Items:")
    for item in auction_items:
        print(f"Item: {item[0]}, Listed Price: ${item[1]:.2f}, Shipping Cost: ${item[2]:.2f}, Profit After Fees: ${item[3]:.2f}, Max bid Limit: ${item[4]:.2f}")

    print(f"\nTotal Budget: ${item_cost:.2f}")

    total_costs = sum(item[3] for item in auction_items)
    print(f"After Fees: ${total_costs:.2f}")

    if total_costs > item_cost:
        print("Warning: The total costs exceed your total budget!")
    else:
        remaining_budget = item_cost - total_costs
        print(f"Remaining Budget: ${remaining_budget:.2f}")

if __name__ == "__main__":
    main()
