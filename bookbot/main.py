import sys

from stats import count_words,count_characters,chars_dict_to_sorted_list

def print_report(path_to_file, words, character_count):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char, count in character_count:
        print(f"{char}: {count}")
    print("============= END ===============")




def main():
    sys_check = len(sys.argv)

    if sys_check != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]

    words = count_words(book_path)
    characters = count_characters(book_path)
    character_count = chars_dict_to_sorted_list(characters)

    print_report(book_path, words, character_count)

main()