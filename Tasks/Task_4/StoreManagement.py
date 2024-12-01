from prettytable import PrettyTable

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = self.read_products()
        
    def read_products(self):
        return [
            Product("Notebook", 50.0, 500),
            Product("Pen", 10.0, 1000),
            Product("Pencil", 5.0, 1500),
            Product("Eraser", 3.0, 800),
            Product("Ruler", 20.0, 300)
        ]

    def print_product_table(self):
        product_table = PrettyTable()
        product_table.field_names = ["Name", "Price", "Quantity"]
        for product in self.products:
            stock_status = product.quantity if product.quantity > 0 else "Out of Stock"
            product_table.add_row([product.name, product.price, stock_status])
        print("\nProducts Available:")
        print(product_table)

    def get_valid_product(self, product_name):
        """Check if a product exists and return it."""
        return next((p for p in self.products if p.name.lower() == product_name.lower()), None)

    def get_product_choice(self):
        total_discounted_price = 0
        while True:
            self.print_product_table()
            product_name = input("Enter Product Name: ").strip().lower()
            product = self.get_valid_product(product_name)

            if product is None:
                print("Product not found. Please try again.")
                continue

            if product.quantity == 0:
                print(f"Sorry, {product.name} is out of stock.")
                continue

            try:
                quantity_required = int(input("Enter Quantity Required: "))
                if quantity_required <= 0:
                    print("Quantity must be a positive number.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if quantity_required > product.quantity:
                print(f"Insufficient quantity. Available stock: {product.quantity}.")
                continue

            # Calculate discount
            discount_quantity = quantity_required // 250
            discount_percentage = min(5.0 * discount_quantity, 25.0)
            discounted_price = quantity_required * product.price * (1 - discount_percentage / 100)
            product.quantity -= quantity_required
            total_discounted_price += discounted_price

            print(f"Discounted Price: ${discounted_price:.2f}")
            print(f"Remaining Stock for {product.name}: {product.quantity}")
            
            another_item = input("Do you want to add another item? (yes/no): ").strip().lower()
            if another_item != 'yes':
                break

        return total_discounted_price

    def process_payment(self, total_discounted_price):
        delivery_charge = 200
        pickup_charge = 50

        while True:
            delivery_option = input("Do you want delivery or pick-up? (Enter 'delivery' or 'pick-up'): ").strip().lower()
            if delivery_option == 'delivery':
                total_discounted_price += delivery_charge
                break
            elif delivery_option == 'pick-up':
                total_discounted_price += pickup_charge
                break
            else:
                print("Invalid option. Please choose 'delivery' or 'pick-up'.")

        payment_currency = input("Choose a payment currency (USD, EUR, EGP): ").strip().upper()
        usd_to_eur_rate = 0.92
        usd_to_egp_rate = 30.90

        if payment_currency == "USD":
            total_price_in_chosen_currency = total_discounted_price
        elif payment_currency == "EUR":
            total_price_in_chosen_currency = total_discounted_price * usd_to_eur_rate
        elif payment_currency == "EGP":
            total_price_in_chosen_currency = total_discounted_price * usd_to_egp_rate
        else:
            print("Invalid currency choice. Defaulting to USD.")
            total_price_in_chosen_currency = total_discounted_price

        print(f"\nTotal Discounted Price in {payment_currency}: ${total_price_in_chosen_currency:.2f}")

    def main(self):
        self.print_product_table()
        total_discounted_price = self.get_product_choice()
        print(f"\nTotal Discounted Price: ${total_discounted_price:.2f}")
        self.process_payment(total_discounted_price)
        print("\nThank you for shopping with us! Your order is on the way!")

if __name__ == "__main__":
    store = Store()
    store.main()
