import nltk
sentence = """Of waking life. to him before me..
And who is forsaken.
And fill my heart be broken..
Through my fingers to the church-yard bore me..
"""
tokens = nltk.word_tokenize(sentence)
tokens
['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
'Arthur', 'did', "n't", 'feel', 'very', 'good', '.']
tagged = nltk.pos_tag(tokens)
tagged[0:6]
[('At', 'IN'), ('eight', 'CD'), ("o'clock", 'JJ'), ('on', 'IN'),
('Thursday', 'NNP'), ('morning', 'NN')]
entities = nltk.chunk.ne_chunk(tagged)
print(entities)