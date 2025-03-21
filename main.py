import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count


def get_book_text(filepath):
    with open(filepath) as f:
        booktext = f.read()
    return booktext

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    num_words = get_word_count(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count = get_character_count(text)
    sorted_character_count = sort_character_count(character_count)
    for item in sorted_character_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


main()