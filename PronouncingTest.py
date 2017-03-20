import string

import pronouncing

print(pronouncing.rhymes("moon"))
print(pronouncing.rhymes("orange"))
translator = str.maketrans('', '', string.punctuation)

print("lame!".translate(translator) in pronouncing.rhymes("tame"));

print("dog!".translate(translator))
print("geese" in pronouncing.rhymes("cheese"));
