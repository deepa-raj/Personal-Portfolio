word_list = [
'abruptly',
'absurd',
'abyss',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphaza',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'vodka',
'voodoo',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
]


import random
from random import shuffle


morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


score = 0
end = False

while not end:
    get_word = input("Hit 'y' to play the game: ").lower()
    if get_word == "y":
        choice = random.choice(word_list)
        random_word = choice
        # print(f"Word without shuffle: {random_word}")
        list_word = list(random_word)
        shuffle(list_word)
        print(f"shuffled word: {' '.join(list_word)}")
        print(f"Hint: Word starts with '{random_word[0]}' and ends with '{random_word[-1]}'.")
        find_word = input("Let's check your word matches with Morse code: ")

        text = find_word.upper()
        output = ', '.join(morse_code_dict[letter] for letter in text if letter in morse_code_dict)
        if find_word == random_word:
            print(f"Yes, your word and morse code matches perfectly \nHere's your Code: {output}\n")
            score += 1
            print(f"Well done, your score: {score}")
        else:
            print(f"Pffff, No it doesn't match with Morse code, \nHere's the correct Word & Code: {random_word} - {output}\n")
            print(f"Its alright, your score's still: {score}")
          

      
