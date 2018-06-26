import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    class enemies: 

        def __init__(self):
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

            "hier wordt het spel opgezet om gespeeld te worden, de vijanden worden toegevoegd en de speler wordt neergezet"
            

            file_path = os.path.dirname(os.path.abspath(__file__))
            os.chdir(file_path)

            arcade.set_background_color(arcade.color.OXFORD_BLUE)

            self.frame_count = 0

            self.all_sprites_list = arcade.SpriteList()
            self.enemy_list = arcade.SpriteList()
            self.player_list = arcade.SpriteList()
            self.bullet_list = arcade.SpriteList()
            self.score = 0

            self.player = arcade.Sprite("images/playerShip1_orange.png", 0.5)
            self.player_list.append(self.player)
            self.all_sprites_list.append(self.player)

            enemy = arcade.Sprite("images/playerShip1_green.png", 0.5)
            enemy.center_x = 120
            enemy.center_y = SCREEN_HEIGHT - enemy.height
            enemy.angle = 180
            self.all_sprites_list.append(enemy)
            self.enemy_list.append(enemy)

            enemy = arcade.Sprite("images/playerShip1_green.png", 0.5)
            enemy.center_x = SCREEN_WIDTH - 120
            enemy.center_y = SCREEN_HEIGHT - enemy.height
            enemy.angle = 180
            self.all_sprites_list.append(enemy)
            self.enemy_list.append(enemy)

            enemy = arcade.Sprite("images/playerShip1_green.png", 0.5)
            enemy.center_x = 250
            enemy.center_y = SCREEN_HEIGHT - enemy.height
            enemy.angle = 180
            self.all_sprites_list.append(enemy)
            self.enemy_list.append(enemy)
            
            enemy = arcade.Sprite("images/playerShip1_green.png", 0.5)
            enemy.center_x = 550
            enemy.center_y = SCREEN_HEIGHT - enemy.height
            enemy.angle = 180
            self.all_sprites_list.append(enemy)
            self.enemy_list.append(enemy)

            boss = arcade.Sprite("images/playerBoss1_red.png", 1.2)
            boss.center_x = 400
            boss.center_y = SCREEN_HEIGHT - boss.height
            boss.angle = 180
            self.all_sprites_list.append(boss)
            self.enemy_list.append(boss)

    class game:
        "hier wordt het scherm neergezet, dus hoe het spel er zlef uit ziet"

        def respawn(self):
            self.respawning = 1
            self.center_x = SCREEN_WIDTH / 2
            self.center_y = SCREEN_HEIGHT / 2


        def on_draw(self):
            """Render the screen. """

            arcade.start_render()

            self.all_sprites_list.draw()

            output = f"Score: {self.score}"
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    class update:
        "hier vind alles plaats wat met updates moet gebeuren, wat er gebeurt na een bepaalde hoeveelheid tijd"

        def update(self, delta_time):

            self.frame_count += 1

            for enemy in self.enemy_list:

                if random.randrange(150) == 0:
                    bullet = arcade.Sprite("images/laserBlue01.png")
                    bullet.center_x = enemy.center_x
                    bullet.angle = -90
                    bullet.top = enemy.bottom
                    bullet.change_y = -8
                    self.bullet_list.append(bullet)
                    self.all_sprites_list.append(bullet)  


            self.bullet_list.update()

            for bullet in self.bullet_list:
                if bullet.top < 0:
                    bullet.kill()
                    self.score -= 1

                if bullet.top >600:
                    bullet.kill()
                    self.score += 1
            
                hit_list = arcade.check_for_collision_with_list(bullet, self.player_list)

                for self.player in hit_list:
                    bullet.change_y = +15
                    bullet.angle = 90
                    self.score += 1


            for self.player in self.player_list:
                col_list = arcade.check_for_collision_with_list(self.player, self.enemy_list)
                if col_list:
                    self.player.kill()


        def on_mouse_motion(self, x, y, delta_x, delta_y):
        
            self.player.center_x = x
            self.player.center_y = y
        
        
            
        
        

def main():
    MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
