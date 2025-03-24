class Item:
    def __init__(self, item_id, name, description, price):
        if isinstance(item_id, int) and item_id > 0:
            self.item_id = item_id
        else:
            print("Invalid ID, setting to 1")
            self.item_id = 1
        
        if name.strip() != "" and isinstance(name, str):
            self.name = name.strip()
        else:
            print("Invalid name, using default name")
            self.name = "Unnamed"

        self.description = description

        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            print("Invalid price, setting to 0.0")
            self.price = 0.0


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            print(f"Item with ID {item_id} already exists. Try a different ID.")
            return
        item = Item(item_id, name, description, price)
        self.items[item_id] = item
        print("Item created successfully!")

    def read_item(self, item_id):
        if item_id in self.items:
            item = self.items[item_id]
            print(f"ID: {item.item_id}")
            print(f"Name: {item.name}")
            print(f"Description: {item.description}")
            print(f"Price: {item.price}")
        else:
            print("Item not found!")

    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id in self.items:
            item = self.items[item_id]
            if name:
                item.name = name.strip() if name.strip() else item.name
            if description:
                item.description = description
            if price:
                try:
                    item.price = float(price) if float(price) > 0 else item.price
                except:
                    print("Invalid price. Skipping update.")
            print("Item updated successfully!")
        else:
            print("Item not found!")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Item not found!")


def main():
    manager = ItemManager()

    while True:
        # Print the menu inside the loop to display it every time
        print("\nItem Management System")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                item_id = int(input("Enter Item ID: "))
                name = input("Enter Item Name: ")
                description = input("Enter Item Description: ")
                price = float(input("Enter Item Price: "))
                manager.create_item(item_id, name, description, price)
            except:
                print("Invalid input. Please try again.")

        elif choice == "2":
            try:
                item_id = int(input("Enter Item ID: "))
                manager.read_item(item_id)
            except:
                print("Invalid ID. Please enter a number.")

        elif choice == "3":
            try:
                item_id = int(input("Enter Item ID: "))
                name = input("Enter new name (leave blank to skip): ")
                description = input("Enter new description (leave blank to skip): ")
                price = input("Enter new price (leave blank to skip): ")
                manager.update_item(item_id, name or None, description or None, price or None)
            except:
                print("Invalid input.")

        elif choice == "4":
            try:
                item_id = int(input("Enter Item ID: "))
                manager.delete_item(item_id)
            except:
                print("Invalid ID. Please enter a number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
