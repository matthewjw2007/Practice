# Matthew Esqueda
# Program: Valid Anagram
# Description: This program checks to see if two words are an anagram of one another through the use of a frequency
# counter. The frequency counter is seeing what characters are in the words and how many times each character appears.
# Date: December 14, 2019


# Valid anagram function
def valid_anagram(str_one, str_two):
    # Turn entered strings into sorted lists
    list_one = sorted(list(str_one))
    list_two = sorted(list(str_two))

    # Create two dicts
    dict_one = {}
    dict_two = {}

    # Verify the two inputs are the same size
    if len(str_one) != len(str_two):
        print("Different lengths, strings entered are not anagrams")
        return False

    # Transfer lists into the dicts
    for key in list_one:
        # If the key is not in the dictionary already, then add the key and give it a value of 1
        if key not in dict_one.keys():
            dict_one[key] = 1
        # If the key exists, increase the value by 1
        else:
            dict_one[key] += 1

    for key in list_two:
        if key not in dict_two.keys():
            dict_two[key] = 1
        else:
            dict_two[key] += 1

    # Compare the dicts by seeing if they have the same keys and that they keys have the same values
    for key in dict_one:
        # Verify the keys in dict_one exist in dict_two
        if key not in dict_two.keys():
            print("Not anagrams")
            return False
        # Verify the values of the keys match
        if dict_one[key] != dict_two[key]:
            print("Values do not match, not anagrams")
            return False

    # If all tests pass, return true
    print("Those two words are anagrams")
    return True


if __name__ == "__main__":
    # Variables

    # Get user input
    print("Enter two words and I will let you know if they are an anagram")
    input_one = input("First Word: ")
    input_two = input("Second Word: ")

    print("I will compare the following words: " + input_one + " and " + input_two)

    # Call function
    valid_anagram(input_one, input_two)
