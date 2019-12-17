# Matthew Esqueda
# Program: Unique Values
# Description: This program uses "pointers" to check how many unique values a list has and returns the total.
# Last Update: December 16, 2019


# Functions
def unique_values(lst):
    # Variables
    unique_list = []

    # Loop through list, counting how many unique values it has
    for i in lst:
        # Check if value is in unique list
        if i not in unique_list:
            unique_list.append(i)

    total = len(unique_list)

    return total


if __name__ == "__main__":
    # Variables
    lst = []
    i = 0
    total_unique_values = 0

    print("This program will count the total number of unique values in a list containing ints.")

    # Get the amount of values the user wants to enter
    list_size = int(input("How many values will you be entering: "))

    # Fill the list
    while i < list_size:
        value = int(input("Add value " + str(i + 1) + ": "))

        lst.append(value)

        i += 1

    # Call unique_values function
    total_unique_values = unique_values(lst)

    # Tell the user how many unique values their list has
    print("Your list: " + str(lst))
    print("Total unique values: " + str(total_unique_values))
