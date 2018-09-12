import random

NOUN_PLACEHOLDER = 'XXXNOUNXXX'
ADJECTIVE_PLACEHOLDER = 'XXXADJXXX'

story = 'Yesterday, I went to the store to buy a XXXNOUNXXX. But on my way, I ran into a XXXADJXXX XXXNOUNXXX. I was very XXXADJXXX. Then I remembered that I had a XXXNOUNXXX in my pocket. I pulled it out, threw it up in the air, and quickly hid behind a XXXADJXXX XXXNOUNXXX.'

# Import word lists
nouns = open('nouns.txt').read().splitlines()
adjectives = open('adjectives.txt').read().splitlines()

# Perform substitutions
while NOUN_PLACEHOLDER in story:
    newWord = random.choice(nouns)
    story = story.replace(NOUN_PLACEHOLDER, newWord, 1)
while ADJECTIVE_PLACEHOLDER in story:
    newWord = random.choice(adjectives)
    story = story.replace(ADJECTIVE_PLACEHOLDER, newWord, 1)

# Output story with substitutions
print(story)
