def add_contact(contacts, name, phone_number):
    contacts[name] = phone_number
    print("Contact added successfully!")

def search_contact(contacts, name):
    if name in contacts:
        print(f"Name: {name}, Phone Number: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def view_contacts(contacts):
    if contacts:
        print("Contacts:")
        for name, phone_number in contacts.items():
            print(f"Name: {name}, Phone Number: {phone_number}")
    else:
        print("No contacts found.")

def main():
    contacts = {}
    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_contact(contacts, name, phone_number)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(contacts, name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
        elif choice == '4':
            view_contacts(contacts)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
