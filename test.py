import pygame
import os
import random
pygame.init()

# Global Constants
SCREEN_HEIGHT = 600  # chiều cao màn hình
SCREEN_WIDTH = 1100  # chiều ngang màn hình
SCREEN = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))  # đưa màn hình ra
pygame.display.set_caption('BTL_Nhom_12_DEMO')

RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),  # tải hoạt ảnh khi run
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join(
    "Assets/Dino", "DinoJump.png"))  # tải hoạt ảnh khi jump
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]  # tải hoạt ảnh khi ducking

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),  # tải vật cản nhỏ
                pygame.image.load(os.path.join(
                    "Assets/Cactus", "SmallCactus2.png"))
                ]
'''
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),   #tải vật cản lớn
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
'''

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),  # tải hình ảnh vật cản chim
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join(
    "Assets/Other", "Cloud.png"))  # hình ảnh mây
BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))  # background
DINO_0 = pygame.image.load(os.path.join(
    "Assets/Dino", "none.png"))  # style của dino
DINO_1 = pygame.image.load(os.path.join("Assets/Dino", "sword_0.png"))
DINO_2 = pygame.image.load(os.path.join("Assets/Dino", "rifle_0.png"))
DINO_3 = pygame.image.load(os.path.join("Assets/Dino", "grenade_0.png"))
DINO_4 = pygame.image.load(os.path.join("Assets/Dino", "halberd_0.png"))
DINO_5 = pygame.image.load(os.path.join("Assets/Dino", "chainsaw_1.png"))
DINO_6 = pygame.image.load(os.path.join("Assets/Dino", "bow_1.png"))
DINO_7 = pygame.image.load(os.path.join("Assets/Dino", "cig_on_0.png"))
DINO_8 = pygame.image.load(os.path.join("Assets/Dino", "hammer_0.png"))
DINO_9 = pygame.image.load(os.path.join("Assets/Dino", "rifle_1.png"))


DESTROY = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets/Dino", "cacti2_gun_1.png")), (100, 100))

SMDES = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Cactus", "cacti1_gun_0.png")), (100, 100)),  # tải hoạt ảnh khi run
         pygame.transform.scale(pygame.image.load(os.path.join("Assets/Cactus", "cacti2_bat_0.png")), (100, 100))]
LASER = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets/Dino", "flipflop_1.png")), (20, 20))

TANK = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Tank", "tank_0.png")), (200, 200)),
        pygame.transform.scale(pygame.image.load(
            os.path.join("Assets/Tank", "tank_1.png")), (200, 200)),
        pygame.transform.scale(pygame.image.load(
            os.path.join("Assets/Tank", "tank_2.png")), (200, 200)),
        pygame.transform.scale(pygame.image.load(
            os.path.join("Assets/Tank", "tank_3.png")), (200, 200)),
        pygame.transform.scale(pygame.image.load(
            os.path.join("Assets/Tank", "tank_4.png")), (200, 200)),
        pygame.transform.scale(pygame.image.load(
            os.path.join("Assets/Tank", "tank_5.png")), (200, 200)),
        pygame.transform.scale(pygame.image.load(
            os.path.join("Assets/Tank", "tank_6.png")), (200, 200)),
        pygame.transform.scale(pygame.image.load(
            os.path.join("Assets/Tank", "tank_7.png")), (200, 200)),
        ]


