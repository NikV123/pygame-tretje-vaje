import random
import pygame
from pygame import event

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
bg_color = (0, 0, 0)
pygame.display.set_caption("Flappy bird")

background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (width, height))


def jump():
    global ball_speed
    ball_speed = ball_space


# OVIRA
ovira_sirina = 100
ovira_dolzina = 300
ovira_barva = (0, 255, 0)
ovira_speed = 5

# ZOGA
ball_radius = 10
ball_color = (255, 0, 0)
ball_zac_poz = (width // 4, height // 2)
ball_gravity = 0.3
ball_space = 10

# PRIPRAVA ZOGE
ball_position = list(ball_zac_poz)
ball_speed = 0

# PRIPRAVA OVIRE
ovira_x = width
ovira_gap = 200
ovira_y = random.randint(ovira_gap, height - ovira_gap)

# TOČKOVNIK
score = 0
font = pygame.font.SysFont(None, 55)


def display_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def game_over():
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text,
                (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    exit()


clock = pygame.time.Clock()
while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    ball_speed -= ball_gravity
    ball_position[1] -= ball_speed
    pygame.draw.circle(screen, ball_color, (ball_position[0], int(ball_position[1])), ball_radius)

    # premikanje ovire
    ovira_x -= ovira_speed
    if ovira_x < -ovira_sirina:
        ovira_x = width
        ovira_gap = random.randint(150, 400)
        ovira_y = random.randint(ovira_gap, height - ovira_gap)
        score += 1  # Povečaj točko ob prehodu ovire

    pygame.draw.rect(screen, ovira_barva, (ovira_x, 0, ovira_sirina, ovira_y - ovira_gap // 2))
    pygame.draw.rect(screen, ovira_barva, (ovira_x, ovira_y + ovira_gap // 2, ovira_sirina, height - ovira_y // 2))

    # detekcija trčenja
    if (ball_position[0] + ball_radius >= ovira_x and ball_position[0] - ball_radius <= ovira_x + ovira_sirina and
            (ball_position[1] - ball_radius <= ovira_y - ovira_gap // 2 or ball_position[
                1] + ball_radius >= ovira_y + ovira_gap // 2)):
        game_over()

    display_score(score)
    pygame.display.update()
    clock.tick(60)