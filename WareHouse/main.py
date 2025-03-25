from database import create_connection, initialize_db, add_item, get_items, update_item_quantity, get_item_by_id, buy_item
from datetime import datetime

def main_menu(conn):
    while True:
        print("\nWarehouse Management System")
        print("1. View all items")
        print("2. Add new item")
        print("3. Update item quantity")
        print("4. Buy item")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            items = get_items(conn)
            print("\nAll items:")
            for item in items:
                print(item)

        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            employee_name = input("Enter employee name: ")
            city = input("Enter city: ")
            add_item(conn, name, quantity, price, employee_name, city)
            print(f"Item '{name}' added successfully.")

        elif choice == '3':
            item_id = int(input("Enter item ID: "))
            quantity = int(input("Enter quantity to subtract: "))
            update_item_quantity(conn, item_id, quantity)
            item = get_item_by_id(conn, item_id)
            print(f"\nUpdated item with ID {item_id}:")
            print(item)

        elif choice == '4':
            item_id = int(input("Enter item ID to buy: "))
            quantity = int(input("Enter quantity to buy: "))
            client_name = input("Enter client name: ")
            buy_item(conn, item_id, quantity, client_name)

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    conn = create_connection()
    initialize_db(conn)

    # examples of edding some stuff
    example_items = [
        ("Widget", 100, 1.99, "Alice", "New York"),
        ("Gadget", 50, 2.49, "Charlie", "Los Angeles"),
        ("Thingamajig", 75, 3.99, "Eve", "Chicago"),
        ("Doohickey", 30, 4.99, "Grace", "Houston"),
        ("Whatchamacallit", 20, 5.99, "Ivy", "Phoenix"),
        ("Gizmo", 60, 6.49, "Kim", "Philadelphia"),
        ("Contraption", 90, 7.99, "Mia", "San Antonio"),
        ("Doodad", 40, 8.99, "Oscar", "San Diego"),
        ("Thingamabob", 70, 9.49, "Quinn", "Dallas"),
        ("Whatsit", 80, 10.99, "Sam", "San Jose")
    ]

    for item in example_items:
        add_item(conn, *item)

    main_menu(conn)
    conn.close()

if __name__ == "__main__":
    main()
