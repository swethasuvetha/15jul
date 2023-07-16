# Initialize an empty dictionary
my_dict = {}

while True:
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Print")
    print("5. Stop/Exit")

    option = input("Enter your choice: ")

    if option == "1":
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        my_dict[key] = value
        print("Record added successfully!")

    elif option == "2":
        key = input("Enter the key to edit: ")
        if key in my_dict:
            value = input("Enter the new value: ")
            my_dict[key] = value
            print("Value updated successfully!")
        else:
            print("Key not found!")

    elif option == "3":
        key = input("Enter the key to delete: ")
        if key in my_dict:
            del my_dict[key]
            print("Key deleted successfully!")
        else:
            print("Key not found!")

    elif option == "4":
        print("Dictionary:", my_dict)

    elif option == "5":
        print("Stopping the program...")
        break

    else:
        print("Invalid option! Please try again.")

print("Program execution stopped.")
