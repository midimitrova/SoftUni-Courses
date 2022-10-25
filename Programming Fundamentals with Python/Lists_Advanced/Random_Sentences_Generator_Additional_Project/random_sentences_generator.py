import random


def get_random_world(words):
    return random.choice(words)


names = ['Mariya', 'Dilyan', 'Georgi', 'Staniela']
places = ['Sofia', 'Haskovo', 'Burgas', 'Plovdiv']
verbs = ['eats', 'holds', 'sees', 'plays with', 'brings']
nouns = ['cake', 'stones', 'apple', 'laptop', 'bikes']
adverbs = ['slowly', 'diligently', 'warmly', 'sadly', 'rapidly']

print('Hello, this is your first random sentence.')
while True:
    random_name = get_random_world(names)
    random_places = get_random_world(places)
    random_verbs = get_random_world(verbs)
    random_nouns = get_random_world(nouns)
    random_adverbs = get_random_world(adverbs)

    print(f'{random_name} from {random_places} {random_adverbs} {random_verbs} {random_nouns}')
    input('Click [Enter] to generate a new one.')
