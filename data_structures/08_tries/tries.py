class TrieNode:
    def __init__(self):
        self.children = [0] * 26
        self.leaf = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, ch):
        return ord('a') - ord(ch)

    def insert_string(self, insert_string):
        buf_root = self.root

        for char in insert_string:
            index = self.get_index(char)
            if buf_root.children[index]:
                buf_root = buf_root.children[index]

            else:
                buf_root.children[index] = TrieNode()
                buf_root = buf_root.children[index]

        buf_root.leaf = True

    def search_string(self, search_string):
        buf_root = self.root

        for char in search_string:
            index = self.get_index(char)
            if not buf_root.children[index]:
                return False
            buf_root = buf_root.children[index]

        return buf_root.leaf


if __name__ == "__main__":
    trie = Trie()
    insert_string = ['hello', 'the', 'robbin', 'disco', 'disqualified', 'damaged', 'dam', 'damote']
    search_string = ['hello', 'the', 'try', 'copy', 'robbi', 'robbin', 'damaged']

    for strings in insert_string:
        trie.insert_string(strings)

    for s_string in search_string:
        print("Searching for string {} in trie, and it was {}".format(s_string, trie.search_string(s_string)))
