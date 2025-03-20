# creating three contacts using a dictionary 
new_contact1 = {
    'full_name': 'Tom Smith',
    'phone': '718-123-4567'
}
new_contact2 = {
    'full_name': 'Samantha Green',
    'phone': '212-222-3333'
}
new_contact3 = {
    'full_name': 'Bill Lewis',
    'phone': '646-444-5555'
}

print(new_contact1['full_name'].ljust(15), new_contact1['phone'].ljust(15))
print(new_contact2['full_name'].ljust(15), new_contact2['phone'].ljust(15))
print(new_contact3['full_name'].ljust(15), new_contact3['phone'].ljust(15))


print()
'''
Remove phone key for second contact using the popitem which removes the last key.
'''

new_contact2.popitem()

#Use get method to avoid any errors for missing keys.
print(new_contact1['full_name'].ljust(15), new_contact1.get('phone', 'N/A').ljust(15))
print(new_contact2['full_name'].ljust(15), new_contact2.get('phone', 'N/A').ljust(15))
print(new_contact3['full_name'].ljust(15), new_contact3.get('phone', 'N/A').ljust(15))