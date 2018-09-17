import random

NOUN_PLACEHOLDER = 'XXXNOUNXXX'
ADJECTIVE_PLACEHOLDER = 'XXXADJXXX'
VERB_PLACEHOLDER = 'XXXVERBXXX'
ADVERB_PLACEHOLDER = 'XXXADVXXX'
EXCLAMATION_PLACEHOLDER = 'XXXEXCLXXX'
PLACE_PLACEHOLDER = 'XXXPLACEXXX'
PERSON_PLACEHOLDER = 'XXXPERSXXX'

story = 'Yesterday, I went to XXXPLACEXXX to buy a XXXNOUNXXX. But on my way, I ran into a XXXADJXXX XXXNOUNXXX. I was very XXXADJXXX. Then I remembered that I had a XXXNOUNXXX in my pocket. I pulled it out, XXXVERBXXX it XXXADVXXX, said, "XXXEXCLXXX! Look over there, it\'s XXXPERSXXX!" and XXXADVXXX XXXVERBXXX behind a XXXADJXXX XXXNOUNXXX.'        

def fillin(text, placeholder, word_file):
    words = open(word_file).read().splitlines()
    while placeholder in text:
        new_word = random.choice(words)
        text = text.replace(placeholder, new_word, 1)
    return text

# Perform substitutions
story = fillin(story, NOUN_PLACEHOLDER, 'nouns.txt')
story = fillin(story, ADJECTIVE_PLACEHOLDER, 'adjectives.txt')
story = fillin(story, VERB_PLACEHOLDER, 'verbs.txt')
story = fillin(story, ADVERB_PLACEHOLDER, 'adverbs.txt')
story = fillin(story, EXCLAMATION_PLACEHOLDER, 'exclamations.txt')
story = fillin(story, PLACE_PLACEHOLDER, 'places.txt')
story = fillin(story, PERSON_PLACEHOLDER, 'persons.txt')

# Output story with substitutions
print(story)
