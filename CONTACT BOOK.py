Phone_Book = {
    "waleed": "03452562290",
    "hamza": "03138635661",
    "afeef obaid": "03234104522",
    "dad": "03004169582",
    "bahauddin": "03154155779",
    "samia": "03344201696",
    "salman": "03484569123",
    "zain": "03174846585",
    "huzaifa": "03493434677",
    "ali hassan": "03234133785"
}


def display_menu():
    print("Phone Book Menu:")
    print("S: Search contact by name")
    print("N: List names of all contacts")
    print("C: Display all contacts")
    print("R: Delete a contact number")
    print("U: Update a contact number")
    print("CL: Clear phone book")
    print("AD: Add a new contact")
    print("Q: Quit")


def search_contact():
    name = input("Enter a name: ")
    if name in Phone_Book:
        print(f"Contact Number: {Phone_Book[name]}")
    else:
        print("Contact not found.")


def list_names():
    for name in Phone_Book.keys():
        print(name)


def display_contacts():
    for name, number in Phone_Book.items():
        print(f"{name}: {number}")


def delete_contact():
    name = input("Enter the name to delete: ")
    if name in Phone_Book:
        deleted_number = Phone_Book.pop(name)
        print(f"Deleted contact: {name}, {deleted_number}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name to update: ")
    if name in Phone_Book:
        new_number = input("Enter the new contact number: ")
        Phone_Book[name] = new_number
        print("Contact updated.")
    else:
        print("Contact not found.")


def clear_phone_book():
    Phone_Book.clear()
    print("Phone book cleared.")


def add_contact():
    name = input("Enter the name of the new contact: ")
    number = input("Enter the contact number: ")
    Phone_Book[name] = number
    print("Contact added.")


def main():
    while True:
        display_menu()
        purpose = input("Enter your choice (S/N/C/R/U/CL/AD/Q): ").upper()

        if purpose == "S":
            search_contact()
        elif purpose == "N":
            list_names()
        elif purpose == "C":
            display_contacts()
        elif purpose == "R":
            delete_contact()
        elif purpose == "U":
            update_contact()
        elif purpose == "CL":
            clear_phone_book()
        elif purpose == "AD":
            add_contact()
        elif purpose == "Q":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
