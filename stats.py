def get_num_words(text):
    words = text.split()
    return len(words)
def get_char_counts(text):
    l_text = text.lower()
    char_list = {}
    for char in l_text:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list
