import pygame

width = 1300
height = 700
screen_mode = 1
animation_time = 90
low_mode = 0
FPS = 60
DRAW = 4
button_text_color = pygame.Color(255, 255, 255)
button_normal_back_color = pygame.Color(0, 0, 0)
button_hover_back_color = pygame.Color(0, 178, 42)
button_pressed_back_color = pygame.Color('blue')
background_square_color = pygame.Color('grey')
square_color = pygame.Color(0, 178, 42)
name_color = pygame.Color(0, 178, 42)
font_name = 'Times New Roman'
font_size = 24
game_front_name = 'Times New Roman'
game_font_size = 72
main_menu_font_name = 'Times New Roman'
main_menu_font_size = 100
game_font_color = pygame.Color(255, 255, 255)
sencivity = 250
#mail_icon_name = 'Mail_icon_1.png'
toolbar_color = pygame.Color('Grey')
text_messange_font = 'Times New Roman'
text_messange_size = 20
text_messange_color = pygame.Color('Green')


def text_messange_repeat_x():
    return int((width * 10) / 100)


def text_messange_repeat_y():
    return int((height * 80) / 100)


def text_messange_repeat_button_w():
    return int((height * 10) / 100)


def text_messange_repeat_button_h():
    return int((height * 10) / 100)


def text_messange_next_x():
    return int((width * 60) / 100)


def text_messange_next_y():
    return int((height * 80) / 100)


def text_messange_next_button_w():
    return int((width * 30) / 100)


def text_messange_next_button_h():
    return int((height * 10) / 100)


def toolbar_width():
    return 80


def pause_text_x():
    return int((width * 50) / 100)


def pause_text_y():
    return int((height * 50) / 100)


def bowl_x():
    return int((width * 5) / 100)


def bowl_y():
    return int((height * 3) / 100)


def square_size():
    return int((height * 4.5) / 100)


def padding():
    return 10


def text_padding():
    return 20


def menu_offset_x():
    return int((width * 30) / 100)


def menu_offset_y():
    return int((height * 30) / 100)


def menu_button_w():
    return int((width * 40) / 100)


def menu_button_h():
    return int((height * 10) / 100)


def menu_name_x():
    return int((width * 35) / 100)


def menu_name_y():
    return int((height * 5) / 100)


def save_menu_offset_x():
    return int((width * 30) / 100)


def save_menu_offset_y():
    return int((height * 10) / 100)

# def decktop_button():
#    return 10


def save_menu_button_w():
    return int((width * 40) / 100)


def save_menu_button_h():
    return int((height * 10) / 100)


def mail_button_x():
    return 10


def mail_button_y():
    return 10


def desktop_square_button():
    return 64


def char_in_line():
    return width // 10
