import random

import arcade

WIDTH = 800
HEIGHT = 600


class Mygame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)
        self.playerx = 100
        self.playery = 100
        self.speedx = 300
        self.speedy = 250

        self.sprite1 = arcade.Sprite('persone.png', 0.3, center_x=400, center_y=300)

        self.coin_list = arcade.SpriteList()

        for i in range(6):
            coin = arcade.Sprite('coin.png', 0.2)
            coin.center_x = random.randint(30, 770)
            coin.center_y = random.randint(30, 570)
            self.coin_list.append(coin)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()  # Отрисовал сначала монетку, чтобы она не была поферх персонажа
        self.sprite1.draw()

    def on_update(self, delta_time: float):

        if self.right:
            self.playerx += self.speedx * delta_time
        if self.left:
            self.playerx -= self.speedx * delta_time
        if self.up:
            self.playery += self.speedy * delta_time
        if self.down:
            self.playery -= self.speedy * delta_time
        self.sprite1.set_position(self.playerx, self.playery)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = True

        if symbol == arcade.key.LEFT:
            self.left = True

        if symbol == arcade.key.UP:
            self.up = True

        if symbol == arcade.key.DOWN:
            self.down = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.right = False

        if symbol == arcade.key.LEFT:
            self.left = False

        if symbol == arcade.key.UP:
            self.up = False

        if symbol == arcade.key.DOWN:
            self.down = False


def main():
    game = Mygame(WIDTH, HEIGHT)
    arcade.run()


main()
