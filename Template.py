import pygame
# Import random module
import 

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
  
  # Select the font size 
  font = pygame.font.Font(None,     )
  
  # Call the choice() function from random module 
  text = font.render(                (students), 1, (0,0,0))
  
  # Display the randomly chosen name at (130, 50) 
  screen.blit(text, (         ))
 
  pygame.time.wait(300)
  pygame.display.flip()
    
pygame.quit()
