import pygame   #dùng thư viện pygame
pygame.init()   #khởi tạo thư viện

running=True
WHITE =(255,255,255)
GREY=(214,214,214)
BLACK=(0,0,0)
PANEL=(249,255,230)
font=pygame.font.SysFont('sans', 40)
daucong=font.render('+',True, WHITE)
screen=pygame.display.set_mode((1200,700))
while running:
    screen.fill(GREY)
    pygame.draw.rect(screen, BLACK, (50,50, 700,500))
    pygame.draw.rect(screen, PANEL, (55,55, 690,490))
    pygame.draw.rect(screen, BLACK, (800,50, 50,50))
    screen.blit(daucong, (810,52))
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip() #cập nhật thay đổi màn hình
pygame.quit()


                           
                        
                           
