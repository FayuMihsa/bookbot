# Splitting the text into a list of strings and counting the amount.

def get_num_words(text):
    words = text.split()
    return len(words)

# Converting characters to lower case and counting individual characters.

def get_character_count(text):
    character_count = {}
    lower_case = text.lower()
    for case in lower_case:
        if case not in character_count:
            character_count[case] = 1
        else:
            character_count[case] += 1
    return character_count

# Sorting the dictionary by highest count.

def sort_highest(dict):
    dict_list = []
    for dic, num in dict.items():
        single_dict = {dic: num}
        dict_list.append(single_dict)
    dict_list.sort(key=sorting_help, reverse=True)
    return dict_list

def sorting_help(dict):
    return list(dict.values())[0]