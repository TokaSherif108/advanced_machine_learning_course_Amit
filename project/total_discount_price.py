from prettytable import PrettyTable
    
products=[
    {"Name": "water", "Price": 80.0, "Quantity": 1200},
    {"Name": "Soda", "Price": 130.0, "Quantity": 1200},
    {"Name": "Chips", "Price": 75.0, "Quantity": 1200},
    {"Name": "Bread", "Price": 45.0, "Quantity": 1200},
    {"Name": "Eggs", "Price": 65.0, "Quantity": 1200}]

table = PrettyTable()
table.field_names = ["Name", "Price", "Quantity"]
for product in products:
    table.add_row([product["Name"], product["Price"], product["Quantity"]])
print(table)
total_discount_price=0
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