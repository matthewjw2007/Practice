# This program checks to see if two words are an anagram of one another through the use of a frequency counter


# Valid anagram function
def valid_anagram(str_one, str_two):
    # Create two dicts
    dict_one = {}
    dict_two = {}

    # Verify the two inputs are the same size
    if len(str_one) != len(str_two):
        print("Different lengths, strings entered are not anagrams")
        return False

    # Transfer strings into the dicts

    # Compare the dicts

    # If all tests pass, return true
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
