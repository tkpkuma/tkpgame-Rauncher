import pygame


pygame.init()

file_path = "c:\\users\\user\\downloads\\BGM A.wav"
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(75)

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Game Rauncher bytkp')

font = pygame.font.SysFont(None, 48)
text = font.render('Game Rauncher(ver0,02)...', True, (255, 0, 0))
text2 = font.render('created by.tkp', True, (255, 0, 0))
start_time = pygame.time.get_ticks()
logo = pygame.image.load("c:\\Users\\user\\downloads\\tkp Logo.jpg")
background_color = (0, 250, 0)
change_background = False

running = True
while running:    
    screen.fill((0, 0, 0)) 
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    screen.blit(text, (20, 100))
    screen.blit(text2, (20, 600))
    screen.blit(logo, (1000, 500)) 
    pygame.display.update()

    current_time = pygame.time.get_ticks()

    if current_time - start_time >= 10000 and not change_background:
        background_color = (0, 0, 0)
        change_background = True
        text = font.render('select game!', True, (255, 0, 0))
        text2 = font.render('created by.tkp', True, (255, 0, 0))
        pygame.display.update()

        

    
    if current_time - start_time >= 10000:
        new_text = font.render('1_21game(ver1,00)', True, (255, 255, 255))
        pygame.display.update()
        screen.blit(new_text, (20, 140))
        pygame.display.update()   

        
   