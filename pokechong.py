import random

class Human:

    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.meds = 3
        self.hp_ups = 0
        self.attack_ups = 0
        self.party = []
        self.errors = 0


class Pokechong:

    seenpokes = 0

    def __init__(self, name, difficulty):
        self.name = name
        x = random.randrange(3)
        if x == 0:
            self.type = "Grass"
        elif x == 1:
            self.type = "Fire"
        else:
            self.type = "Water"
        self.hp = 20 + random.randrange(difficulty, int(difficulty * 5 + 0.5))
        self.max_hp = int(self.hp)
        self.attack = 5 + random.randrange(difficulty, int(difficulty * 5 + 0.5))
        self.difficulty = difficulty
        self.level_up = 0
        self.level = 1
        self.shiny = random.randrange(100) == 0
        Pokechong.seenpokes += 1

def menu(human, mypoke):
    if human.coins >= 100:
        return victory()
    print(f"\nThe game will end once you collect 100 coins. You currently have: {human.coins}/100 coins.")
    print("What would you like to do?\n")
    comm = input("Would you like to view your 'Pokechong', 'heal' HP, visit the 'shop', or 'explore' more Pokechong? ")
    if comm.upper() == "POKECHONG":
        return pokemons(human, mypoke)
    elif comm.upper() == "HEAL":
        return menu_heal(human, mypoke)
    elif comm.upper() == "SHOP":
        return shop(human, mypoke)
    elif comm.upper() == "EXPLORE":
        return explore(human, mypoke)
    else:
        human.errors += 1
        if human.errors >= 10:
            return secret_ending1()
        print("Wow, you suck at typing! Please try again...")
        return menu(human, mypoke)

def pokemons(human, mypoke):
    print("\nPokechong Name: {}\nType: {}\nHP: {}/{}\nAttack: {}\nUntil Next LVL: {}\nShiny: {}\n".format(mypoke.name, mypoke.type, mypoke.hp, mypoke.max_hp, mypoke.attack, 100 - mypoke.level_up, mypoke.shiny))
    input("Type anything to return: ")
    return menu(human, mypoke)

def menu_heal(human, mypoke):
    while human.meds > 0:
        print(f"\nYour Pokechong {mypoke.name} has {mypoke.hp}/{mypoke.max_hp} HP! (Meds: {human.meds})")
        med_use = input("Would you like to use a med? ('yes' or 'no'): ")
        if med_use.upper() == "YES":
            print("\nUsed a med!")
            if mypoke.max_hp - mypoke.hp >= 15:
                mypoke.hp += 15
            else:
                mypoke.hp = int(mypoke.max_hp)
            human.meds -= 1
        elif med_use.upper() == "NO":
            print("\nReturning to menu!")
            return menu(human, mypoke)
        else:
            human.errors += 1
            if human.errors >= 10:
                return secret_ending1()
            print("\nGreat typing, stupid!")
    print("\nYou don't have enough meds!")
    return menu(human, mypoke)

def shop(human, mypoke):
    print(f"\nWelcome to the shop! What would you like to buy? (Coins: {human.coins})")
    print(f"Meds: 15 coins (In bag: {human.meds})")
    # print(f"Meds: 20 coins (In bag: {human.hp_ups})")
    # print(f"Meds: 25 coins (In bag: {human.attack_ups})")
    dec = input("\nPlease type what items you would like, or 'exit' the shop: ")
    if dec.upper() == "MEDS":
        try:
            amount = int(input("\nHow many would you like to buy? (Type a number): "))
        except:
            human.errors += 1
            if human.errors >= 10:
                return secret_ending1()
            print("Don't know what numbers are, do you? Let's try that again...")
            return shop(human, mypoke)
        if amount * 15 <= human.coins:
            human.coins -= (amount * 15)
            human.meds += amount
            print("Thank you for your purchase!")
            return menu(human, mypoke)
        else:
            while True:
                steal = input("You can't afford that much! Would you like to steal? ('yes' or 'no'): ")
                if steal.upper() == "YES":
                    return steal_attempt(human, mypoke, amount)
                elif steal.upper() == "NO":
                    print("You picked the moral choice.")
                    return shop(human, mypoke)
                else:
                    human.errors += 1
                    if human.errors >= 10:
                        return secret_ending1()
                    print("Are you trying to be bad typer? Let's circle back...")
    elif dec.upper() == "EXIT":
        return menu(human, mypoke)
    else:
        human.errors += 1
        if human.errors >= 10:
            return secret_ending1()
        print("You really suck at typing, don't you? Let's try that again...")
        return shop(human, mypoke)

