def words_sorting(*args):
    words_value = {}
    for word in args:
        words_value[word] = sum([ord(ch) for ch in word])

    total_sum = 0
    for value in words_value.values():
        total_sum += value

    if total_sum % 2 == 0:
        sorted_words = sorted(words_value.items(), key=lambda x: x[0])
    elif total_sum % 2 == 1:
        sorted_words = sorted(words_value.items(), key=lambda x: -x[1])

    result = ''
    for word, value in sorted_words:
        result += f"{word} - {value}\n"
    return result


# --- TEST CODE ---
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))
#
#
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))
#
#
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))
