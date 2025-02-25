import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_highest

def main ():
# Getting the data.
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    character_count = get_character_count(book_text)
    sorted_character_count = sort_highest(character_count)
# Formatting the Console Output.

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
# Filtering out non alphabetic characters.

    for char_dict in sorted_character_count:
        for char, count in char_dict.items():
            if char.isalpha():
                print(f"{char}: {count}")    
    print("============= END ===============")

# Opening the book file and turning it into a string.

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book = f.read()
    return book


if __name__ == "__main__":
    main()