def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item= input("enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} has been added to the shopping list")
            else:
                print("no item added")
        elif choice == '2':
            # Prompt for and remove an item
            item= input("enter the item u want to remove").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed")
            else:
                print("no item removed")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("\n your shopping list")
                for i, item in enumerate (shopping_list, start=1):
                    print(f"{i}. {item}\n")
            else:
                print("ur shopping list is currently empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()