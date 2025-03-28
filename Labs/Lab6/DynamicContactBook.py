# create empty dictionaries to start.
new_contact1 = dict();
new_contact2 = dict();

#you can also create an empty dict with curly braces
new_contact3 = {};

# get the information for each contact below from the end user. 
new_contact1['full_name'] = input("Enter full name for contact 1: ")
new_contact1['phone'] = input("Enter phone number for contact 1: ")
print()

new_contact2['full_name'] = input("Enter full name for contact 2: ")
new_contact2['phone'] = input("Enter phone number for contact 2: ")
print()

new_contact3['full_name'] = input("Enter full name for contact 3: ")
new_contact3['phone'] = input("Enter phone number for contact 3: ")
print()

#creating a list with the contacts
contacts = [
    new_contact1, 
    new_contact2,
     new_contact3
]




'''
Iterate over items in the contacts List.
NOTE: we will discuss loops at a later time. For now, type everything you see below including ALL indentations.
'''

print("Contact Directory: ")
#Output 1
contact_id = 1
for contact in contacts:
    #Below we are accessing the keys by their name:
    print(f"{contact_id}) {contact['full_name']:<15s}{contact['phone']:<15s}")

    contact_id = contact_id + 1
print()


    #updating the content section
contact_index_to_update = int(input("Which contact do you want to update? "))

    # Since the index is off by one from the natural count we are going to add - 1.
contact_index_to_update = contact_index_to_update -1

print(f"\nUpdating contact: {contacts[contact_index_to_update]['full_name']} \n")

contacts[contact_index_to_update]['full_name'] = input(f"Enter new full name: ")
contacts[contact_index_to_update]['phone'] = input("Enter new phone number: ")
print()
# Output 2
print("Contact Directory: ")
contact_id = 1
for contact in contacts:
    print(f"{contact_id}) {contact['full_name']:<15s}{contact['phone']:<15s}")

    contact_id = contact_id + 1
print()

contact_index_to_delete = int(input("Which contact do you want to delete? "))
contact_index_to_delete = contact_index_to_delete -1
print()

    #Removing the contact from list
del contacts[contact_index_to_delete]

    #Output3
print("Contact Directory: ")
contact_id = 1
for contact in contacts:
    print(f"{contact_id}) {contact['full_name']:<15s}{contact['phone']:<15s}")

    contact_id = contact_id + 1