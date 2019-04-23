from pprint import pformat


class SuffixKeywordTree:
    def __init__(self, s):
        """
        Init a suffix keyword tree

        :param s: text or a sequence, should be a string without '$'
        """
        self.s = s
        self.root = {}
        for i in range(len(s)):
            self.__add_kwd(s[i:], i)

    def __repr__(self):
        """
        Pretty print the suffix tree

        :return: None
        """
        return pformat(self.root)

    def __add_kwd(self, kwd, i):
        """
        Private function with constructor,
        to construct an suffix key word tree from a keyword

        :param kwd: string, keyword
        :param i: index instructor
        :return: None
        """
        cur = self.root
        for ch in kwd:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur[str(i)] = {}

    def search_kwd(self, kwd):
        """
        Search API of suffix keyword tree.

        :param kwd: the pattern to search, it should be a short string
        :return: sorted list of indexes such as [1, 3, 19], if no such keyword, return [-1]
        """
        if not kwd:
            return [-1]
        cur = self.root
        for ch in kwd:
            if ch in cur:
                cur = cur[ch]
            else:
                return [-1]
        res = []
        self.__dfs(cur, res)
        res.sort()
        return res

    def __dfs(self, root, res):
        """
        DFS algorithm to search all indexes of occurrences of the searching pattern

        :param root: tree root, should be a dict
        :param res: global return, to record all indexes
        :return:
        """
        for k, v in root.items():
            if k.isdigit():
                res.append(int(k))
            else:
                self.__dfs(v, res)


if __name__ == '__main__':
    s = 'ATTTATCGGGCGGCGAGAGAGAGCGT'
    kwds = [
        'ATTA',
        'GGG',
        'T',
        'GCGAG',
        'GA',
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    ]
    skt = SuffixKeywordTree(s)  # init a suffix keyword tree with a sequence/text
    print(s)
    print(skt)  # pretty print your suffix keyword tree

    # some tests of searching patterns
    for kwd in kwds:
        res = skt.search_kwd(kwd)
        print(kwd)
        print(res)
