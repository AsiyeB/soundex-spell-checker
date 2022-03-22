# compute soundex code of all terms in a csv file
import csv
import re
from soundex import soundex

invalid = re.compile("^[a-zA-Z0-9_#$@&!*\u06F0-\u06F9]*$")
# instead of all_words we can use any other dictionary to compute the soundex code of it words like out1.csv in symspellpy folder
# instead of soundex_all_words.csv we can use testdict.csv
with open('soundex_all_words.csv','w',encoding='utf-8',newline='') as f1:
    with open('all_words.csv',encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            writer=csv.writer(f1)
            for row in csv_reader:
                if not invalid.search(row[0]):
                    writer.writerow([row[0], soundex(row[0])])