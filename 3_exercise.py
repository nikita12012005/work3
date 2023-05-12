friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for friend, enemie in zip(friends, enemies):
    if friend== enemie:
        print(f'{friend} we are not friends anymore')
    elif friend!=enemie and friend!='James':
        print(f'{friend} we are the best friends')