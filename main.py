file_contents = ""
# read file
with open('books/frankenstein.txt', 'r') as file:
    file_contents = file.read()

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(dict):
    return dict["count"]

def print_report(filepath, word_count, char_count):
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")
    
    # Convert char_count to a list of dictionaries and sort
    char_list = [{"char": char, "count": count} for char, count in char_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    
    # Print character counts
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")

# Count words and characters
word_count = count_words(file_contents)
char_count = count_characters(file_contents)

# Print the report
print_report('books/frankenstein.txt', word_count, char_count)
