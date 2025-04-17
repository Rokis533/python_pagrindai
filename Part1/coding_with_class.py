# Kortos nuo 9 iki A (24 kortos)
# 2 žaidejai
# 6 kortos kiekvienam
# kozeriai 
# daugiausiai 6 kortos išmestos
# jei žaidejas neturi kaip apsiginti - privalo imti kortas
# jei žaidejas raundo pradžioje neturi 6 kortų - privalo traukti iš kaladės
# laimi tas kuris pirmas atsikratė visų kortų (jei kaladė tuščia)
# žaidejas ginasi didesnia to pačio tipo korta arba kozeriu, jei kozeris turi buti didesnis
# kai apsigina pradedantysis pasikeičia
# puolantis deda pasirnkta korta (kolkas nera dametimo)


# 9, 10, J, Q, K, A
# clubs (♣), diamonds (♦), hearts (♥) and spades (♠).
import sys
import random

deck_sample = {
    "♣" : ["9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"],
    "♦" : ["9♦", "10♦", "J♦", "Q♦", "K♦", "A♦"],
    "♥" : ["9♥", "10♥", "J♥", "Q♥", "K♥", "A♥"],
    "♠" : ["9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
}

player1_deck = []
player2_deck = []
trump_card = None # kozeris
trump_symbol = None # kozerio simbolis

game_deck = []

dict_cards_list = list(deck_sample.values())

game_deck.extend(dict_cards_list[0])
game_deck.extend(dict_cards_list[1])
game_deck.extend(dict_cards_list[2])
game_deck.extend(dict_cards_list[3])


random.shuffle(game_deck)
print(game_deck)
print()
# išdalinam kortas žaidejams
for _ in range(6):
    player1_deck.append(game_deck.pop())
    player2_deck.append(game_deck.pop())

trump_card = game_deck[0] # isissaugo kozeri bet jo iš kalades nepašalinam
trump_symbol = trump_card[-1] # isissaugo kozerio simboli

print("deck", game_deck)
print("player1", player1_deck)
print("player2", player2_deck)
print("trump_card", trump_card)
print("trump_symbol", trump_symbol)

# surandom kas iš žaideju turi mažiausia kozeri
player_1_index_of_trump = sys.maxsize
player_2_index_of_trump = sys.maxsize



for player1_card in player1_deck:
    try:
        dict_trump_list = deck_sample[trump_symbol]
        player_1_index_of_trump_temp = dict_trump_list.index(player1_card)
        if player_1_index_of_trump_temp < player_1_index_of_trump:
            player_1_index_of_trump = player_1_index_of_trump_temp
    except ValueError:
        pass

for player2_card in player2_deck:
    try:
        dict_trump_list = deck_sample[trump_symbol]
        player_2_index_of_trump_temp = dict_trump_list.index(player2_card)
        if player_2_index_of_trump_temp < player_2_index_of_trump:
            player_2_index_of_trump = player_2_index_of_trump_temp
    except ValueError:
        pass

print("player_1_index_of_trump", player_1_index_of_trump)
print("player_2_index_of_trump", player_2_index_of_trump)

if player_1_index_of_trump < player_2_index_of_trump:
    print("player1 starts")
else:
    print("player2 starts")










