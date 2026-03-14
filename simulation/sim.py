import pygame
import numpy as np
import numerical

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

g = 981  # m/s^2
L = 200  # m

origin = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
theta = np.radians(70)
omega = 0
pos = pygame.Vector2(origin.x + (L * np.sin(theta)), origin.y + (L * np.cos(theta)))


def a(theta, omega):
    B = 0.5
    return -(g / L) * np.sin(theta) - B * omega


def x(omega):
    return omega


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    pygame.draw.circle(screen, "black", origin, 10)
    pygame.draw.circle(screen, "red", pos, 20)
    theta, omega = numerical.pendulum_step(a, x, theta, omega, dt)
    pos.x = origin.x + L * np.sin(theta)
    pos.y = origin.y + L * np.cos(theta)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
