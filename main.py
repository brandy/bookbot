import sys
from stats import get_num_words, get_char_counts, get_sorted_char_counts


def get_book_text(file_name):
    with open(file_name, 'r') as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    file_name = sys.argv[1]
    book = get_book_text(file_name)
    num_words = get_num_words(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for char, count in get_sorted_char_counts(get_char_counts(book)):
        print(f"{char}: {count}")

    print("============= END ===============")


main()
