import pygame
pygame.init()
color_table=pygame.Surface((4096,4096),depth=24)
Surface=pygame.display.set_mode((480,640))
for x in range(4097):
    for y in range(4097):
        r=x%256
        g=y%256
        b=x//256*16+y//256
        y+=1
        color_table.set_at((x,y), (r, g, b))
    x+=1
pygame.image.save(color_table, "color_table.png")