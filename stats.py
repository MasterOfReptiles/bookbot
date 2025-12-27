def get_word_count(book_contents):
    word_list = book_contents.split()
    word_count = len(word_list)
    return word_count

def get_character_count(book_contents):
    book_contents_lower = book_contents.lower()
    book_contents_withot_spaces = book_contents_lower.replace(' ','')
    letters = {}
    for char in book_contents_withot_spaces:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] =1
    return letters

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    dictionary_list = []
    for item in dictionary:
        dictionary_list.append({"char" : item, "num" : dictionary[item]}) 
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list

