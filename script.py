import csv

def calculate_total_cost(item_price, shipping_cost):
    fee_cost = (item_price * 0.12) + 0.70
    after_fees = item_price - fee_cost - shipping_cost
    return after_fees

def calculate_budget(item_price_listed):
    return item_price_listed * .7

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    auction_items = []
    item_cost = 0

    print("------------Find your item's max bid-------------------")
    
    while True:
        item_name = input("Enter the name of the item (or press Enter to finish): ")
        if item_name == "":
            break

        list_item_price = get_float_input("Enter the average listed price: ")
        shipping_cost = get_float_input("Enter the shipping cost for the item: ")

        total_cost = calculate_total_cost(list_item_price, shipping_cost)
        item_budget = calculate_budget(total_cost)
        item_cost += item_budget

        auction_items.append((item_name, list_item_price, total_cost, item_budget))

        print(f"Item '{item_name}' added. Profit After Fees: ${total_cost:.2f}, Max Bid Limit: ${item_budget:.2f}")

        finished = input("Are you finished adding items? (yes/no): ").strip().lower()
        if finished == "yes":
            break

    print("\nAuction Items Summary:")
    for item in auction_items:
        print(f"Item: {item[0]}, Listed Price: ${item[1]:.2f}, Net: ${item[2]:.2f}, Max Bid: ${item[3]:.2f}")

    print(f"\nTotal Budget: ${item_cost:.2f}")

    total_costs = sum(item[2] for item in auction_items)
    print(f"After Fees: ${total_costs:.2f}")

    if total_costs > item_cost:
        print("Warning: The total costs exceed your total budget!")
    else:
        remaining_budget = item_cost - total_costs
        print(f"Remaining Budget: ${remaining_budget:.2f}")

    # Save to CSV
    with open('auction_items.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name", "Listed Price", "Net", "Max Bid"])
        writer.writerows(auction_items)
    
    print("Auction items saved to auction_items.csv")

if __name__ == "__main__":
    main()
