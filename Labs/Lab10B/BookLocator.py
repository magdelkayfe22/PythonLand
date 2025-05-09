# Book Locator Application
def find_book(call_number):
    # Decision structure to determine the location of the book in range of call numbers
    if call_number <= 99: 
        return 'Book not found!'
    
    elif call_number >= 100 and call_number <= 199:
        return 'Basement'
    
    elif call_number >= 200 and call_number <= 500 or call_number > 900:
        return 'Main Floor'
    
    elif call_number >= 501 and call_number <= 900 and not (call_number >= 700 and call_number <= 750):
        return 'Upper Floor'
    
    elif call_number >= 700 and call_number <= 750:
        return 'Archives'
    
    else:
        return 'Book not found!'
    # end of decision structure


# Message to use when exiting the application
def good_bye():
    print("Good-bye!")

# Function to retireve info from the user
def get_input():
    answer = input("Do you want to locate a book? (yes/no)? ")

    # if user doesnt want to locate a book, exit the application
    if answer.lower() == 'no':
        good_bye()
        return None
    
    if answer.lower() != 'yes':
        # recursive call to itself to show the question again
        return get_input()
    
    return int(input("\nEnter a call number: "))

# Display the results from the request.
def display_result(result):
    print(f"\n*** Location of your book: {result}", end="\n\n")

def main():
    print("{0:^40}".format("Welcome to QCC Book Locator"))
    print("=" * 40)

    keep_running = True
    # The loop below is purposefully infinite. There is logic
    # exit the application if the user doesnt want to select anymore books.
    while keep_running:
        call_number = get_input()

        if call_number == None:
            break

        location_of_book = find_book(call_number)

        display_result(location_of_book)

# Invoke main to start the application.
if __name__ == "__main__":
    main()