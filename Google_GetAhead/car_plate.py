def load_vocab(path):
    with open(path, "rt") as fd:
        return set(fd.readlines())
all_words = load_vocab("/usr/share/dict/american-english-huge")

import collections

def extract_letter(plate):
  """Returns a list with all the alphabet characters in a plate."""
  return [char for char in plate if char.isalpha()]

def is_valid(word, plate_letters):
    """Determines whether `word` could be a match for a given license plate."""
    word_count = collections.Counter(word)
    letters_count = collections.Counter(plate_letters)
    for letter in letters_count:
        if not word_count[letter] >= letters_count[letter]:
            
    return False


def shortest_word_finder(plate):
    words = collections.defaultdict(plate)
    plate_letters = extract_letter(plate)

    for w in all_words:
        if not is_valid(w, plate_letters):
            continue
        for letter in w:
            words[letter.lower()].add(w.lower())