class Dinosaur:
    X_POS = 80  # vị trí X của khủng long
    Y_POS = 310  # vị trí Y của khủng long
    Y_POS_DUCK = 340  # vị trí Y khi khủng long duck
    JUMP_VEL = 10  # chỉ số tăng Y khi khủng long jump

    def __init__(self):  # khởi tạo khủng long bất cứ khi nào khủng long được tạo lại
        self.duck_img = DUCKING  # hình ảnh khủng long cúi
        self.run_img = RUNNING  # hình ảnh khủng long chạy
        self.jump_img = JUMPING  # hình ảnh khủng long nhảy
        self.dino_duck = False
        self.dino_run = True  # cài đặt mặc định khủng long running
        self.dino_jump = False
        self.dino_style = DINO_0
        self.step_index = 0  # chỉ số bước chân = 0
        # khởi tạo thuộc tính jump_vel bằng 1 hằng số JUMP_VEL mặc định
        self.jump_vel = self.JUMP_VEL
        # hình ảnh đầu tiên khi con khủng long được chạy
        self.image = self.run_img[0]
        # hình chữ nhật làm khung cảm ứng va chạm cho hình ảnh khủng long
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS  # tọa độ x và y của hình chữ nhật = tọa độ khủng long
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):  # hàm cập nhật khủng long mỗi lần lặp lại vòng while
        if self.dino_duck:  # Kiểm tra trạng thái khủng long
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:  # chỉ số bước mỗi 10 bước thì reset về 0
            self.step_index = 0

        # khi bấm up hoặc Space mà khủng long không jump thì khủng long jump
        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        # khi bấm down mà khủng long không duck thì khủng long duck
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        # nếu không jump hay duck thì run
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
        if userInput[pygame.K_0]:
            self.dino_style = DINO_0
        if userInput[pygame.K_1]:
            # Nếu người chơi bấm phím 1 khủng long sẽ thay đổi style thành DINO1
            self.dino_style = DINO_1
        if userInput[pygame.K_2]:
            # Nếu người chơi bấm phím 2 khủng long sẽ thay đổi style thành DINO2
            self.dino_style = DINO_2
        if userInput[pygame.K_3]:
            # Nếu người chơi bấm phím 3 khủng long sẽ thay đổi style thành DINO3
            self.dino_style = DINO_3
        if userInput[pygame.K_4]:
            # Nếu người chơi bấm phím 4 khủng long sẽ thay đổi style thành DINO4
            self.dino_style = DINO_4
        if userInput[pygame.K_5]:
            # Nếu người chơi bấm phím 5 khủng long sẽ thay đổi style thành DINO5
            self.dino_style = DINO_5
        if userInput[pygame.K_6]:
            # Nếu người chơi bấm phím 6 khủng long sẽ thay đổi style thành DINO6
            self.dino_style = DINO_6
        if userInput[pygame.K_7]:
            # Nếu người chơi bấm phím 7 khủng long sẽ thay đổi style thành DINO7
            self.dino_style = DINO_7
        if userInput[pygame.K_8]:
            # Nếu người chơi bấm phím 8 khủng long sẽ thay đổi style thành DINO8
            self.dino_style = DINO_8
        if userInput[pygame.K_a] and self.dino_style == DINO_2 and self.dino_jump == False:
            self.dino_style = DINO_9
            global oke
            oke = True

    def duck(self):
        # hình ảnh tương ứng của khủng long(khi số bước chân tứ 0 - 5 hình ảnh 1 hiển thị , từ 5 -10 hình ảnh 2 hiển thị vượt quá 10 chỉ số được đặt lại)
        self.image = self.duck_img[self.step_index // 5]
        # tọa độ hình chữ nhật của hình ảnh khủng long
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS  # đặt hình chữ nhật vào vị trí khủng long hiển thị
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1  # tăng chỉ số bước chân lên 1

    def run(self):
        # hình ảnh tương ứng của khủng long(khi số bước chân tứ 0 - 5 hình ảnh 1 hiển thị , từ 5 -10 hình ảnh 2 hiển thị vượt quá 10 chỉ số được đặt lại)
        self.image = self.run_img[self.step_index // 5]
        # tọa độ hình chữ nhật của hình ảnh khủng long
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80  # đặt hình chữ nhật vào vị trí khủng long hiển thị
        self.dino_rect.y = 310
        self.step_index += 1  # tăng chỉ số bước chân lên 1

    def jump(self):
        self.image = self.jump_img  # thay đổi hình ảnh của khủng long
        if self.dino_jump:  # nếu trạng thái nhảy của khủng long được kích hoạt
            # tọa độ y của khủng long sẽ thay đổi dựa vào chỉ số jump_vel
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8  # Giảm dần chỉ số jump_vel để hạ độ cao dần
        if self.jump_vel < - self.JUMP_VEL:  # Khi khủng long trở về vị trí ban đầu trước lúc jump
            self.dino_jump = False         # trạng thái Jump được tắt
            self.jump_vel = self.JUMP_VEL  # cài đặt lại thuộc tính jump_vel về ban đầu

    def draw(self, SCREEN):  # hàm vẽ lên màn hình
        # Vẽ hình ảnh của khủng long lên màn hình game
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        if (self.dino_style == DINO_1):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        30, self.dino_rect.y-180))  # dino 1
        elif (self.dino_style == DINO_2):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        20, self.dino_rect.y-180))  # dino 2
        elif (self.dino_style == DINO_3):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        40, self.dino_rect.y-180))  # dino 3
        elif (self.dino_style == DINO_4):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        40, self.dino_rect.y-180))  # dino 4
        elif (self.dino_style == DINO_5):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        40, self.dino_rect.y-170))  # dino 5
        elif (self.dino_style == DINO_6):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        20, self.dino_rect.y-170))  # dino 6
        elif (self.dino_style == DINO_7):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        25, self.dino_rect.y-160))  # dino 7
        elif (self.dino_style == DINO_8):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        45, self.dino_rect.y-170))  # dino 8
        elif (self.dino_style == DINO_9):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        30, self.dino_rect.y-180))  # dino 9
            self.dino_style = DINO_2
            SCREEN.blit(self.dino_style,
                        (self.dino_rect.x-20, self.dino_rect.y-180))
        elif (self.dino_style == DINO_0):
            SCREEN.blit(self.dino_style, (self.dino_rect.x -
                        45, self.dino_rect.y-170))  # dino 0