def steal_attempt(human, mypoke, amount):
    print("You decided to steal out of a lack of a moral compass!")
    x = random.randrange(100)
    if x > amount * 10:
        print("You successfully stole from the shop! What a terrible human being...")
        human.meds += amount
        return menu(human, mypoke)
    else:
        print("The storeowner caught you cheating and transformed into a Pokechong!\n")
        aipoke = Pokechong("GILGAMESH", 20)
        if mypoke.type == "Grass":
            aipoke.type = "Fire"
        elif mypoke.type == "Water":
            aipoke.type = "Grass"
        else:
            aipoke.type = "Water"
        return battle(human, mypoke, aipoke)

def explore(human, mypoke):
    while True:
        decision = input("\nThere are 'grasslands' and 'roughlands' up ahead, which path will you take? ")
        if decision.upper() == "GRASSLANDS":
            grasslands(human, mypoke)
        elif decision.upper() == "ROUGHLANDS":
            roughlands(human, mypoke)
        else:
            human.errors += 1
            if human.errors >= 10:
                return secret_ending1()
            print("Sorry, I couldn't catch that because of your awful typing! Please try again...")

def grasslands(human, mypoke):
    print("\nYou decided to search through the grasslands for more Pokechong to battle...")
    print("You found a Pokechong! Let the battle begin!\n")
    aipoke = Pokechong(create_name(), 1)
    battle(human, mypoke, aipoke)
    return menu(human, mypoke)

def roughlands(human, mypoke):
    print("\nYou decided to search through the roughlands for more Pokechong to battle...")
    print("You found a Pokechong! Let the battle begin!\n")
    aipoke = Pokechong(create_name(), 3)
    battle(human, mypoke, aipoke)
    return menu(human, mypoke)

def battle(human, mypoke, aipoke):
    print(f"You encountered a {aipoke.name}!")
    while mypoke.hp > 0 and aipoke.hp > 0:
        playerturn(human, mypoke, aipoke)
        if aipoke.hp > 0:
            aiturn(aipoke, mypoke)
    if aipoke.hp <= 0:
        if aipoke.name == "GILGAMESH":
            return secret_ending2()
        xp_gained = aipoke.difficulty * (20 + random.randrange(11))
        print(f"You won the battle! {mypoke.name} gained {xp_gained} EXP!")
        mypoke.level_up += xp_gained
        if mypoke.level_up >= 100:
            mypoke.level_up -= 100
            print(f"{mypoke.name} leveled up and received some stat boosts!")
            mypoke.max_hp += (10 * mypoke.level)
            mypoke.hp += (15 * mypoke.level)
            mypoke.attack += (10 * mypoke.level)
            mypoke.level += 1
        coins_won = aipoke.difficulty * (10 + random.randrange(6))
        human.coins += coins_won
        print(f"You received {coins_won} coins!")
        del aipoke
    else:
        print(f"{mypoke.name} fainted!")
        return gameover()

def attack(attacker, defender):
    if attacker.type == "Grass" and defender.type == "Fire":
        print(f"{attacker.name} did {int(attacker.attack / 1.5)} damage!")
        print("It's not very effective...\n")
        defender.hp -= int(attacker.attack / 1.5)
    elif attacker.type == "Grass" and defender.type == "Water":
        print(f"{attacker.name} did {int(attacker.attack * 1.5)} damage!")
        print("It's super effective!\n")
        defender.hp -= int(attacker.attack * 1.5)
    elif attacker.type == "Fire" and defender.type == "Water":
        print(f"{attacker.name} did {int(attacker.attack / 1.5)} damage!")
        print("It's not very effective...\n")
        defender.hp -= int(attacker.attack / 1.5)
    elif attacker.type == "Fire" and defender.type == "Grass":
        print(f"{attacker.name} did {int(attacker.attack * 1.5)} damage!")
        print("It's super effective!\n")
        defender.hp -= int(attacker.attack * 1.5)
    elif attacker.type == "Water" and defender.type == "Grass":
        print(f"{attacker.name} did {int(attacker.attack / 1.5)} damage!")
        print("It's not very effective...\n")
        defender.hp -= int(attacker.attack / 1.5)
    elif attacker.type == "Water" and defender.type == "Fire":
        print(f"{attacker.name} did {int(attacker.attack * 1.5)} damage!")
        print("It's super effective!\n")
        defender.hp -= int(attacker.attack * 1.5)
    else:
        print(f"{attacker.name} did {attacker.attack} damage!\n")
        defender.hp -= attacker.attack

