import sys
import random

# Initialize deck
deck_sample = {
    "♣" : ["9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"],
    "♦" : ["9♦", "10♦", "J♦", "Q♦", "K♦", "A♦"],
    "♥" : ["9♥", "10♥", "J♥", "Q♥", "K♥", "A♥"],
    "♠" : ["9♠", "10♠", "J♠", "Q♠", "K♠", "A♠"]
}

player1_deck = []
player2_deck = []
trump_card = None  # kozeris
trump_symbol = None  # kozerio simbolis
game_deck = []

# Convert dictionary to list
dict_cards_list = list(deck_sample.values())

# Add all cards to the game deck
game_deck.extend(dict_cards_list[0])
game_deck.extend(dict_cards_list[1])
game_deck.extend(dict_cards_list[2])
game_deck.extend(dict_cards_list[3])

# Shuffle the deck
random.shuffle(game_deck)
print("Initial shuffled deck:", game_deck)
print()

# Deal cards to players
for _ in range(6):
    player1_deck.append(game_deck.pop())
    player2_deck.append(game_deck.pop())

# Set trump card and symbol
trump_card = game_deck[0]  # Save trump card but don't remove from deck
trump_symbol = trump_card[-1]  # Get trump symbol

print("Deck:", game_deck)
print("Player 1:", player1_deck)
print("Player 2:", player2_deck)
print("Trump card:", trump_card)
print("Trump symbol:", trump_symbol)

# Find who has the lowest trump card
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

print("Player 1 lowest trump index:", player_1_index_of_trump)
print("Player 2 lowest trump index:", player_2_index_of_trump)

# Determine who starts
if player_1_index_of_trump < player_2_index_of_trump:
    current_attacker = 1
    current_defender = 2
    print("Player 1 starts")
else:
    current_attacker = 2
    current_defender = 1
    print("Player 2 starts")

# Helper function to get card rank for comparison
def get_card_rank(card):
    rank_map = {"9": 0, "10": 1, "J": 2, "Q": 3, "K": 4, "A": 5}
    if card[0:2] == "10":
        return rank_map["10"]
    return rank_map[card[0]]

# Game loop
game_over = False
discarded_pile = []

