import random

NOUN_PLACEHOLDER = 'XXXNOUNXXX'
ADJECTIVE_PLACEHOLDER = 'XXXADJXXX'
VERB_PLACEHOLDER = 'XXXVERBXXX'
ADVERB_PLACEHOLDER = 'XXXADVXXX'
EXCLAMATION_PLACEHOLDER = 'XXXEXCLXXX'
PLACE_PLACEHOLDER = 'XXXPLACEXXX'
PERSON_PLACEHOLDER = 'XXXPERSXXX'

story = 'Yesterday, I went to XXXPLACEXXX to buy a XXXNOUNXXX. But on my way, I ran into a XXXADJXXX XXXNOUNXXX. I was very XXXADJXXX. Then I remembered that I had a XXXNOUNXXX in my pocket. I pulled it out, XXXVERBXXX it XXXADVXXX, said, "XXXEXCLXXX! Look over there, it\'s XXXPERSXXX!" and XXXADVXXX XXXVERBXXX behind a XXXADJXXX XXXNOUNXXX.'

# Perform substitutions
nouns = open('nouns.txt').read().splitlines()
while NOUN_PLACEHOLDER in story:
    newWord = random.choice(nouns)
    story = story.replace(NOUN_PLACEHOLDER, newWord, 1)

adjectives = open('adjectives.txt').read().splitlines()
while ADJECTIVE_PLACEHOLDER in story:
    newWord = newWord = random.choice(adjectives)
    story = story.replace(ADJECTIVE_PLACEHOLDER, newWord, 1)

verbs = open('verbs.txt').read().splitlines()
while VERB_PLACEHOLDER in story:
    newWord = newWord = random.choice(verbs)
    story = story.replace(VERB_PLACEHOLDER, newWord, 1)

adverbs = open('adverbs.txt').read().splitlines()
while ADVERB_PLACEHOLDER in story:
    newWord = newWord = random.choice(adverbs)
    story = story.replace(ADVERB_PLACEHOLDER, newWord, 1)

exclamations = open('exclamations.txt').read().splitlines()
while EXCLAMATION_PLACEHOLDER in story:
    newWord = newWord = random.choice(exclamations)
    story = story.replace(EXCLAMATION_PLACEHOLDER, newWord, 1)

places = open('places.txt').read().splitlines()
while PLACE_PLACEHOLDER in story:
    newWord = newWord = random.choice(places)
    story = story.replace(PLACE_PLACEHOLDER, newWord, 1)

persons = open('persons.txt').read().splitlines()
while PERSON_PLACEHOLDER in story:
    newWord = newWord = random.choice(persons)
    story = story.replace(PERSON_PLACEHOLDER, newWord, 1)

# Output story with substitutions
print(story)
