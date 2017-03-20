import string

import markovify
import pronouncing

# Get raw text as string.
with open("poem.txt") as f:
    text = f.read()
translator = str.maketrans('', '', string.punctuation)

# Build the model.
text_model = markovify.Text(text, state_size=2)

# # Print three randomly-generated sentences of no more than 140 characters
# for i in range(2):
print(text_model.make_short_sentence(60))


def test(text):
        found = False
        iteration = 0
        while(not found):
            if iteration > 150:
                text = text_model.make_short_sentence(140)
                iteration = 0
            new = text_model.make_short_sentence(140)
            spit1 = text.split()
            spit2 = new.split()
            print(spit1)
            print(spit2)
            word2 = spit2[len(spit2) - 1].translate(translator)
            word1 = spit1[len(spit1) - 1].translate(translator)
            if ((word1 in pronouncing.rhymes(word2))):
                text = text + "\n" + new
                found = True
                return (text)
            iteration += 1

        return (text)




print(test(text_model.make_short_sentence(140)))
