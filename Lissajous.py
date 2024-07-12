import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lissajous Curve")

WHITE = (255, 255, 255)

A = WIDTH // 2.01
B = HEIGHT // 2.01
a, b = 10, 9 # Frequency ratio for the x and y oscillation, feel free to experiment with them.

running = True
t = 0 
shouldGen = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw points
    if shouldGen:
        for _ in range(100):  # Draw 100 points per frame
            x = A * math.sin(a * t)
            y = B * math.sin(b * t)

            dot_pos = (round(WIDTH // 2 + x), round(HEIGHT // 2 + y))
            pygame.draw.circle(screen, WHITE, dot_pos, 1)  # Draw points
            t += 0.000005

            if t >= 2 * math.pi:
                shouldGen = False
                break

        pygame.display.flip()

    pygame.time.delay(1)


pygame.quit()
