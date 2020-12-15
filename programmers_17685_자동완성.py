def solution(words):
    char_list = [chr(char_index) for char_index in range(97, 122)]
    cursor = 0

    common_word_count = 0

    target_word = ''

    for word in words:
        target_word = word
        if target_word[cursor] in word:
            common_word_count += 1
        cursor += 1

    print(target_word, common_word_count)

    answer = 0
    return answer


print(solution(["go", "gone", "guild"]))
# print(solution(["abc", "def", "ghi", "jklm"]))
# print(solution(["word", "war", "warrior", "world"]))
