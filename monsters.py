"""Program for Aariel
    gives you a random name of a monster hunter monster
"""

from random import randint
def main():
    print("Generates a random monster name from Monster Hunter Series")
    monster_names = []
    with open("Monsters.txt", 'r') as txt:
        total = 0
        for line in txt:
            monster = line
            monster = monster.strip()
            monster_names.append(monster)
            total += 1
#     while True:
        index = randint(0, total)
        print("Monster Name : " + monster_names[index])
#         more = input('Get another monster name? (Y/N): ')
#         more = more.upper()
#         if more == 'N':
#             exit()
#         else:
#             continue

if __name__ == "__main__":
    main()
