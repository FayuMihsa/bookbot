def get_word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_character_count(text):
    letter_count = {}
    for letter in text.lower():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count

def sort_on(dictionary):
    return dictionary["count"]

def sort_character_count(characters):
    char_list = []
    for char in characters:
        count = characters[char]
        new_dict = {"char":char, "count": count}
        char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list