import pygame
import os
# from GameObject import GameObject
# from TextObject import TextObject
# from Tetris import Tetris
import Screens
import config as c

pygame.init()
running = True
pygame.display.set_caption("Hacktrix V1.0")
info = pygame.display.Info()
c.width = info.current_w
c.height = info.current_h
load_screen = 'Main_menu'
if c.screen_mode:
    screen = pygame.display.set_mode((c.width, c.height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((c.width, c.height))

# load screens
Desktop = Screens.Desktop(screen)
SavesMenu = Screens.SavesMenu(screen)
PlayLevel = Screens.PlayLevel(screen)
Text_screen = Screens.Text_screen(screen)
MainMenu = Screens.MainMenu(screen)
# PlayLevel.load_level(os.path.join('levels', '1.txt'))
command = '0'
#pygame.time.set_timer(c.DRAW, 1000 // c.FPS)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if load_screen == 'Main_menu':
            command = MainMenu.run(event)
        elif load_screen == 'Saves_menu':
            command = SavesMenu.run(event)
        elif load_screen == 'Level':
            command = PlayLevel.run(event)
        elif load_screen == 'Desktop':
            command = Desktop.run(event)
        elif load_screen == 'Text':
            command = Text_screen.run(event)

        temp = command.split(';')
        if temp[0] == 'change':
            load_screen = temp[1]
        if temp[0] == 'exit':
            running = False
        if temp[0] == 'load':
            Desktop.set_slot(int(temp[1]))
            Desktop.load()
            load_screen = 'Desktop'
        if temp[0] == 'play':
            PlayLevel.load_level(temp[1])
            load_screen = 'Level'
        if temp[0] == 'Game_over':
            load_screen = 'Text'
            Desktop.load_text(state='lose')
            Text_screen.set_rep_button(True)
            Text_screen.set_next_button(False)
            Text_screen.set_text(Desktop.level_text)
            #Desktop.end_level(end='lose')
        if temp[0] == 'Game_win':
            load_screen = 'Text'
            Text_screen.set_rep_button(True)
            Text_screen.set_next_button(True)
            Desktop.load_text(state='win')
            Text_screen.set_text(Desktop.level_text)
            #Desktop.end_level(end='win')
        if temp[0] == 'next':
            load_screen = 'Desktop'
            Desktop.select_next_level()
        if temp[0] == 'repeat':
            load_screen = 'Desktop'
            Desktop.repeat_level()
        if temp[0] == 'set_text':
            load_screen = 'Text'
            Text_screen.set_text(temp[1])
            try:
                if temp[2] == '01':
                    Text_screen.set_rep_button(False)
                    Text_screen.set_next_button(True)
                if temp[2] == '00':
                    Text_screen.set_rep_button(False)
                    Text_screen.set_next_button(False)
                if temp[2] == '11':
                    Text_screen.set_rep_button(True)
                    Text_screen.set_next_button(True)
                if temp[2] == '10':
                    Text_screen.set_rep_button(True)
                    Text_screen.set_next_button(False)
            except:
                pass
        if temp[0] == 'history':
            load_screen = 'Text'
            file = open(os.path.join('levels', 'start.txt'), encoding='UTF-8')
            Text_screen.set_text(file.readlines()[0])
            file.close()
    pygame.display.flip()
pygame.quit()
