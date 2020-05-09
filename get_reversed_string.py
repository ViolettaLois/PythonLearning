def get_reversed_string(string):
    new_string = ""
    index = (len(string) - 1)
    for i in range(0, len(string)):
        new_string += string[index]
        index -= 1
    return new_string


test_string = "he loves avocado"
result = get_reversed_string(test_string)
print("Test string: " + test_string)
print("Reversed string: " + result)
