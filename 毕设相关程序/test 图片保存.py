import pygame
pygame.init()
sam=20
lucy=10
color_table=pygame.Surface((20,20),depth=24)
Surface=pygame.display.set_mode((480,640))
n=0
while n<=5:
    for x in range(21):
        for y in range(21):
            r=x%256
            g=y%256
            b=x//256*16+y//256
            y+=1
            color_table.set_at((x,y), (r, g, b))
        x+=1
    pygame.image.save(color_table, str(sam+n)+str(lucy-n)+".png")
    n+=1

