"""
Counts the number of words is a book
"""
import sys
from stats import get_num_words, get_char_counts, sort_dict


def get_book_text(path_to_file):
    """Opens a file and prints its contents to console

    Args:
        path_to_file (string): path to file to be opened
    """
    with open(path_to_file) as f:
        return f.read()


def main():
    """
    Main entry point for the program. This function initializes and
    coordinates the execution of the program's core logic.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_dict = get_char_counts(book_text)
    sorted_list_of_dicts = sort_dict(char_dict)
    for char_dict in sorted_list_of_dicts:
        char = char_dict["character"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char_dict["character"]}: {char_dict["count"]}")



main()
