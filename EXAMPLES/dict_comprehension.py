#!/usr/bin/env python
import os

animals = ['OWL', 'Badger', 'bushbaby', 'Tiger', 'Wombat', 'GORILLA', 'AARDVARK']

# {KEY: VALUE for VAR ... in ITERABLE if CONDITION}
d = {a.lower(): len(a) for a in animals}  # <1>

print(d, '\n')

# words = ['unicorn', 'stigmata', 'barley', 'bookkeeper']
#
# d = {w:{c:w.count(c) for c in sorted(w)} for w in words} # <2>
#
# for word, word_signature in d.items():
#     print(word, word_signature)

# for file_name in os.listdir('../DATA'):
#     file_path = os.path.join('../DATA/', file_name)
#     file_size = os.path.getsize(file_path)

fruits = ["pomegranate", "cherry", "apricot", "Apple",  "GUAVA", 'Peach', 'DATE',
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon", "LEMON", "Lemon", "lemon"
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

#                 item     for var in iterable
unique_fruits = {f.lower() for f in fruits}
print("unique_fruits: {}".format(unique_fruits))
