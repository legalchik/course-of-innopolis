

#  ПРОСТИТЕ ЗА ПЛОХОЕ КАЧЕСТВО ПЕРСОНАЖА


import random

import arcade

WIDTH = 800
HEIGHT = 600


class Mygame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

        self.score = 0
        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture('StapRight.png'))
        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture('WalkRight1.png'))
        self.player.walk_right_textures.append(arcade.load_texture('WalkRight2.png'))
        self.player.walk_right_textures.append(arcade.load_texture('WalkRight3.png'))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture('StapLeft.png'))
        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture('WalkLeft1.png'))
        self.player.walk_left_textures.append(arcade.load_texture('WalkLeft2.png'))
        self.player.walk_left_textures.append(arcade.load_texture('WalkLeft3.png'))

        self.player.walk_up_textures = []
        self.player.walk_up_textures.append(arcade.load_texture('WalkUp1.png'))
        self.player.walk_up_textures.append(arcade.load_texture('WalkUp2.png'))
        self.player.walk_up_textures.append(arcade.load_texture('WalkUp3.png'))

        self.player.walk_down_textures = []
        self.player.walk_down_textures.append(arcade.load_texture('WalkDown1.png'))
        self.player.walk_down_textures.append(arcade.load_texture('WalkDown2.png'))
        self.player.walk_down_textures.append(arcade.load_texture('WalkDown3.png'))

        self.player.center_x = 400
        self.player.center_y = 300
        self.player.scale = 4.5
        self.player_list.append(self.player)
        self.coin_list = arcade.SpriteList()
        self.coin = arcade.AnimatedTimeBasedSprite()
        self.coin.frames = []
        self.coin.scale = 0.2

        self.fon = arcade.Sprite('fon.png', center_x=400, center_y=300)

        for i in range(2):
            for j in range(3):
                tex = arcade.load_texture('coin.png', x=j * 220, y=i * 230, width=220, height=230)
                frame = arcade.AnimationKeyframe(1, 120, tex)
                self.coin.frames.append(frame)

        self.coin.center_x = random.randint(30, 600)
        self.coin.center_y = random.randint(30, 600)
        self.coin_list.append(self.coin)

    def on_draw(self):
        arcade.start_render()
        self.fon.draw()
        self.coin_list.draw()
        self.player_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 20, 550, arcade.color.GOLD, 30)

    def on_update(self, delta_time: float):
        self.player_list.update()
        self.player_list.update_animation()
        self.coin_list.update_animation()
        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list, )
        for i in coin_hit_list:
            i.remove_from_sprite_lists()
            self.score += 1
            self.coin.center_x = random.randint(30, 600)
            self.coin.center_y = random.randint(30, 600)
            self.coin_list.append(self.coin)
            if self.score == 20:
                self.score = 0
                self.coin.center_x = random.randint(30, 600)
                self.coin.center_y = random.randint(30, 600)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.player.change_x = 8

        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.player.change_x = -8

        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.player.change_y = 8

        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.player.change_y = -8

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.player.change_x = 0

        if symbol == arcade.key.LEFT or symbol == arcade.key.A:
            self.player.change_x = 0

        if symbol == arcade.key.UP or symbol == arcade.key.W:
            self.player.change_y = 0

        if symbol == arcade.key.DOWN or symbol == arcade.key.S:
            self.player.change_y = 0


def main():
    Mygame(WIDTH, HEIGHT)
    arcade.run()


main()