while not game_over:
    print("\n" + "=" * 50)
    
    # Make sure players have cards if deck isn't empty
    if len(game_deck) > 0:
        while len(player1_deck) < 6 and len(game_deck) > 0:
            player1_deck.append(game_deck.pop())
        while len(player2_deck) < 6 and len(game_deck) > 0:
            player2_deck.append(game_deck.pop())
    
    # Check win condition
    if len(player1_deck) == 0 and len(game_deck) == 0:
        print("Player 1 wins!")
        game_over = True
        break
    
    if len(player2_deck) == 0 and len(game_deck) == 0:
        print("Player 2 wins!")
        game_over = True
        break
    
    print(f"Deck: {len(game_deck)} cards")
    print(f"Player 1: {player1_deck}")
    print(f"Player 2: {player2_deck}")
    print(f"Trump card: {trump_card} (Symbol: {trump_symbol})")
    print(f"Player {current_attacker} is attacking, Player {current_defender} is defending")
    
    # Current round cards
    table_cards = []
    round_over = False
    defense_successful = True
    
    # Play up to 6 cards in a round
    while len(table_cards) < 12 and not round_over:  # 12 cards max (6 attacks + 6 defenses)
        # Attacker's turn
        if current_attacker == 1:
            attacker_deck = player1_deck
        else:
            attacker_deck = player2_deck
            
        if len(table_cards) == 0:  # First attack of the round
            print(f"\nPlayer {current_attacker}'s turn to attack:")
            if len(attacker_deck) == 0:
                print(f"Player {current_attacker} has no cards left!")
                round_over = True
                continue
                
            # Print cards with indices for selection
            for i, card in enumerate(attacker_deck):
                print(f"{i}: {card}")
                
            valid_choice = False
            while not valid_choice:
                try:
                    card_index = int(input(f"Player {current_attacker}, choose a card to attack: "))
                    if 0 <= card_index < len(attacker_deck):
                        attack_card = attacker_deck.pop(card_index)
                        table_cards.append(attack_card)
                        print(f"Player {current_attacker} attacks with {attack_card}")
                        valid_choice = True
                    else:
                        print("Invalid card index.")
                except ValueError:
                    print("Please enter a valid number.")
        else:  # Subsequent attacks in the same round
            # Check if attacker can add more cards
            if len(attacker_deck) == 0:
                print(f"Player {current_attacker} has no more cards to attack with.")
                round_over = True
                continue
                
            # Get ranks of cards already on the table
            valid_ranks = set()
            for card in table_cards:
                if card[0:2] == "10":
                    valid_ranks.add("10")
                else:
                    valid_ranks.add(card[0])
            
            # Check if attacker has valid cards to play
            valid_attack_cards = []
            for i, card in enumerate(attacker_deck):
                card_rank = card[0:2] if card[0:2] == "10" else card[0]
                if card_rank in valid_ranks:
                    valid_attack_cards.append((i, card))
            
            if not valid_attack_cards:
                print(f"Player {current_attacker} has no valid cards to continue attacking.")
                round_over = True
                continue
                
            print(f"\nPlayer {current_attacker}, you can play these cards:")
            for idx, (i, card) in enumerate(valid_attack_cards):
                print(f"{idx}: {card} (position {i} in hand)")
                
            play_more = input(f"Player {current_attacker}, do you want to attack more? (y/n): ").lower()
            if play_more != 'y':
                round_over = True
                continue
                
            valid_choice = False
            while not valid_choice:
                try:
                    choice_index = int(input(f"Choose card (0-{len(valid_attack_cards)-1}): "))
                    if 0 <= choice_index < len(valid_attack_cards):
                        card_idx, attack_card = valid_attack_cards[choice_index]
                        attack_card = attacker_deck.pop(card_idx)
                        table_cards.append(attack_card)
                        print(f"Player {current_attacker} attacks with {attack_card}")
                        valid_choice = True
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a valid number.")
        
        # Defender's turn
        if current_defender == 1:
            defender_deck = player1_deck
        else:
            defender_deck = player2_deck
            
        print(f"\nPlayer {current_defender}'s turn to defend against {table_cards[-1]}:")
        
        # Check if defender has valid cards
        attack_card = table_cards[-1]
        attack_suit = attack_card[-1]
        attack_rank = get_card_rank(attack_card)
        
        valid_defense_cards = []
        
        for i, card in enumerate(defender_deck):
            card_suit = card[-1]
            card_rank = get_card_rank(card)
            
            # Same suit with higher rank
            if card_suit == attack_suit and card_rank > attack_rank:
                valid_defense_cards.append((i, card))
            # Trump card against non-trump
            elif card_suit == trump_symbol and attack_suit != trump_symbol:
                valid_defense_cards.append((i, card))
            # Trump vs Trump with higher rank
            elif card_suit == trump_symbol and attack_suit == trump_symbol and card_rank > attack_rank:
                valid_defense_cards.append((i, card))
        
        if not valid_defense_cards:
            print(f"Player {current_defender} has no valid cards to defend!")
            print(f"Player {current_defender} takes all cards from the table.")
            defender_deck.extend(table_cards)
            table_cards = []
            round_over = True
            defense_successful = False
            continue
            
        # Show valid defense cards
        print(f"Player {current_defender}, you can defend with these cards:")
        for idx, (i, card) in enumerate(valid_defense_cards):
            print(f"{idx}: {card} (position {i} in hand)")
            
        take_cards = input(f"Player {current_defender}, do you want to take the cards instead? (y/n): ").lower()
        if take_cards == 'y':
            print(f"Player {current_defender} takes all cards from the table.")
            defender_deck.extend(table_cards)
            table_cards = []
            round_over = True
            defense_successful = False
            continue
            
        valid_choice = False
        while not valid_choice:
            try:
                choice_index = int(input(f"Choose defense card (0-{len(valid_defense_cards)-1}): "))
                if 0 <= choice_index < len(valid_defense_cards):
                    card_idx, defense_card = valid_defense_cards[choice_index]
                    defender_deck.pop(card_idx)
                    table_cards.append(defense_card)
                    print(f"Player {current_defender} defends with {defense_card}")
                    valid_choice = True
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
                
    # Round ended
    if defense_successful:
        print("\nDefense successful! All cards are discarded.")
        discarded_pile.extend(table_cards)
        # Swap roles
        current_attacker, current_defender = current_defender, current_attacker
    else:
        print("\nDefense failed! The defender takes the cards.")
        # Attacker stays the same
    
    # Check if game is over
    if len(player1_deck) == 0 and len(game_deck) == 0:
        print("\nPlayer 1 wins!")
        game_over = True
    
    if len(player2_deck) == 0 and len(game_deck) == 0:
        print("\nPlayer 2 wins!")
        game_over = True

print("\nGame over!")