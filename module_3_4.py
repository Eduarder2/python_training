def single_root_words(root_word, *other_words):
    same_words = list()
    root_word = root_word.lower()
    for word in other_words:
        word_l = word.lower()
        if (root_word in word_l) or (word_l in root_word):
            same_words.append(word)
    return same_words

print(single_root_words('raT', 'Crat', 'ipRit', 'at', 'MaKarAT', 'rOt'))