import pygame

class Bird:
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, sprites, x, y):
        self.x = x
        self.y = y
        self.SPRITES = sprites
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.SPRITES[0]


    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.5 * self.tick_count**2
        # With tick_count set 0 in jump() we make the bird go upwards until it
        # get it's full height so it will go downwards

        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            # Tilt the bird upwards
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            # Tilt bird downwards
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    
    def set_current_sprite(self):
        if self.img_count < self.ANIMATION_TIME:
            self.img = self.SPRITES[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.SPRITES[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.SPRITES[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.SPRITES[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.SPRITES[0]
            self.img_count = 0

        # If the bird is falling then show only 1 sprite
        if self.tilt <= -80:
            self.img = self.SPRITES[1]
            self.img_count = self.ANIMATION_TIME*2


    def draw(self, window):
        self.img_count += 1

        self.set_current_sprite()

        # Rotate our image (It's black magic from SO)
        rotated_sprite = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_sprite.get_rect(center=self.img.get_rect(topleft= (self.x, self.y)).center)
        window.blit(rotated_sprite, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
        