class Laser:
    def __init__(self):
        self.image = LASER
        self.rect = self.image.get_rect()
        self.rect.x = 200

    def update(self):
        self.rect.x += game_speed

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, 350))


def check(obj1, obj2):
    if obj1.rect.x - obj2.rect.x <= 10:
        return True
    return False


class Cloud:  # vẽ mây
    def __init__(self):
        # + random.randint(800, 1000)  #vị trí x của mây = độ rộng của màn hình + random(800 -> 1000)
        self.x = SCREEN_WIDTH
        # vịt trí y của mây = random(50 -> 100)
        self.y = random.randint(50, 100)
        self.image = CLOUD  # hình ảnh mây
        self.width = self.image.get_width()     # độ rộng của mây

    def update(self):
        self.x -= game_speed  # vị trí x của mây trừ theo tốc độ của game
        if self.x < -self.width:  # khi mây vượt khỏi màn hình thì tạo lại mây
            self.x = SCREEN_WIDTH  # + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):  # vẽ mây lên màn hình
        SCREEN.blit(self.image, (self.x, self.y))


class Destroy:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def set(self, s):
        self.rect.x = s

    def sety(self, s):
        self.rect.y = s

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            dt.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], (self.rect.x, self.rect.y-15))


class Obstacle:  # vật cản
    def __init__(self, image, type):
        self.image = image  # hình ảnh
        self.type = type  # loại vật cản
        # tọa độ hình chữ nhật của vật cản
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH  # tọa độ vật cản = độ ngang màn hình

    def update(self):  # di chuyển chướng ngại vật trên màn hình
        self.rect.x -= game_speed  # giảm tọa độ x của vật cản bằng tốc độ game
        if self.rect.x < -self.rect.width:  # nếu x ra khỏi màn hình thì loại bỏ
            obstacles.pop()
            if len(ob) != 0:
                ob.pop()

    def getx(self):
        return self.rect.x

    def gety(self):
        return self.rect.y

    def gett(self):
        return self.type

    def draw(self, SCREEN):  # vẽ vật cản lên màn hình
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):  # xương rồng nhở
        self.type = random.randint(0, 1)  # chọn ngẫu nhiên 1 trong 3 loại
        super().__init__(image, self.type)  # đưa về lớp cha
        self.rect.y = 325


