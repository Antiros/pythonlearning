def single_root_words(root_word, *other_word):
    root_word_lower = root_word.lower()
    def is_related(word):
        return root_word_lower in word.lower() or word.lower() in root_word_lower
    return list(filter(is_related, other_word))
result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result_1)
print(result_2)





# def single_root_words(root_word, *other_word):
#     same_list = []
#     root_word_lower = root_word.lower()
#     for word in other_word:
#         if root_word_lower in word.lower() or word.lower() in root_word_lower:
#             same_list.append(word)
#     return  same_list
# result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result_1)
# print(result_2)



# def is_related(root_word, word):
#     return root_word.lower() in word.lower() or word.lower() in root_word.lower()
# def single_root_words(root_word, *other_word):
#     return list(filter(lambda word: is_related(root_word, word), other_word))
# result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result_1)
# print(result_2)



# def single_root_words(root_word, *other_word):
#     root_word_lower = root_word.lower()
#     return list(filter(lambda word: root_word_lower in word.lower() or word.lower() in root_word_lower, other_word))
# result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
# result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result_1)
# print(result_2)