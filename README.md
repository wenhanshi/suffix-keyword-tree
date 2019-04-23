# suffix-keyword-tree
Toy code of a simple implementation of suffix keyword tree for CS466


# Examples

```python
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
print(skt)  # pretty print your suffix keyword tree

# some tests of searching patterns
for kwd in kwds:
    res = skt.search_kwd(kwd)
    print(kwd)
    print(res)
```


```
{'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'15': {}}}}}},
                                     'C': {'G': {'T': {'17': {}}}}}},
                         'C': {'G': {'T': {'19': {}}}}}},
             'C': {'G': {'T': {'21': {}}}}},
       'T': {'C': {'G': {'G': {'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'4': {}}}}}}}}}}}}}}}}}}}}},
             'T': {'T': {'A': {'T': {'C': {'G': {'G': {'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'0': {}}}}}}}}}}}}}}}}}}}}}}}}}}},
 'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'13': {}}}}}}}}}}}},
             'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'10': {}}}}}}}}}}}}}},
                   'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'6': {}}}}}}}}}}}}}}}}}}},
             'T': {'23': {}}}},
 'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'14': {}}}}}},
                                           'C': {'G': {'T': {'16': {}}}}}},
                               'C': {'G': {'T': {'18': {}}}}}},
                   'C': {'G': {'T': {'20': {}}}}}},
       'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'12': {}}}}}}}}}}}},
                   'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'9': {}}}}}}}}}}}}}}},
                   'T': {'22': {}}}},
       'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'11': {}}}}}}}}}}}},
                         'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'8': {}}}}}}}}}}}}}}}}},
             'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'7': {}}}}}}}}}}}}}}}}}}},
       'T': {'24': {}}},
 'T': {'25': {},
       'A': {'T': {'C': {'G': {'G': {'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'3': {}}}}}}}}}}}}}}}}}}}}}}},
       'C': {'G': {'G': {'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'5': {}}}}}}}}}}}}}}}}}}}}},
       'T': {'A': {'T': {'C': {'G': {'G': {'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'2': {}}}}}}}}}}}}}}}}}}}}}}},
             'T': {'A': {'T': {'C': {'G': {'G': {'G': {'C': {'G': {'G': {'C': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'A': {'G': {'C': {'G': {'T': {'1': {}}}}}}}}}}}}}}}}}}}}}}}}}}}
```

```
ATTA
[-1]
GGG
[7]
T
[1, 2, 3, 5, 25]
GCGAG
[12]
GA
[14, 16, 18, 20]
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
[-1]
```
