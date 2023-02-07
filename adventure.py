import pygame
from random import randint

location = "home"
player_health = 100
enemy_health = 100

pygame.init()
screen = pygame.display.set_mode((400, 300))


def display_options(location):
    font = pygame.font.Font(None, 36)
    if location == "home":
        text = font.render("You are at home.", True, (255, 255, 255))
        text2 = font.render("1: Go to the arena", True, (255, 255, 255))
    elif location == "arena":
        text = font.render("You are in the arena.", True, (255, 255, 255))
        text2 = font.render("1: Battle AI", True, (255, 255, 255))
        text3 = font.render("2: Return home", True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(text, (100, 100))
    screen.blit(text2, (100, 150))
    if location == "arena":
        screen.blit(text3, (100, 200))
    pygame.display.update()


def get_choice():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.unicode == '1':
                return '1'
            elif event.unicode == '2':
                return '2'


def update_location(choice, location):
    global player_health, enemy_health
    if location == "home":
        if choice == '1':
            location = "arena"
    elif location == "arena":
        if choice == '1':
            player_health, enemy_health = battle(player_health, enemy_health)
        elif choice == '2':
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
