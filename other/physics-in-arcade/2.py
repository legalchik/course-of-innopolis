import arcade
import pymunk

WIDTH = 800
HEIGHT = 600
space = pymunk.Space()
space.gravity = 0, -1000
x = 400
y = 500
mass = 1
inner = 0
radius = 30


class Mygame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.player_list = arcade.SpriteList()
        self.score = 0
        segment = pymunk.Segment(space.static_body, (0, 300), (800, 300), 2)
        segment.elasticity = 1
        segment.friction = 1
        space.add(segment)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.player_list.draw()
        arcade.draw_line(0, 300, 800, 300, arcade.color.RED, 2)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 20, 550, arcade.color.GOLD, 30)

    def on_update(self, delta_time: float):
        space.step(delta_time)
        for index, sprite in enumerate(self.player_list):
            sprite.set_position(space.bodies[index].position.x, space.bodies[index].position.y)
            for body in space.bodies:
                if body.position.y < 350:
                    self.player_list.remove(sprite)
                    space.remove(body)

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.SPACE:
            circle_moment = pymunk.moment_for_circle(mass, inner, radius)
            circle_body = pymunk.Body(mass, circle_moment)
            circle_body.position = x, y

            circle_shape = pymunk.Circle(circle_body, radius)
            circle_shape.elasticity = 0.8
            circle_shape.friction = 1
            space.add(circle_shape, circle_body)
            self.player_list.append(
                arcade.Sprite("circle.png", center_x=circle_body.position.x, center_y=circle_body.position.y,
                              scale=0.15))
            self.score += 1

    def on_key_release(self, symbol, modifiers):
        pass


def main():
    Mygame(WIDTH, HEIGHT, "Physics(Для появления шарика)")
    arcade.run()


main()
