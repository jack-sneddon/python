# print the first 10 cubes 1^3, 2^3, ...
print("\n=====slices=====")
players = ['federer', 'djokovic', 'murray', 'nadal', 'williams']
print(players)

# kind of like the range function
print(players[0:3])
print(players[1:4])
print(players[:2])

# work from back
print(players[-3])
print(players[-3:])

# skip items in the slice
print(players[1:4:2])

# for loop
print("\nthe top players are:")
for player in players[:3]:
    print(player.title())




