
import pygame
import random
import os

# pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (173, 9, 9)
green = (17, 173, 9)
black = (0, 0, 0)
yellow = (255,223,0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background image
bg_img = pygame.image.load("snake_img_bg.jpg")
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height)).convert_alpha()
wel_bg_img = pygame.image.load("wel_screen.jpg")
wel_bg_img = pygame.transform.scale(wel_bg_img, (screen_width, screen_height)).convert_alpha()
over_bg_img = pygame.image.load("over.jpg")
over_bg_img = pygame.transform.scale(over_bg_img, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("cobra Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    pygame.mixer.music.stop()
    exit_game = False
    while not exit_game:
        gameWindow.blit(wel_bg_img, (0, 0))
        text_screen("Welcome to nagin Snakes", black, 200, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bg_music = pygame.mixer.Sound("snk_mu_bg.wav")
                    bg_music.set_volume(.2)
                    ch1.play(bg_music, -1)
                    gameloop()

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

def check(a, b):
    for y in b:
        if (a[0] > y[0] - 10 and a[0] < y[0] + 10) and (a[1] > y[1] - 10 and a[1] < y[1] + 10):
            return True


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    demo_snake_x = random.randint(60, screen_width-80)
    demo_snake_y = random.randint(60, screen_height-80)
    demo_velocity_x = 0
    demo_velocity_y = 0
    demo_snk_list = []
    demo_snk_length = 100
    count = 0
    # Check if high_score.txt exists
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(40, screen_width - 50)
    food_y = random.randint(40, screen_height - 50)
    s_food_x = random.randint(40, screen_width - 50)
    s_food_y = random.randint(40, screen_height - 50)
    score = 0
    init_velocity = 1.5
    demo_init_velocity = 0.5
    snake_size = 10
    fps = 60
    while not exit_game:
        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(over_bg_img, (0, 0))
            text_screen("Game Over! Press Enter To to go to Main Menu", red, 30, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # Cheat code
                    if event.key == pygame.K_q:
                        if snk_length > 20:
                            snk_length = snk_length - 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
            if choice == 10:
                choice1 = random.choice([0, 1, 2, 3])
                if choice1 == 0:
                    if not (demo_velocity_x < 0):
                        demo_velocity_x = demo_init_velocity
                        demo_velocity_y = 0
                elif choice1 == 2:
                    if not (demo_velocity_x > 0):
                        demo_velocity_x = -demo_init_velocity
                        demo_velocity_y = 0
                elif choice1 == 1:
                    if not (demo_velocity_y > 0):
                        demo_velocity_x = 0
                        demo_velocity_y = -demo_init_velocity
                elif choice1 == 3:
                    if not (demo_velocity_y < 0):
                        demo_velocity_x = 0
                        demo_velocity_y = demo_init_velocity

            if demo_snake_x < 5:
                demo_velocity_x = demo_init_velocity
                demo_velocity_y = 0
            elif demo_snake_x > screen_width-5:
                demo_velocity_x = -demo_init_velocity
                demo_velocity_y = 0
            elif demo_snake_y < 30:
                demo_velocity_x = 0
                demo_velocity_y = demo_init_velocity
            elif demo_snake_y > screen_height-50:
                demo_velocity_x = 0
                demo_velocity_y = -demo_init_velocity

            demo_snake_x = demo_snake_x + demo_velocity_x
            demo_snake_y = demo_snake_y + demo_velocity_y

            if abs(snake_x - food_x) < 7 and abs(snake_y - food_y) < 7:
                # pygame.mixer.Channel(1).play(pygame.mixer.Sound("Snake_Eat1.wav"), maxtime = 60000)
                count = count + 1
                eat_sound = pygame.mixer.Sound("Snake_Eat1.wav")
                eat_sound.set_volume(1)
                ch2.play(eat_sound, maxtime = 800)
                score += 10
                food_x = random.randint(40, screen_width - 50)
                food_y = random.randint(40, screen_height - 50)
                snk_length *= 2
                if score > int(hiscore):
                    hiscore = score

            if count == 5:
                pygame.draw.circle(gameWindow, yellow, [s_food_x, s_food_y], 5)
                pygame.display.update()
                if abs(snake_x - s_food_x) < 7 and abs(snake_y - s_food_y) < 7:
                    count = 0
                    # pygame.mixer.Channel(1).play(pygame.mixer.Sound("Snake_Eat1.wav"), maxtime = 60000)
                    eat_sound = pygame.mixer.Sound("Snake_Eat1.wav")
                    eat_sound.set_volume(1)
                    ch2.play(eat_sound, maxtime=800)
                    s_food_x = random.randint(40, screen_width - 50)
                    s_food_y = random.randint(40, screen_height - 50)
                    if snk_length > 60:
                        snk_length = int(snk_length/1.5)
                    else:
                        snk_length -= 2
                    score += 5
                    if score > int(hiscore):
                        hiscore = score

            if count > 5:
                count = 0

            gameWindow.blit(bg_img, (0,0))
            text_screen("Score: " + str(score) + "  Highscore: "+str(hiscore), white, 5, 5)
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                l = len(snk_list) - snk_length
                for i in range(l):
                    del snk_list[i]

            demo_head = []
            demo_head.append(demo_snake_x)
            demo_head.append(demo_snake_y)
            demo_snk_list.append(demo_head)

            if len(demo_snk_list) > demo_snk_length:
                del demo_snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                ch1.stop()
                over_sound = pygame.mixer.Sound("snk_game_over.wav")
                over_sound.set_volume(1)
                ch3.play(over_sound, maxtime= 5000)

            if check(head, demo_snk_list):
                game_over = True
                ch1.stop()
                over_sound = pygame.mixer.Sound("snk_game_over.wav")
                over_sound.set_volume(1)
                ch3.play(over_sound, maxtime=5000)

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                ch1.stop()
                over_sound = pygame.mixer.Sound("snk_game_over.wav")
                over_sound.set_volume(1)
                ch3.play(over_sound, maxtime=5000)

            eye = []
            for i in head:
                i = i + 5
                eye.append(i)

            plot_snake(gameWindow, yellow, snk_list, snake_size)
            pygame.draw.circle(gameWindow, black, eye, 2)
            plot_snake(gameWindow, red, demo_snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()



if __name__ == "__main__":
    ch1 = pygame.mixer.Channel(0)
    ch2 = pygame.mixer.Channel(1)
    ch3 = pygame.mixer.Channel(2)
    welcome()
