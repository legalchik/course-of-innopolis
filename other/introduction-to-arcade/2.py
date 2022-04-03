import arcade

screen1 = 700
screen2 = 700
arcade.open_window(720, 720, 'display')
arcade.start_render()


def snowman(x, y):  # Снеговики
    arcade.draw_circle_filled(x, y, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y + 50, 20, arcade.color.WHITE)


# Первый начальный снеговик
snowman(50, 50)

#  Второй начальный снеговик
snowman(50, 650)

# Первая диагональ
for i in range(100, 700, 50):
    x = i
    y = i + 20
    snowman(x, y)

# ввёл координаты начального снеговика
x = 100
y = 650

for i in range(100, 700, 50):  # Вторая диагональ
    x = i
    y = y - 50
    snowman(x, y)
arcade.finish_render()
arcade.run()
