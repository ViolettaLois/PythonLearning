import re


def get_number_of_words(string):
    words = 0
    string = clear_punctuation(string)
    string = clear_repeating_whitespaces(string)

    for index, symbol in enumerate(string):
        if symbol == " ":
            words += 1

    words += 1
    return words


def clear_repeating_whitespaces(string):
    new_string = ""
    for index, symbol in enumerate(string):
        if string[index] == " " and string[index-1] == " ":
            continue
        else:
            new_string += symbol

    return new_string.strip()


def clear_punctuation(string):
    punctuation_characters = [",", ".", "!", "?", "-"]
    new_string = ""
    for index, symbol in enumerate(string):
        if symbol not in  punctuation_characters:
            new_string += symbol
    return new_string


def remove_character_by_index(string,index):
    return string[:index] + string[index+1:]


def split_string_into_words(string):
    new_string = re.findall("[a-zA-Z0-9]+", string)
    return new_string


def get_longest_word(string):
    words = split_string_into_words(string)
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore " \
              "et dolore magna aliqua."
number_of_words = get_number_of_words(test_string)
longest_word = get_longest_word(test_string)
print("Test string is: " + test_string)
print("Number of words: " + str(number_of_words))
print("The longest word: " + longest_word)









