import pygame
import os
TANK = [pygame.image.load(os.path.join("Assets/Tank","tank_0.png")),
        pygame.image.load(os.path.join("Assets/Tank","tank_1.png")),
        pygame.image.load(os.path.join("Assets/Tank","tank_2.png")),
        pygame.image.load(os.path.join("Assets/Tank","tank_3.png")),
        pygame.image.load(os.path.join("Assets/Tank","tank_4.png")),
        pygame.image.load(os.path.join("Assets/Tank","tank_5.png")),
        pygame.image.load(os.path.join("Assets/Tank","tank_6.png")),
        pygame.image.load(os.path.join("Assets/Tank","tank_7.png")),
        ]
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),  #tải hoạt ảnh khi run
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
print(TANK[0].get_rect().x-RUNNING[0].get_rect().x)
print(RUNNING[0].get_rect().x)