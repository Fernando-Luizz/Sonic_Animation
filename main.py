import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sonic Animation")
blue_color = (173, 216, 230)

stopped_sprites = [pygame.image.load("assets/stopped/run1.jpeg"), pygame.image.load("assets/stopped/run2.jpeg"), pygame.image.load("assets/stopped/run3.jpeg"), pygame.image.load("assets/stopped/run4.jpeg"), pygame.image.load("assets/stopped/run5.jpeg")]
run_sprites = [pygame.image.load("assets/run/run6.jpeg"), pygame.image.load("assets/run/run7.jpeg"), pygame.image.load("assets/run/run8.jpeg"), pygame.image.load("assets/run/run9.jpeg"), pygame.image.load("assets/run/run10.jpeg"), pygame.image.load("assets/run/run11.jpeg"), pygame.image.load("assets/run/run12.jpeg"), pygame.image.load("assets/run/run13.jpeg"), pygame.image.load("assets/run/run14.jpeg"), pygame.image.load("assets/run/run15.jpeg")]
roll_sprites = [pygame.image.load("assets/roll/roll1.jpeg"), pygame.image.load("assets/roll/roll2.jpeg"), pygame.image.load("assets/roll/roll3.jpeg"), pygame.image.load("assets/roll/roll4.jpeg") , pygame.image.load("assets/roll/roll5.jpeg"), pygame.image.load("assets/roll/roll6.jpeg")]
hang_sprites = [pygame.image.load("assets/hang/hang1.jpeg"), pygame.image.load("assets/hang/hang2.jpeg"), pygame.image.load("assets/hang/hang3.jpeg"), pygame.image.load("assets/hang/hang4.jpeg"), pygame.image.load("assets/hang/hang5.jpeg")]

x, y = 100, 500
initial_y = y  # Armazenar a posição inicial do eixo y
speed = 5

current_animation = stopped_sprites
frame_index = 0
animation_speed = 95
counter = 0

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_position(keys):
    global x, y, current_animation, initial_y
    if keys[pygame.K_RIGHT]:
        x += speed
        current_animation = run_sprites
    elif keys[pygame.K_LEFT]:
        x -= speed
        current_animation = run_sprites
    else:
        current_animation = stopped_sprites

    if keys[pygame.K_DOWN]:
        current_animation = roll_sprites

    if keys[pygame.K_UP]:
        current_animation = hang_sprites
        initial_y = y
        y -= 50

    if not keys[pygame.K_UP] and y < initial_y:
        y = initial_y

def update_animation_frame():
    global frame_index, counter
    counter += 1
    if current_animation and len(current_animation) > 0:
        frame_index = (frame_index + 1) % len(current_animation)

def draw_screen():
    screen.fill(blue_color)
    if current_animation and len(current_animation) > 0:
        screen.blit(current_animation[frame_index], (x, y))
    pygame.display.flip()

clock = pygame.time.Clock()

while True:
    handle_events()
    keys = pygame.key.get_pressed()
    update_position(keys)
    update_animation_frame()
    draw_screen()
    clock.tick(5)
