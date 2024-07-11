import json
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

with open('parsed_data.json') as f:
    data = json.load(f)

counter = Counter()
# Additional stopwords because nltk does not have a curse word filter
# Reads from gitignored text file of bad words
with open('bad_words.txt', 'r') as f:
    bad_words = f.read().splitlines()
    
stopwords = set(stopwords.words('english')).union(set([bad_words[0]]))

for key, value in data.items():
    if isinstance(value, dict):
        for sub_key in value.keys():
            # Remove punctuation, convert to lower case, and split the key into words
            words = re.sub(r'[^\w\s]', '', sub_key.lower()).split()
            # Filter out stop words, numbers, and words that are 2 characters or less
            words = [word for word in words if word not in stopwords and not word.isdigit() and len(word) > 2]
            counter.update(words)

# Find most common words, >= 20
counter = Counter({word: count for word, count in counter.items() if count >= 20})

word_freq = f'Most Frequent Words:  {dict(counter.most_common())}'

with open('term_freq.json', 'w') as f:
    json.dump(word_freq, f, indent=4)
