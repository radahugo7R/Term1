# Import Libraries
import pygame # Used to generate the GUI
from random import randint # Used to generate random ints
from time import sleep # Used to wait/sleep

# Assign default variables
location = "home" # Players starting location
player_health = 100 # Players starting health
enemy_health = 100 # Enemy's starting health
in_battle = False # Whether or not the player is currently in a battle

# Init and configure the pygame gui
pygame.init()
screen = pygame.display.set_mode((400, 300))


# Display the players location options on the screen
# @param: Location - The current location of the player
def display_options(location):
    font = pygame.font.Font(None, 36)
    if location == "home":
        text = font.render("You are at home.", True, (255, 255, 255))
        text2 = font.render("1: Go to the arena", True, (255, 255, 255))
        text3 = font.render("2: Quit Game", True, (255, 255, 255))
    elif location == "arena":
        text = font.render("You are in the arena.", True, (255, 255, 255))
        text2 = font.render("1: Battle AI", True, (255, 255, 255))
        text3 = font.render("2: Return home", True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(text, (100, 100))
    screen.blit(text2, (100, 150))
    screen.blit(text3, (100, 200))
    pygame.display.update()


# Listen for input and return the string value
def get_choice():
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.unicode == '1':
                return '1'
            elif event.unicode == '2':
                return '2'

# Update the dynamic location variables
# @param: choice - The users choice of where to go
# @param: location - The users current location
def update_location(choice, location):
    global player_health, enemy_health
    if location == "home":
        if choice == '1':
            location = "arena"
        elif choice == '2':
            location = "quit"
    elif location == "arena":
        if choice == '1':
            player_health, enemy_health = battle(player_health, enemy_health)
        elif choice == '2':
            location = "home"
    return location

# Main Battle Function
# @param: player_health - Previously defined variable
# @param: enemy_health - Previously defined variable
def battle(player_health, enemy_health):
    global in_battle, move_enemy, move, text4
    move = "ply1"

    font = pygame.font.Font(None, 36)
    while player_health > 0 and enemy_health > 0:
        in_battle = True
        text = font.render("What move do you want to use?", True, (255, 255, 255))
        text2 = font.render("1: Attack", True, (255, 255, 255))
        text3 = font.render("2: Defend", True, (255, 255, 255))

        if move == 'ply1':
            text4 = font.render("Your Move", True, (255, 255, 255))
        elif move == 'ply2':
            text4 = font.render("Enemy's Move", True, (255, 255, 255))

        text5 = font.render(str(player_health), True, (0, 0, 255))
        text6 = font.render(str(enemy_health), True, (255, 0, 0))

        move = get_choice()

        if move == '1':
            move = 'ply1'
            enemy_health = enemy_health - randint(10, 20)
            move = 'ply2'
            player_health = player_health - randint(5, 15)
            move = 'ply1'
        elif move == '2':
            player_health = player_health - randint(5, 15)
            move = 'ply1'

        screen.fill((0, 0, 0))
        screen.blit(text, (15, 50))
        screen.blit(text2, (30, 100))
        screen.blit(text3, (250, 100))
        screen.blit(text4, (130, 165))
        screen.blit(text5, (5, 265))
        screen.blit(text6, (355, 265))
        pygame.display.update()

    if player_health <= 0:
        player_health = 0

        screen.fill((0, 0, 0))
        text = font.render("You lost!", True, (255, 0, 0))
        screen.blit(text, (130, 130))
        pygame.display.update()

        sleep(5)
        pygame.quit()
    else:
        enemy_health = 0

        screen.fill((0, 0, 0))
        text = font.render("You won!", True, (255, 215, 0))
        screen.blit(text, (130, 130))
        pygame.display.update()

        sleep(5)
        pygame.quit()

    pygame.display.update()
    return player_health, enemy_health


# Main game function, called when the program starts.
def main():
    global location
    while location != "quit":
        if not in_battle:
            display_options(location)
            choice = get_choice()
            location = update_location(choice, location)
    pygame.quit()


main()
