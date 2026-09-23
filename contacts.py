import json
import os

#Check if file already exists.
if os.path.exists("contacts_data.json"):
    with open("contacts_data.json", "r") as file:
        contacts = json.load(file)
else:
    contacts = {}

#add contacts
def add_contacts(contact):
    name = input("Enter Name: ")
    number = input("Number: ")
    email = input("Email: ")
    address = input("Address: ")

    if name in contact:
        contact[name]["Number"] = number
        contact[name]["Email"] = email
        contact[name]["Address"] = address
    else:
        contact[name] = {"Number": number, "Email": email, "Address": address}
    print("Details added successfully.\n")

#search contacts
def search_contacts(contact):
    name = input("Enter name to search: ")
    if name in contact.keys():
        return f"{name}: {contact[name]}\n"
    else:
        return "\nNot found.\n"

#delete contacts
def delete_contacts(contact):
    name = input("Enter name to delete: ")
    try:
        del contact[name]   
        print("Contact deleted successfully.\n")
    except:
        print("The person is not in contacts.\n")


#Execution
print("\n=== WELCOME TO MY CONTACT MANAGER ===\n")

while True:
    action = input("ENTER ACTION: add, search, delete, stop? ")
    action = action.lower()
    if action == "add":
        add_contacts(contacts)
    elif action == "search":
        print(search_contacts(contacts))
    elif action == "delete":
        delete_contacts(contacts)
    elif action == "stop":
        break
    else:
        print("Enter Action correctly.\n")

print("\nYou Exited the program.\n")             #Unless you stop the program the data wont be stored in the file.

with open("contacts_data.json", "w") as file:
    json.dump(contacts, file, indent=4)
