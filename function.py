
def break_words(stuff):
    """ This funciton will break up words for us."""
    word = stuff.split(' ')
    return word

def sort_words(words):
    return sorted(words) 

def print_last_word(words):
    word = words.pop(-1)
    print  word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)


