total_discount_price=0

def total_discount_price(products):
    while True:
        product_name = input("Enter Product Name: ").lower()

    # Ceck if theh entered product not exists in the list
        if product_name not in map(lambda x: x["Name"].lower(), products):
            print("Product not found in the table. Please enter a valid product.")
            continue

        quantity_required = float(input("Enter Quantity Required: "))

# Locate each input with saved data
#el for loop el 3adya msh btrg3ly 8er lma a2olha lkn el next bt return 
#el nxt 5znt el p w htlf 3leha 
#next hya function 

        product = next(p for p in products if p["Name"].lower() == product_name)

    # Check if the entered quantity is greater than the available quantity
        if quantity_required > product["Quantity"]:
            print("Insufficient quantity. Please enter a new quantity.")
            continue
    # 5% discount for every 250 quantity (CALCULATIONS)
        discount_quantity = quantity_required // 250
        discount_percentage = 5.0 * discount_quantity
        total_discount = min(discount_percentage, 25.0)  # Cap the discount at 25%
        discounted_price = quantity_required * product["Price"] * (1 - total_discount / 100)

    # Updated list after purchase
        product["Quantity"] -= quantity_required

    # total of the Added discounted price
        total_discounted_price += discounted_price

        print(f"Discounted Price: ${discounted_price:.2f}")

        another_item = input("Do you want to add another item? (yes/no): ")
        if another_item.lower() != 'yes':
            break