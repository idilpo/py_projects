letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
           "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {k:v for k,v in zip(letters,points)}
print(letter_to_points)

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letter_to_points.keys():
      point_total += letter_to_points[letter]
    else: point_total += 0
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)


player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi on":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for w in words:
    player_points += score_word(w)
  player_to_points[player] = player_points
print(player_to_points)



def players_words(p, word):
    for p in player_to_words.keys():
        w_list = player_to_words[p]
        w_list.append(word)
    return p,w_list
players_words("player1", "PINK")
print(player_to_words)



"""
* play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
update_point_totals() — turn your nested loops into a function that you can call any time a word is played
make your letter_to_points dictionary able to handle lowercase inputs as well
"""