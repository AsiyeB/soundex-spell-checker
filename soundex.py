"""
.. module:: soundex
   :synopsis: Module for soundex spelling correction algorithm.
"""

import re
import csv
"""
This module encodes a string using Soundex, as described by
http://en.wikipedia.org/w/index.php?title=Soundex&oldid=466065377
Only strings with the letters A-Z and of length >= 2 are supported.
"""

persian_alpha_codepoints = '\u0621-\u0629\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC'
invalid_re = re.compile("[ئءأإؤآاوحهعی\u064B-\u0651\u200c]|'^[\s'+persian_alpha_codepoints+']*$")
charsubs = {'ب': '1', 'ف': '1', 'پ': '1',
            'س': '2','ث': '2','ص': '2','ز': '2','ذ': '2','ض': '2','ظ': '2',
            'ک': '2','گ': '2','ق': '2', 'غ': '2', 'چ': '2',
            'ج': '2', 'خ': '2', 'ژ': '2', 'ش': '2',
            'د': '3','ط': '3', 'ت': '3', 'ل': '4', 'م': '5',
            'ن': '5', 'ر': '6','ة': '3'}
fa_en = {'ب': 'B', 'ف': 'F', 'پ': 'P',
            'س': 'S','ث': 'S','ص': 'S','ز': 'Z','ذ': 'Z','ض': 'Z','ظ': 'Z',
            'ک': 'K','گ': 'G','ق': 'G', 'غ': 'G', 'چ': 'C',
            'ج': 'J', 'خ': 'X', 'ژ': 'Z', 'ش': 'S',
            'د': 'D','ط': 'T', 'ت': 'T', 'ل': 'L', 'م': 'M',
            'ن': 'N', 'ر': 'R',
            'آ': 'A','ا': 'A','و': 'V','ح': 'H','ه': 'H','ع': 'A','ی': 'Y',
            'ئ': 'XX','ؤ': 'XX','إ': 'A', 'أ': 'A', 'ء': 'A'}
def normalize(s):
    """ Returns a copy of s without invalid chars and repeated letters. """
    #this function remove invalid chars

    first = fa_en[s[0]]
    s = re.sub(invalid_re, "", s[1:])
    # remove repeated chars
    char = None
    s_clean = first
    for c in s:
        if char != c:
            s_clean += c
        char = c
    
    return s_clean


def soundex(s):
    # this function calculate soundex 4 character code
    if len(s) < 2:
        return None

    s = normalize(s)
    last = None
    enc = s[0]
    for c in s[1:]:
        if len(enc) == 4:
            break

        if charsubs[c] != last:
            enc += charsubs[c]
        last = charsubs[c]

    while len(enc) < 4:
        enc += '0'

    return enc


def lookup(string):
    #this function return suggestion based on input:string
    csv_file = csv.reader(open('soundex/testdict.csv', "r",encoding='utf-8'), delimiter=",") 
    # instead of testdict.csv we can use another dictionary => soundex_all_words.csv
    suggestionList = []
    strCode = soundex(string)
    print(strCode)
    for row in csv_file:
        if row!=[]:
            if strCode == row[1]:
                suggestionList.append(row[0])
    
    for i in suggestionList:
        if i==string:
            return [string]
    return suggestionList
