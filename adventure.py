from random import randint

location = "home"
player_health = 100
enemy_health = 100


def display_options(location):
    match location:
        case "home":
            print("You are at home.")
            print("1: Go to the arena")
        case "arena":
            print("You are in the arena.")
            print("1: Battle AI")
            print("2: Return home")


def get_choice():
    choice = input("Enter your choice on your keyboard (1-2)")
    if choice == '1':
        return choice
    elif choice == '2':
        return choice
    else:
        print("That is not a valid response!")
        get_choice()


def update_location(choice, location):
    match location:
        case "home":
            match choice:
                case '1':
                    location = "arena"
        case "arena":
            match choice:
                case '1':
                    battle(player_health, enemy_health)
                case '2':
                    location = "home"
    return location


def battle(player_health, enemy_health):
    while player_health > 0 and enemy_health > 0:
        print("What Move do you want to use?")
        print("1: Attack")
        print("2: Defend")
        move = get_choice()
        enemy_move = randint(1, 2)
        match move:
            case '1':
                enemy_health = enemy_health - randint(10, 20)
                print("You attack the enemy and deal damage.")
            case '2':
                print("You defend and take reduced damage.")
        match enemy_move:
            case 1:
                player_health = player_health - randint(5, 15)
                print("The enemy attacks and you take damage.")
            case 2:
                print("The enemy defends and takes reduced damage")

    if player_health <= 0:
        print("You lost the battle!")
    else:
        print("You won the battle!")
    return player_health, enemy_health


def main():
    global location
    while location != "quit":
        display_options(location)
        choice = get_choice()
        location = update_location(choice, location)


main()
