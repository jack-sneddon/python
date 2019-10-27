import json

us_state_capitals = '../files/us_state_capitals.json'

with open(us_state_capitals) as f:
    state_capitals = json.load(f)

# format different ways

print(f"---- State Capitals (indend of 4)\n {json.dumps(state_capitals, indent=4)}")

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
print(encoded_hand)
decoded_hand = json.loads(encoded_hand)
print(decoded_hand)

print(blackjack_hand == decoded_hand)
print(type(encoded_hand))
print(type(decoded_hand))

blackjack_hand == tuple(decoded_hand)
print(blackjack_hand)









