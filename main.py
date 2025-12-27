from stats import get_word_count, get_character_count, sort_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        f.close()
        return file_contents
    
def print_report(path,words,characters):
    print(f'''============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------''')
    for item in characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    path_to_book = "./books/frankenstein.txt"
    book_contents = get_book_text(path_to_book)
    num_words = get_word_count(book_contents)
    character_dictionary = get_character_count(book_contents)
    list_of_characters = sort_dictionary(character_dictionary)
    print_report(path_to_book,num_words,list_of_characters)


main()