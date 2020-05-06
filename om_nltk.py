# Perform nlp on OPRAmachine request titles and plot word frequencies

import pandas as pd
import requests
import html2text
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import seaborn as sns

# Obtain all state URLs from the COVID Tracking Project
opra_data = pd.read_csv("https://github.com/gavinrozzi/opra-data/raw/master/opramachine_requests.csv")

# Get just the titles for all records
request_titles = opra_data['title']

# Break the page up into sentences so it can be properly tokenized
tokens = opra_data.apply(lambda row: nltk.word_tokenize(str(row['sentences'])), axis=1)

# Define stopwords
sw = nltk.corpus.stopwords.words('english')

# Extra words

extra_words = ['for', 'to', 'of', 'the', '.']

for item in extra_words:
    sw.append(item)

# Remove stopwords. These are not needed.
words = [word for word in tokens if word not in sw]

# Unpack the lists of lists so it will work with freqdist
flat_list = []
for sublist in words:
    for item in sublist:
        flat_list.append(item)

# Create a frequency distribution of the words
freqdist = nltk.FreqDist(flat_list)

# Plot the first 25 words
freqdist.plot(25)

# save figure
plt.savefig('plot.png')
