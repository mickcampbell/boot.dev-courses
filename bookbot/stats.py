
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(path_to_file):
    text = get_book_text(path_to_file).lower()
    words = text.split()
    return len(words)

def count_characters(path_to_file) -> dict[str, int]:
    char_count = {}
    text = get_book_text(path_to_file).lower()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(entry: tuple[str, int]) -> int:
    return entry[1]

def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    char_list = []

    for char in char_count:
        char_list.append((char, char_count[char]))

    char_list = sorted(char_list, key=sort_on, reverse=True)

    return char_list

