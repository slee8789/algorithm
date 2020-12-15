class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.head = Node(None)

    def insert(self, number):
        current = self.head

        for char in number:
            if char not in current.child:
                current.child[char] = Node(char)

            if current.is_end:
                return True

            current = current.child[char]

        current.is_end = True
        return False


def solution(phone_book):
    trie = Trie()
    answer = True
    for phone in sorted(phone_book):
        if trie.insert(phone):
            answer = False
            break

    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