class Bird(Obstacle):  # chim cũng kế thừa từ lớp obstacle
    def __init__(self, image):
        self.type = 0  # có 1 loại chim nên đặt là 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(250, 300)  # tọa độ y con chim sẽ bay
        self.index = 0  # chỉ mục để tạo hoạt ảnh

    def draw(self, SCREEN):
        if self.index >= 9:  # nếu chỉ mục lớn hơn 9 thì reset về 0
            self.index = 0
        # từ 0 - 4 chim dùng 1 hình , từ 5 - 9 chim dùng 1 hình
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1  # tăng chỉ số lên 1


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, ob, dt, ls, ls1
    global oke
    oke = False
    dem = 0
    run = True  # công tắc cho vòng lặp
    clock = pygame.time.Clock()  # đồng hồ cho trò chơi
    player = Dinosaur()
    cloud = Cloud()
    laser = Laser()
    game_speed = 15  # tốc độ ban đầu
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0  # điểm ban đầu 0
    font = pygame.font.Font('freesansbold.ttf', 20)  # font cho chữ score
    obstacles = []
    death_count = 0  # số lần chết = 0
    ob = []
    dt = []
    ls = []
    ls1 = []
    help = []

    def dino2(a): # in ra số đạn trên màn hình
        text = font.render('Bullet '+str(21-a), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 70)
        SCREEN.blit(text, textRect)

    def score():
        global points, game_speed
        points += 1  # cộng 1 point theo tg
        if points % 100 == 0:
            game_speed += 1  # mỗi 100 point thì tăng tốc gốc

        text = font.render("Points: " + str(points), True,
                           (0, 0, 0))  # text sẽ in ra point và điểm
        textRect = text.get_rect()  # lấy hình chữ nhật để bao quanh score
        textRect.center = (1000, 40)  # vị trí của score
        SCREEN.blit(text, textRect)  # vẽ point lên màn hình

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()  # chiều dài image = độ dài bg
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))  # vẽ background lên màn hình
        # vẽ nối thêm 1 backgroud nữa
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:  # khi bg chạy quá gần hết màn hình thì vẽ lại
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed  # vị trí của backgroud giảm dần theo game_speed
    sti = 0
    while run:
        if dem == 5:
            dem = 0
        oke = False
        for event in pygame.event.get():  # dấu X thoát trò chơi
            if event.type == pygame.QUIT:  # Khi người chơi click vào dấu x vòng lặp sẽ dừng
                run = False

        SCREEN.fill((255, 255, 255))  # tô màu màn hình thành màu trắng
        userInput = pygame.key.get_pressed()  # biến đầu vào người dùng
        if userInput[pygame.K_h]:
            if len(help) == 0:
                help.append(1)

        if len(help) == 1:
            if sti == 7:
                SCREEN.blit(TANK[6], (80, 200))
            else:
                SCREEN.blit(TANK[sti], (80, 200))
                sti = sti + 1

        if len(help) == 1:
            if len(obstacles) > 0:
                td1 = obstacles[0].rect.x
                td2 = TANK[0].get_rect().x
                if abs(td2-td1) <= 200:
                    obstacles = []
                    ob = []
                    help = []
                    player.dino_style = DINO_0

        if userInput[pygame.K_q]:
            if len(help) == 1:
                help = []
        if len(help) == 0:
            player.draw(SCREEN)  # vẽ lên màn hình
            # cập nhật khủng long với mỗi sự kiện tương tác của người chơi
            player.update(userInput)

        if player.dino_style == DINO_2:
            dino2(len(ls1))
        if len(ls1) == 21 and player.dino_style == DINO_2:
            player.dino_style = DINO_0

        if len(dt) == 0:
            # tạo ngẫu nhiên 1 chim hoặc 1 xương rồng nếu độ dài của list vật cản = rỗng
            if len(obstacles) == 0:
                if random.randint(0, 1) == 0:
                    obstacles.append(SmallCactus(SMALL_CACTUS))
                    ob.append(1)
                elif random.randint(0, 1) == 1:
                    obstacles.append(Bird(BIRD))

        s1 = 0
        s2 = 0
        ty = 0
        laser = Laser()
        if oke == True and player.dino_jump == False:
            if dem == 0:
                if len(ls1) <= 20:
                    ls.append(laser)
                    ls1.append(1)
            dem = dem + 1

        if len(dt) > 0:
            for dts in dt:
                dts.draw(SCREEN)
                dts.update()
        if len(obstacles) > 0:
            for obstacle in obstacles:  # lấy ra vật cản để vẽ và update
                obstacle.draw(SCREEN)
                obstacle.update()
                # câu lệnh thể hiện va chạm
                if player.dino_rect.colliderect(obstacle.rect) and len(help) == 0:
                    # sau khi va chạm thì chờ để hiện menu
                    pygame.time.delay(100)
                    death_count += 1  # va chạm death +1
                    menu(death_count)
        if len(ls) > 0: # bắn ra đạn
            for i in ls:
                if i.rect.x < SCREEN_WIDTH:
                    i.draw(SCREEN)
                    i.update()
                    if len(obstacles) != 0 and len(ob) != 0:
                        if check(obstacles[0], i) == True: # đụng phải vật cản
                            s1 = obstacles[0].getx()
                            s2 = obstacles[0].gety()
                            ty = obstacles[0].gett()
                            obstacles = []
                            ob = []
                            ls.pop()
                            if len(dt) == 0: # set vật bị phá hủy
                                destr = Destroy(SMDES, ty)
                                destr.set(s1)
                                destr.sety(s2)
                                dt.append(destr)

        background()
        #print(oke)
        cloud.draw(SCREEN)  # vẽ mây
        cloud.update()

        score()

        clock.tick(40)  # cài đặt fps
        pygame.display.update()  # đưa lên màn hình


def menu(death_count):
    global points  # lấy point
    run = True
    while run:
        SCREEN.fill((255, 255, 255))  # nền trắng
        font = pygame.font.Font('freesansbold.ttf', 30)  # font chữ

        if death_count == 0:  # số lần chết = 0 thì bấm để bắt đầu
            text = font.render(
                "Press any Key to Start and Press 0-8 to choose style", True, (0, 0, 0))
        elif death_count > 0:
            # số lần chết lớn hơn 0 in bấm để chơi lại
            text = font.render(
                "Press any Key to Restart and Press 0-8 to choose style", True, (0, 0, 0))
            # in ra số điểm đã đạt được
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            # vị trí của score
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)  # vẽ score lên màn hình
        textRect = text.get_rect()
        # vị trí của text
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)  # vẽ text lên màn hình
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 -
                    20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():  # nếu bấm nút thoát thì sẽ out game
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:  # bấm nút thì tiếp tục choi
                main()
    pygame.quit()


menu(death_count=0)
