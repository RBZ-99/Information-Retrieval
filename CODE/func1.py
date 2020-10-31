from nltk.tokenize import word_tokenize
import sys
#tokenize words in the docs
print(sys.argv[1])
filename = sys.argv[1]
fileopen = open(filename, 'r')
source = fileopen.read()
source = source.decode('utf-8')
tokens_list = word_tokenize(source)




# make a vector of each document with the count of the terms
n = no_of_docs
doc_vec_list = [dict() for x in range(n)]
for doc in documents:
	for word in doc:
		if(doc_vec_list[doc].has_key(word)):
			doc_vec_list[doc][word] += 1
		else
			doc_vec_list[doc][word] = 1





# Inverted index containing document-wise frequency
inverted_index = {}

for doc in documents:
    for word in doc:
        if inverted_index.has_key(word):
            posting_list = inverted_index[word]
            if posting_list.has_key(doc):
                posting_list[doc] = posting_list[doc] + 1
            else:
                posting_list[doc] = 1
        else:
            inverted_index[word] = {doc:1}



# maximum term frequency for every document
max_frequency = {}
for doc in documents:
    max_frequency[doc] = 0

for posting_list in inverted_index.values():
    for doc in posting_list.keys():
        max_frequency[doc] = max(max_frequency[doc], posting_list[doc])




# QUERY

#populating query dictionary with counts
Q = {}
for word in query:
	if Q.has_key(word):
		Q[word] += 1
	else:
		Q[word] = 1



