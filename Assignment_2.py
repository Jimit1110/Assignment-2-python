class Product:
    def __init__(self, name, price, quantity, product_type):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_type = product_type

    def __str__(self):
        return f"{self.name}, {self.price} RS, {self.quantity}, {self.product_type}"

def print_inventory(inventory):
    print("Inventory:")
    for product in inventory:
        print(product)
    print()

def main():
    # Initial inventory with some pre-defined products
    inventory = [
        Product("lettuce", 10.5, 50, "Leafy green"),
        Product("cabbage", 20, 100, "Cruciferous"),
        Product("pumpkin", 30, 30, "Marrow"),
        Product("cauliflower", 10, 25, "Cruciferous"),
        Product("zucchini", 20.5, 50, "Marrow"),
        Product("yam", 30, 50, "Root"),
        Product("spinach", 10, 100, "Leafy green"),
        Product("broccoli", 20.2, 75, "Cruciferous"),
        Product("garlic", 30, 20, "Leafy green"),
        Product("silverbeet", 10, 50, "Marrow")
        ]


    print("Total number of products:", len(inventory), "\n")   
    
    # Dynamically add new products to the inventory
    while True:

        choice=input("Do you want to add new product:(yes/no)")
        if choice=='yes':
            name = input("Enter product name: ")
            price = float(input("Enter product price (RS): "))
            quantity = int(input("Enter product quantity: "))
            product_type = input("Enter product type: ")
            new_product = Product(name, price, quantity, product_type)
            inventory.append(new_product)
            print("Product added successfully!\n")
        
        elif choice=='no':
            break
        else:
            print("please enter valid choice")


    print("Total number of products:", len(inventory), "\n")
    print_inventory(inventory)
    

    # Print products of type 'Leafy green'
    leafy_green_products = [product for product in inventory if product .product_type == "Leafy green"]
    print("Leafy green products:")
    print_inventory(leafy_green_products)
    

    # Remove 'garlic' from the inventory
    inventory = [product for product in inventory if product.name != "garlic"]
    print("garlic is sold out so,")
    print("Total number of products left:", len(inventory), "\n")


    # Dynamically add quantity to existing products in the inventory
    while True:
        add_qty = input("Do you want to add quantity to existing product?(yes/no): ")
        if add_qty=='yes':
            product_name = input("Enter the name of the product to add quantity: ")
            quantity_to_add = int(input(f"Enter the quantity to add for {product_name}: "))
    
            product_found = False
            for product in inventory:
                if product.name.lower() == product_name.lower():
                    product.quantity += quantity_to_add
                    print(f"quantity of {product_name} updated !!!")
                    product_found = True
                    break
    
            if product_found:
                print(f"Final quantity of {product_name} in the inventory: {product.quantity}\n")
            else:
                print(f"{product_name} not found in the inventory. Please add the product first.\n")
        elif add_qty=='no':
            break
        else:
            print("enter valid option")
    
    
    # Calculate the total cost for specific purchases
    purchase_list = [
        {"name": "lettuce", "quantity": 1},
        {"name": "zucchini", "quantity": 2},
        {"name": "broccoli", "quantity": 1}
    ]
    total_cost = sum(product.price * purchase["quantity"] for purchase in purchase_list for product in inventory if product.name == purchase["name"])
    # Print the total cost rounded to the nearest integer
    print("Total cost of 1kg lettuce, 2kg zucchini, 1kg broccoli:", round(total_cost), "RS\n")
		

if __name__ == "__main__":
    main()