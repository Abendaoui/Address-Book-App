from contact import *
from address_book import *

def main():
    print('Welcome To Address Book Application.')
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Display All Contacts")
        print("2. Search Contact")
        print("3. Add Contact")
        print("4. Close.")
        choice = input("Enter your choice: ")

        if choice == '1':
            address_book.get_contacts()
        elif choice == "2":
            search = input("Please Enter Contact name or Contact number : ")
            address_book.get_search_contacts(search)
            pass
        elif choice == "3":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            address_book.add_contact(contact)
            print("Contact added successfully!")
            pass
        elif choice == "4":
            print("Colsing...")
            break
        else:
            print("Invalid choice. Please try again.")
    
    
if __name__ == "__main__":
    main()



