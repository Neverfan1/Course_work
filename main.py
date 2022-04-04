import pygame
import random

pygame.init()

# -----------------------------------IMAGE
# ------------------DISPLAY
icon = pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/game_icon.png")
# -----------------MAIN HERO
hero_image = pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/Garry1.png")
# ----------------BACKGROUND
background = pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/background3.png")
# -----------------BLOCKS
block_img = [pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/block1.png"),
             pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/block2.png"),
             pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/block3.png")]
# ----------------DECOR
seashells_image = [pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/seashells1.png"),
                   pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/seashells2.png"),
                   pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/seashells3.png"),
                   pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/seashells4.png")]
treasure_image = [pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/treasure1.png"),
                  pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/treasure2.png")]
fish_image = [pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/fish1.png"),
              pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/fish2.png"),
              pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/fish3.png"), ]
health_image = pygame.image.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Icons/heart.png")
health_image = pygame.transform.scale(health_image, (25, 25))
health_image2 = pygame.transform.scale(health_image, (35, 35))
# -------------------------------------------------------------

# ------------------------------SOUNDS
#pygame.mixer.music.load(r"/Users/danilaparamin/Desktop/Курсовая/игра/Sounds/background_sound.mp3")
pygame.mixer.music.set_volume(0.3)

jump_sound = pygame.mixer.Sound(r"/Users/danilaparamin/Desktop/Курсовая/игра/Sounds/jump_sound.mp3")
bash_sound = pygame.mixer.Sound(r"/Users/danilaparamin/Desktop/Курсовая/игра/Sounds/bash_sound.mp3")
lost_sound = pygame.mixer.Sound(r"/Users/danilaparamin/Desktop/Курсовая/игра/Sounds/lost1_sound.mp3")
health_sound = pygame.mixer.Sound(r"/Users/danilaparamin/Desktop/Курсовая/игра/Sounds/health_sound.mp3")

# --------------------DISPLAY
display_width = 800
display_height = 600
# display = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE | pygame.SCALED)
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Running Garry:)")
pygame.display.set_icon(icon)

# --------------------FPS
clock = pygame.time.Clock()
FPS = 60

# ---------------------MAIN HERO
hero_width = 60
hero_height = 100
hero_x = display_width // 3
hero_y = display_height - hero_height - 97

# --------------------SPEED
speed_game = 1
speed_block = 5
speed_hero = 1
speed_decor = 4
speed_score = 1
speed_health = 4

# --------------------BLOCKS
block_options = [80, 418, 80, 418, 96, 408]

# ----------------- FOR JUMP
jump = False
jmp_counter = 30

# --------------- FOR SCORE
score = 0
max_score = 0
max_blocks = 0

# ----------------HEALTH SCORE
health = 3


# ----------------CLASS BLOCK
class Object:
    def __init__(self, x, y, width, speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.speed = speed
        self.image = image

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, distance, y, width, image):
        self.x = distance
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


# -----------------FUNCTION FOR START GAME
def start_game():
    global jump, speed_game, speed_score
    game = True

    #pygame.mixer.music.play(-1)
    block_arr = []
    create_block_arr(block_arr)
    heart = Object(display_width, 300, 30, speed_health * speed_game, health_image2)

    seashells, treasure, fish = random_img_decor()

    while game:
        for event in pygame.event.get():
            # -------EXIT1
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        # ---------EXIT2
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        # ------------JUMP
        if key[pygame.K_SPACE]:
            jump = True
        if jump:
            make_jump()
        if key[pygame.K_p]:
            pause()
        if key[pygame.K_1]:
            speed_game = 1
            speed_score = 1
            block_arr = []
            seashells, treasure, fish = random_img_decor()
            create_block_arr(block_arr)
            heart = Object(display_width, 300, 30, speed_health * speed_game, health_image2)

        if key[pygame.K_2]:
            speed_game = 1.5
            speed_score = 2
            block_arr = []
            seashells, treasure, fish = random_img_decor()
            create_block_arr(block_arr)
            heart = Object(display_width, 300, 30, speed_health * speed_game, health_image2)

        if key[pygame.K_3]:
            speed_game = 2
            speed_score = 3
            block_arr = []
            seashells, treasure, fish = random_img_decor()
            create_block_arr(block_arr)
            heart = Object(display_width, 300, 30, speed_health * speed_game, health_image2)


        counter_score(block_arr)

        display.blit(background, (0, 0))

        print_text("SCORE:" + str(score), 600, 10)

        draw_array_blocks(block_arr)

        move_decor(seashells, treasure, fish)

        display.blit(hero_image, (hero_x, hero_y))

        heart.move()
        pick_heart(heart)

        if check_collision(block_arr):
            game = False
            pygame.mixer.music.stop()
        health_draw()
        pygame.display.update()  # update display
        clock.tick(FPS)  # set FPS
    return game_over()


# --------------FUNCTION FOR JUMP
def make_jump():
    global hero_y, jmp_counter, jump
    if jmp_counter >= -30:
        if jmp_counter == 30:
            pygame.mixer.Sound.play(jump_sound)

        hero_y -= jmp_counter / 2.5 * speed_hero * speed_game
        jmp_counter -= 1 * speed_hero * speed_game
    else:
        jmp_counter = 30
        jump = False


# -------------------------------FUNCTIONS FOR OBJECT

# --------------CREAT
def create_block_arr(array):
    rand = random.randrange(0, 3)
    image = block_img[rand]
    width = block_options[rand * 2]
    height = block_options[rand * 2 + 1]
    array.append(Object(display_width + 20, height, width, speed_block * speed_game, image))

    rand = random.randrange(0, 3)
    image = block_img[rand]
    width = block_options[rand * 2]
    height = block_options[rand * 2 + 1]
    array.append(Object(display_width + 320, height, width, speed_block * speed_game, image))

    rand = random.randrange(0, 3)
    image = block_img[rand]
    width = block_options[rand * 2]
    height = block_options[rand * 2 + 1]
    array.append(Object(display_width + 620, height, width, speed_block * speed_game, image))


# -------------CORRECT DISTANCE
def find_distance(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    distance = maximum
    if distance < display_width:
        distance = display_width + 20

    # --- two options respawn block
    rand = random.randrange(0, 5)
    if rand == 0:
        distance += 32  # -- first
    else:
        distance += random.randrange(450, 600)  # -- twice

    return distance


# -------------DRAW
def draw_array_blocks(array):
    for block in array:
        check = block.move()
        if not check:
            return_obj(array, block)


# -----------------------------------------------------------------------
# -------------------- RANDOM IMG FOR DECOR

def random_img_decor():
    rand1 = random.randrange(0, 4)
    rand2 = random.randrange(0, 2)
    rand3 = random.randrange(0, 3)

    img_fish = fish_image[rand3]
    img_treasure = treasure_image[rand2]
    img_seashells = seashells_image[rand1]

    seashells = Object(display_width, display_height - 85, 55, speed_decor * speed_game, img_seashells, )
    treasure = Object(display_width + 100, display_height - 4, 96, speed_decor * speed_game, img_treasure, )
    fish = Object(display_width, 89, 96, speed_decor * speed_game, img_fish)

    return seashells, treasure, fish


# --------------------- MOVE DECOR
def move_decor(seashells, treasure, fish):
    check1 = seashells.move()
    if not check1:
        rand1 = random.randrange(0, 4)
        img_seashells = seashells_image[rand1]
        seashells.return_self(display_width, 470 + random.randrange(15, 67), seashells.width, img_seashells)

    check2 = treasure.move()
    if not check2:
        rand2 = random.randrange(0, 2)
        img_treasure = treasure_image[rand2]
        treasure.return_self(display_width, 470 + random.randrange(25, 37), treasure.width, img_treasure)

    check3 = fish.move()
    if not check3:
        rand3 = random.randrange(0, 3)
        img_fish = fish_image[rand3]
        fish.return_self(display_width, random.randrange(30, 300), fish.width, img_fish)


# ------------------------ PRINT TEXT
def print_text(txt, x, y, color=(0, 0, 0), type="paper_cuts.ttf", size=30):
    type = pygame.font.Font(type, size)
    text = type.render(txt, True, color)
    display.blit(text, (x, y))


# ------------------------PAUSE
def pause():
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text("Paused.If you want to continue press U.", 160, 300)
        pygame.display.update()
        clock.tick(20)

        key = pygame.key.get_pressed()
        if key[pygame.K_u]:
            paused = False
    pygame.mixer.music.unpause()


# ------------------------RETURN OBJ
def return_obj(objs, obj):
    distance = find_distance(objs)
    rand = random.randrange(0, 3)
    image = block_img[rand]
    width = block_options[rand * 2]
    height = block_options[rand * 2 + 1]
    obj.return_self(distance, height, width, image)


# -------------------------COLLISION
def check_collision(blocks):
    for block in blocks:

        if block.y == 418:  # collision conditions for the first and twice
            if jmp_counter == 30:  # no jump
                if block.x <= hero_width - 15 + hero_x <= block.x + 4 + block.width:
                    if health_check():
                        return_obj(blocks, block)
                        return False
                    else:
                        return True
            elif jmp_counter != 30:
                if hero_y + hero_height >= block.y + 19:
                    if block.x <= hero_width - 30 + hero_x <= block.x + 6 + block.width:
                        if health_check():
                            return_obj(blocks, block)
                            return False
                        else:
                            return True
            else:
                if hero_y + hero_height >= block.y + 19:
                    if block.x <= hero_x + 10 <= block.x + block.width:
                        if health_check():
                            return_obj(blocks, block)
                            return False
                        else:
                            return True

        if block.y == 408:  # collision conditions for the third
            if jmp_counter == 30:  # no jump
                if block.x <= hero_width - 17 + hero_x <= block.x + block.width:
                    if health_check():
                        return_obj(blocks, block)
                        return False
                    else:
                        return True
            elif jmp_counter != 30:
                if hero_y + hero_height >= block.y + 20:
                    if block.x <= hero_width - 30 + hero_x <= block.x + 6 + block.width:
                        if health_check():
                            return_obj(blocks, block)
                            return False
                        else:
                            return True
            else:
                if hero_y + hero_height >= block.y + 15:
                    if block.x <= hero_x + 10 <= block.x + block.width:
                        if health_check():
                            return_obj(blocks, block)
                            return False
                        else:
                            return True
    return False


# ------------------ COUNTER SCORE
def counter_score(blocks):
    global score, max_blocks
    check_score = 0

    if -18 <= jmp_counter <= 26:
        for block in blocks:
            if hero_y + hero_height <= block.y:
                if block.x <= hero_x <= block.x + block.width:
                    check_score += 1
                elif block.x <= hero_x + hero_width <= block.x + block.width:
                    check_score += 1
        max_blocks = max(max_blocks, check_score)
    else:
        if jmp_counter == -30:
            score += max_blocks * speed_score
            max_blocks = 0


# ---------------------- FUNCTIONS FOR HEART

# -----------DRAW
def health_draw():
    global health
    counter = 0
    x_health = 60
    while counter != health:
        display.blit(health_image, (x_health, 20))
        x_health += 25
        counter += 1


# ---------CHECK
def health_check():
    global health
    health -= 1
    if health == 0:
        pygame.mixer.Sound.play(lost_sound)
        return False
    else:
        pygame.mixer.Sound.play(bash_sound)
        return True


# ------------PICK
def pick_heart(heart):
    global health, hero_x, hero_y, hero_height, hero_width
    if hero_x <= heart.x <= hero_x + hero_width:
        if hero_y <= heart.y <= hero_y + hero_height:
            pygame.mixer.Sound.play(health_sound)
            if health < 3:
                health += 1

            distance = display_width + random.randrange(1500, 3000)
            heart.return_self(distance, random.randrange(250, 300), hero_width, health_image2)


# ------------------- GAME OVER
def game_over():
    global score, max_score
    stopped = True
    if score > max_score:
        max_score = score
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text("GAME OVER. If you want to restart game press R:(", 140, 250)
        print_text("Press Esc to EXIT.", 140, 290)
        print_text("Max score:" + str(max_score), 140, 100)

        pygame.display.update()
        clock.tick(20)

        key = pygame.key.get_pressed()
        if key[pygame.K_r]:
            lost_sound.stop()
            return True
        if key[pygame.K_ESCAPE]:
            return False


while start_game():
    jump = False
    jmp_counter = 30
    hero_y = display_height - hero_height - 97
    score = 0
    health = 3
pygame.quit()
quit()
