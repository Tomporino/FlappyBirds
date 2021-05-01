import pygame
import neat
import time
import os
from Bird import Bird

def load_sprite(name):
    return pygame.transform.scale2x(
        pygame.image.load(os.path.join("Resources/imgs", name))
    )

FPS = 60

WIN_WIDTH = 500
WIN_HEIGHT = 800

BIRD_SPRITES = [ load_sprite(f"bird{i}.png") for i in range(1, 4)]
PIPE_SPRITE = load_sprite("pipe.png")
BASE_SPRITE = load_sprite("base.png")
BG_IMG = load_sprite("bg.png")


def draw_window(window, bird):
    window.blit(BG_IMG, (0,0))
    bird.draw(window)

    pygame.display.update()

def main():
    bird = Bird(BIRD_SPRITES, 200, 200)
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bird.move()
        draw_window(window, bird)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()