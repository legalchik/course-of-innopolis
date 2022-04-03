# Выглядит, как художество первоклассника
# Простите за кислотные цвета
# При сворачивании требуется перезагрузка программы
import arcade

arcade.open_window(700, 700, 'display')
arcade.start_render()
arcade.draw_rectangle_filled(350, 350, 700, 700, arcade.color.BLUE)  # Небо

arcade.draw_arc_filled(350, 0, 750, 600, arcade.color.GREEN, 0, 180)  # Земля

arcade.draw_rectangle_filled(350, 350, 100, 100, arcade.color.BROWN)  # Дом

arcade.draw_triangle_filled(300, 400, 350, 450, 400, 400, arcade.color.RED)  # Крыша дома

arcade.draw_circle_filled(650, 650, 75, arcade.color.YELLOW)  # Солнце

arcade.draw_circle_filled(320, 350, 15, arcade.color.CYAN)  # Окна
arcade.draw_circle_filled(380, 350, 15, arcade.color.CYAN)
arcade.draw_line(320, 370, 320, 310, arcade.color.BROWN, 3)
arcade.draw_line(300, 350, 395, 350, arcade.color.BROWN, 3)
arcade.draw_line(380, 370, 380, 310, arcade.color.BROWN, 3)


arcade.draw_line(600, 600, 550, 550, arcade.color.YELLOW, 5)
arcade.draw_line(700, 700, 500, 600, arcade.color.YELLOW, 5)
arcade.draw_line(700, 700, 600, 500, arcade.color.YELLOW, 5)  # Лучики
arcade.draw_line(700, 700, 650, 490, arcade.color.YELLOW, 5)
arcade.draw_line(700, 700, 490, 650, arcade.color.YELLOW, 5)

arcade.finish_render()
arcade.run()
