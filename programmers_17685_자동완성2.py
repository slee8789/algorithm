class Node:
    def __init__(self, key):
        self.key = key
        # self.single_child = True
        self.possible_word_count = 0
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur.child:
                cur.possible_word_count += 1
                cur.child[ch] = Node(ch)

            cur = cur.child[ch]
        cur.child['*'] = True

    def search(self, word):
        cur = self.head
        result = 0
        for ch in word:
            if '*' not in cur.child and cur.possible_word_count == 1 and cur.key is not None:
                result = word.index(ch) + 1

            if ch not in cur.child:
                return False

            cur = cur.child[ch]

        if '*' in cur.child:
            print(result)
            return len(word)


def solution(words):
    trie = Trie()
    answer = 0
    for word in words:
        trie.insert(word)

    for word in words:
        trie.search(word)
        # print(trie.search(word))
    return answer


# print(solution(["go", "gone", "guild"]))
# print(solution(["abc", "def", "ghi", "jklm"]))
# print(solution(["word", "war", "warrior", "world"]))
# print(solution(["word", "world"]))
solution(["word", "world"])