def playerturn(human, mypoke, aipoke):
    print(f"{aipoke.name}, HP = {aipoke.hp}, Type = {aipoke.type}\n")
    print(f"What should {mypoke.name} do? (HP = {mypoke.hp}, Type = {mypoke.type})")
    command = input("Type 'attack' to attack, 'heal' to heal, or 'run' to run! ")
    if command.upper() == "ATTACK":
        attack(mypoke, aipoke)
    elif command.upper() == "HEAL":
        heal(human, mypoke)
    elif command.upper() == "RUN":
        if random.randrange(10, 51) > aipoke.hp:
            del aipoke
            print("\nGot away safely!")
            menu(human, mypoke)
        print("\nCouldn't escape!")
    else:
        print("\nYou suck at typing and wasted a turn!")
        human.errors += 1

def aiturn(aipoke, mypoke):
    choice = random.randrange(1, 11)
    if choice <= 5:
        return attack(aipoke, mypoke)
    elif choice <= 8:
        if aipoke.max_hp - aipoke.hp >= 5:
            aipoke.hp += 5
            print(f"The wild {aipoke.name} healed itself for 5 HP!")
        else:
            aipoke.hp = int(aipoke.max_hp)
            print(f"The wild {aipoke.name} restored itself to full health!")
    else:
        aipoke.attack += 5
        print(f"The wild {aipoke.name} raised its attack!")

def heal(human, mypoke):
    if human.meds <= 0:
        print("You don't have any meds and wasted a turn!")
        return
    if mypoke.max_hp - mypoke.hp >= 15:
        mypoke.hp += 15
        print(f"You used a med on {mypoke.name} and restored 15 HP!")
    else:
        mypoke.hp = int(mypoke.max_hp)
        print(f"You restored {mypoke.name} to full health!")
    human.meds -= 1

def victory():
    print("You collected 100 coins and won the game! Congratulations!")
    print(f"Throughout your journey, you saw a total of {Pokechong.seenpokes} Pokechong.")
    exit()

def secret_ending1():
    print("\nYour typing was just so abysmal that we had to end the game for you...")
    exit()

def secret_ending2():
    print("\nYou defeated GILGAMESH and discovered a secret ending! Nice job!")
    exit()

def gameover():
    print("\nGame over! You lose...")
    exit()

def create_name():
    possible = ["Joebuscus", "Jeff the 2nd", "Bruhman", "Bruhbutton", "Sandwichman", "Pogversity", "Jeff"]
    return possible[random.randrange(len(possible))]

if __name__ == "__main__":
    print("Welcome to the world of Pokechong! What is your name?\n")
    myname = input("Enter your name here: ")
    human = Human(myname)
    print(f"\nHello, {human.name}! You are about to pick a new Pokechong! Choose a name for it!\n")
    pokename = input("Enter its name here: ")
    mypoke = Pokechong(pokename, 1)
    print(f"\n{pokename} was added to the party! Type: {mypoke.type}, HP: {mypoke.hp}, Attack: {mypoke.attack}, Shiny: {mypoke.shiny}\n")
    human.party.append(mypoke)

    aipoke = Pokechong(create_name(), 1)
    if mypoke.type == "Grass":
        aipoke.type = "Water"
    elif mypoke.type == "Water":
        aipoke.type = "Fire"
    else:
        aipoke.type = "Grass"

    battle(human, mypoke, aipoke)

    print("You are now ready to explore the world of Pokechong! Your adventure starts here!")
    menu(human, mypoke)