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
        self.score = 0
        self.sprite1 = arcade.Sprite('persone.png', 0.3, center_x=400, center_y=300)
        self.coin = arcade.Sprite('coin.png', 0.2)
        self.coin.center_x = random.randint(30, 770)
        self.coin.center_y = random.randint(30, 570)

        self.weapon_list = arcade.SpriteList()
        for j in range(5):
            weapon = arcade.Sprite('weapon.png', 0.1)
            weapon.center_x = random.randint(30, 770)
            weapon.center_y = random.randint(30, 570)
            self.weapon_list.append(weapon)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def on_draw(self):
        arcade.start_render()
        self.coin.draw()# Отрисовал сначала монетку, чтобы она не была поферх персонажа
        self.weapon_list.draw()
        self.sprite1.draw()
        output = f"Money: {self.score}"
        arcade.draw_text(output, 20, 550, arcade.color.GOLD, 30)

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
        coin_hit = arcade.check_for_collision(self.sprite1, self.coin, )
        if coin_hit == True:
            self.coin.kill()
            self.score += 1
            self.coin = arcade.Sprite('coin.png', 0.2)
            self.coin.center_x = random.randint(30, 770)
            self.coin.center_y = random.randint(30, 570)

        weapon_hit = arcade.check_for_collision_with_list(self.sprite1, self.weapon_list)
        for i in weapon_hit:
            i.center_x = random.randint(30, 770)
            i.center_y = random.randint(30, 570)



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
    Mygame(WIDTH, HEIGHT)
    arcade.run()


main()
