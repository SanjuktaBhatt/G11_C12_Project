import pygame
#Import module


pygame.init()
students=["John","Maria","Daniel","Martha","Jason"]
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Project C12")
bgd=pygame.image.load("Assets/bgd.png")
bgd_scaled=pygame.transform.smoothscale(bgd,(400,400))
teacher=pygame.image.load("Assets/Teacher.png")
teacher_scaled=pygame.transform.smoothscale(teacher,(400,400))
carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False 
  screen.fill((0,0,0))
  screen.blit(bgd_scaled,(0,0))
  screen.blit(teacher_scaled,(0,0))
  #display a random name
  
  
  
  
  pygame.time.wait(300)
  pygame.display.flip()
    
pygame.quit()
