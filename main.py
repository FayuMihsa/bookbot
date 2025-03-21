def get_book_text(filepath):
    with open(filepath) as f:
        booktext = f.read()
    return booktext

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)


main()