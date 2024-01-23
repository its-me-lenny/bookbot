def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    count_words(text)
    char_dict = count_char(text)
    report_count_alpha(char_dict)
    print(f"\n--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    no_of_words = len(words)
    print(f"{no_of_words} words found in the document\n")

def count_char(text):
    char_dict = {}
    for word in text:
        lc_word = word.lower()
        for char in lc_word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    return char_dict

def val_return(e):
    return e[1]

def report_count_alpha(char_dict):
    char_dict_list = list(char_dict.items())
    char_dict_list.sort(key=val_return, reverse=True)
    for cd in char_dict_list:
        if cd[0].isalpha():
            print(f"The '{cd[0]}' character was found {cd[1]} times")
    



main()