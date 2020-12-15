class Node:
    def __init__(self, char, data=None):
        # 노드의 글자
        self.char = char
        # 마지막 노드일 때 string 값
        self.data = data
        # 해당 노드를 거쳐갈 경우 가능한 글자의 개수
        self.possible_word = 0
        # trie의 자식 노드들
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            # 노드의 가능한 글자 개수를 1 늘려준다.
            curr_node.possible_word += 1
            if char not in curr_node.children:
                # 해당 노드의 next에 문자열이 등록되어 있지 않으면 등록한다
                curr_node.children[char] = Node(char)
            # 다음 노드로 이동한다.
            curr_node = curr_node.children[char]

        # 마지막 글자. 마지막 글자의 possible_word도 1로 만들어준다.
        curr_node.possible_word += 1
        # 마지막 글자이므로, 해당 trie를 타고 왔을 때의 최종문자를 저장해둔다.
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for char in string:
            # 노드를 타고 내려간다.
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        # 해당 노드까지 왔을 때 만들 수 있는 문자의 개수가 1이면 True 반환
        if curr_node.possible_word == 1:
            return True
        else:
            return False

def solution(words):
    cnt = 0
    word_trie = Trie()
    for word in words:
        word_trie.insert(word)

    print(word_trie.head)

    for word in words:
        # 단어 끝까지 돌았는데
        # possible_word가 1이 아닌 경우를 확인하는 변수
        already_find = False

        for i in range(1, len(word) + 1):
            if word_trie.search(word[:i]):
                cnt += len(word[:i])
                already_find = True
                break
        if not already_find:
            cnt += len(word)
    return cnt

# print(solution(["go", "gone", "guild"]))
# print(solution(["abc", "def", "ghi", "jklm"]))
# print(solution(["word", "war", "warrior", "world"]))
# print(solution(["word", "world"]))
# solution(["word", "world"])