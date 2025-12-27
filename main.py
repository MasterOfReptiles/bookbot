from stats import get_word_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        f.close()
        return file_contents

def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(book_contents)
    print(f"Found {num_words} total words")

main()