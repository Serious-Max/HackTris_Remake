import GameObject
import TextObject
import config as c
import pygame
import os
from Tools import Button, load_image
import Tetris
import random


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.objects = list()
        self.menu_buttons = list()
        self.mouse_handlers = list()
        self.name = 'Username'
        self.slot = 1
        self.wait = 0
        self.saves = SavesMenu(self.screen)
        self.background = pygame.transform.scale(load_image('main_menu_back.png'), (c.width, c.height))
        for i, (text, handler) in enumerate((('Load Game', self.load),
                                             ('New Game', self.new_game),
                                             # ('Settings', self.settings),
                                             ('Quit', self.quit))):
            b = Button(c.menu_offset_x(),
                       c.menu_offset_y() + (c.menu_button_h() + int((c.height * 5) / 100)) * i,
                       c.menu_button_w(),
                       c.menu_button_h(),
                       text,
                       handler,
                       padding=c.padding())
            self.objects.append(b)
            self.menu_buttons.append(b)
            self.mouse_handlers.append(b.handle_mouse_event)
            self.objects.append(TextObject.TextObject(c.menu_name_x(), c.menu_name_y(), lambda: 'HackTrix',
                                                      c.name_color, c.main_menu_font_name, c.main_menu_font_size))

    def run(self, event):
        self.command = '0'
        if self.wait:
            self.set_slot(event=event)
        else:

            if event.type in [pygame.MOUSEBUTTONDOWN,
                              pygame.MOUSEBUTTONUP,
                              pygame.MOUSEMOTION]:
                for i in self.menu_buttons:
                    i.handle_mouse_event(event.type, event.pos)
            self.draw()
        return self.command

    def draw(self):
        self.fill()
        for i in self.objects:
            i.draw(self.screen)

    def new_game(self, obj, skip=False):
        if not skip:
            self.set_slot()
        if self.wait:
            pass
        else:
            file = open(os.path.join('saves', str(self.slot) + '.txt'), mode='wt')
            file.write(';'.join([self.name, str(0), '0', str(0)]))
            file.close()
            self.command = 'history'

    def quit(self, obj):
        self.command = 'exit'

    def load(self, obj):
        self.command = 'change;Saves_menu'
        # print('load')

    def settings(self, obj):
        pass

    def fill(self):
        #self.screen.blit(self.background, (0, 0))
        self.screen.fill((0, 0, 0))

    def set_slot(self, event=-1):
        if self.wait == 0:
            self.wait = 1
        else:
            command = self.saves.run(event)
            temp = command.split(';')
            if temp[0] == 'load':
                self.slot = int(temp[1])
                self.wait = 0
                self.new_game(0, True)


class SavesMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = list()
        for i, (text, handler) in enumerate((('Slot 1', self.load1),
                                             ('Slot 2', self.load2),
                                             ('Slot 3', self.load3),
                                             ('Slot 4', self.load4),
                                             ('Back', self.back))):
            b = Button(c.save_menu_offset_x(),
                       c.save_menu_offset_y() + (c.save_menu_button_h() + int((c.height * 5) / 100)) * i,
                       c.save_menu_button_w(),
                       c.save_menu_button_h(),
                       text,
                       handler,
                       padding=c.padding())
            self.buttons.append(b)
        self.background = pygame.transform.scale(load_image('main_menu_back.png'), (c.width, c.height))

    def run(self, event):
        self.command = '0'
        if event.type in [pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION]:
            for i in self.buttons:
                i.handle_mouse_event(event.type, event.pos)
        self.draw()
        return self.command

    def draw(self):
        self.fill()
        for i in self.buttons:
            i.draw(self.screen)

    def load1(self, obj):
        self.command = 'load;1'

    def load2(self, obj):
        self.command = 'load;2'

    def load3(self, obj):
        self.command = 'load;3'

    def load4(self, obj):
        self.command = 'load;4'

    def back(self, obj):
        self.command = 'change;Main_menu'

    def fill(self):
        self.screen.blit(self.background, (0, 0))


class Desktop:
    def __init__(self, screen):
        self.screen = screen
        self.slot = 1
        self.skill = 0
        self.buttons = []
        self.level_ready = False
        self.level_text = 'Andrew'
        self.name = 'Username'
        self.state = 'read'
        self.items = dict()
        self.background = pygame.transform.scale(load_image('wallaper1.png'), (c.width, c.height))
        for i, (text, handler) in enumerate((('Mail', self.mail),
                                             ('IDE', self.start_level),
                                             ('Main_menu', self.back))):
            image = None
            if text == 'Mail':
                image = load_image('Mail_icon_1.png', colorkey=None)
            if text == 'Main_menu':
                image = load_image('main_menu.png', colorkey=-1)
            if text == 'IDE':
                image = load_image('IDE.png')
            b = Button(c.mail_button_x(),
                       c.mail_button_y() + (c.desktop_square_button() + int((c.height * 5) / 100)) * i,
                       c.desktop_square_button(),
                       c.desktop_square_button(),
                       text,
                       handler,
                       padding=c.padding(),
                       image=image)
            self.buttons.append(b)

    def run(self, event):
        self.command = '0'
        if event.type in [pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION]:
            for i in self.buttons:
                i.handle_mouse_event(event.type, event.pos)
        self.draw()
        return self.command

    def draw(self):
        self.fill()
        temp = GameObject.GameObject(0, 0, c.toolbar_width(), c.height)
        pygame.draw.rect(self.screen, c.toolbar_color, temp.bounds)
        for i in self.buttons:
            i.draw(self.screen)

    def mail(self, obj):
        if self.state == 'read':
            self.load_text(state='start')
            self.command = 'set_text;' + self.level_text + ';01'
            print(self.level_text)
            self.level_ready = True

    def start_level(self, obj):
        if self.level_ready:
            self.command = 'play;' + os.path.join('levels', str(self.next_level) + '_start' + '.txt')
            self.state = 'play'

    def back(self, obj):
        self.save()
        self.command = 'change;Main_menu'

    def save(self):
        file = open(os.path.join('saves', str(self.slot) + '.txt'), mode='wt', encoding='UTF-8')
        file.write(';'.join([self.name, str(self.money), str(self.next_level), str(self.skill)]))
        file.close()

    def set_slot(self, slot):
        self.slot = slot

    def load(self):
        file = open(os.path.join('saves', str(self.slot) + '.txt'), mode='rt', encoding='UTF-8')
        temp = file.readlines()[0].split(';')
        file.close()
        self.name = temp[0]
        self.money = int(temp[1])
        self.next_level = temp[2]
        self.skill = int(temp[3])

    def fill(self):
        self.screen.blit(self.background, (0, 0))
        # self.screen.fill((0, 0, 0))

    def select_next_level(self):
        if self.state == 'read':
            self.load()
        else:
            print(self.next_level)
            if int(self.next_level) < 2:
                self.next_level = int(self.next_level) + 1
            if self.next_level == 2:
                self.next_level = 31
            if self.next_level == 31:
                self.next_level = 41
            self.save()
            self.level_ready = False
            self.state = 'read'

    def load_text(self, state='start'):
        file = open(os.path.join('levels', str(self.next_level) + '_' + state + '.txt'), encoding='UTF-8')
        self.level_text = file.readlines()[0]
        file.close()

    def repeat_level(self):
        self.save()
        self.level_ready = True
        self.start_level(0)

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1


class PlayLevel:
    def __init__(self, screen):
        self.screen = screen
        self.active_figure = None
        self.figure_poz_x = 5
        self.figure_poz_y = 0
        self.game_run = False
        self.TICK = 2
        self.CHANGE = 3
        self.count = 0
        self.background = [
            pygame.transform.scale(load_image(os.path.join('background', str(i) + '.png')), (c.width, c.height)) for i
            in range(34)]
        if c.low_mode:
            self.low_background = pygame.transform.scale(load_image('nums.png'), (c.width, c.height))
        pygame.time.set_timer(self.TICK, c.sencivity)
        pygame.time.set_timer(self.CHANGE, c.animation_time)

    def run(self, event):
        if event.type == self.CHANGE:
            self.count = (self.count + 1) % 34
        self.command = '0'
        self.fill()
        if self.game_run:
            temp = TextObject.TextObject(c.pause_text_x(), c.pause_text_y(),
                                         lambda: '{}/{}'.format(self.del_lines, self.end),
                                         c.game_font_color, c.game_front_name, c.game_font_size)
            temp.draw(self.screen)
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                self.game_run = False
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                self.game_run = False
                self.game_win = True
            if event.type == pygame.KEYUP and event.key == pygame.K_l:
                self.game_run = False
                self.game_over = True
            if event.type == self.MOVE:
                if self.active_figure:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x, self.figure_poz_y + 1):
                        self.figure_poz_y += 1
                        # print('Move down')
                    else:
                        # print('Crash')
                        self.tetris.add(self.active_figure, self.figure_poz_x, self.figure_poz_y)
                        self.active_figure = None
                        self.figure_poz_y = 0
                        self.figure_poz_x = 5
                        for i in range(self.tetris.ysize):
                            if all(self.tetris.board[i]):
                                self.tetris.del_line(i)
                                self.del_lines += 1
                                if self.del_lines == self.end:
                                    self.game_win = True
                                    self.game_run = False
                else:
                    # print('Generate figure...')
                    # print(self.tetris.board)
                    self.active_figure = self.tetris.figure(random.randint(0, 6), 0)
                    if self.tetris.is_intersection(self.active_figure, self.figure_poz_x, self.figure_poz_y):
                        self.game_over = True
                        self.game_run = False
                    # print(self.tetris.board)
                    # print('Generate figure...OK')
            if self.active_figure and event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                temp = self.tetris.rotate(self.active_figure)
                if not self.tetris.is_intersection(temp, self.figure_poz_x, self.figure_poz_y):
                    self.active_figure = temp
            if event.type == self.TICK and self.active_figure:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x - 1, self.figure_poz_y):
                        self.figure_poz_x -= 1
                if keys[pygame.K_RIGHT]:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x + 1, self.figure_poz_y):
                        self.figure_poz_x += 1
                if keys[pygame.K_DOWN]:
                    if not self.tetris.is_intersection(self.active_figure, self.figure_poz_x, self.figure_poz_y + 1):
                        self.figure_poz_y += 1
        else:
            if self.game_over:
                self.command = 'Game_over'
                self.figure_poz_y = 0
                self.figure_poz_x = 5
                # print('Game_over')
            elif self.game_win:
                self.command = 'Game_win'
                self.figure_poz_y = 0
                self.figure_poz_x = 5
                # print('Game_win')
            else:
                temp = TextObject.TextObject(c.pause_text_x(), c.pause_text_y(), lambda: 'Press P to start',
                                             c.game_font_color, c.game_front_name, c.game_font_size)
                temp.draw(self.screen)
                if event.type == pygame.KEYUP and event.key == pygame.K_p:
                    # print(1)
                    self.game_run = True
        # if event.type == c.DRAW:
        self.draw()
        return self.command

    def draw(self):
        if self.active_figure:
            temp = self.tetris.render(self.active_figure, self.figure_poz_x, self.figure_poz_y)
        else:
            temp = self.tetris.render([0, 0, ''], 0, 0)
        for x in range(self.tetris.xsize):
            for y in range(self.tetris.ysize):
                symb = temp[y][x]
                temp_obj = GameObject.GameObject(c.bowl_x() + x * (c.square_size() + 1),
                                                 c.bowl_y() + y * (c.square_size() + 1), c.square_size(),
                                                 c.square_size())
                if symb:
                    pygame.draw.rect(self.screen, c.square_color, temp_obj.bounds)
                else:
                    pygame.draw.rect(self.screen, c.background_square_color, temp_obj.bounds)

    def fill(self):
        if c.low_mode:
            self.screen.blit(self.low_background, (0, 0))
        else:
            self.screen.blit(self.background[self.count], (0, 0))
        # self.screen.fill((0, 0, 0))

    def load_level(self, level_name):
        print(level_name)
        self.tetris = Tetris.Tetris(10, 20)
        file = open(level_name, mode='rt', encoding='UTF-8')
        temp = file.readlines()
        self.difficult = int(temp[1])
        self.end = int(temp[2])
        self.game_over = False
        self.game_win = False
        file.close()
        self.MOVE = 1
        self.del_lines = 0
        pygame.time.set_timer(self.MOVE, self.difficult)


class Store:
    def __init__(self, screen):
        self.screen = screen
        self.money = 0

    def run(self):
        self.command = '0'
        self.draw()
        return self.command

    def draw(self):
        self.fill()

    def fill(self):
        self.screen.fill((0, 0, 0))

    def set_money(self, money):
        self.money = money


class Text_screen:
    def __init__(self, screen):
        self.screen = screen
        self.text = 'Andrew, add text!'
        self.x = 0
        self.y = 0
        self.repeat_button_active = False
        self.next_button_active = True
        self.buttons = list()
        b = Button(c.text_messange_repeat_x(),
                   c.text_messange_repeat_y(),
                   c.text_messange_repeat_button_w(),
                   c.text_messange_repeat_button_h(),
                   'Repeat',
                   self.repeat,
                   padding=0,
                   image=load_image('repeat.png'))
        self.buttons.append(b)

        b = Button(c.text_messange_next_x(),
                   c.text_messange_next_y(),
                   c.text_messange_next_button_w(),
                   c.text_messange_next_button_h(),
                   'Next',
                   self.next,
                   padding=0,
                   image=load_image('next_button.png', colorkey=None))
        self.buttons.append(b)

    def run(self, event):
        self.command = ''
        if event.type in [pygame.MOUSEBUTTONDOWN,
                          pygame.MOUSEBUTTONUP,
                          pygame.MOUSEMOTION]:

            if self.repeat_button_active:
                self.buttons[0].handle_mouse_event(event.type, event.pos)
            if self.next_button_active:
                self.buttons[1].handle_mouse_event(event.type, event.pos)
        self.draw()
        return self.command

    def draw(self):
        self.fill()
        if self.repeat_button_active:
            self.buttons[0].draw(self.screen)
        if self.next_button_active:
            self.buttons[1].draw(self.screen)
        temp0 = self.lines()
        for i in range(len(temp0)):
            temp = TextObject.TextObject(self.x, self.y + i * c.text_padding(), lambda: temp0[i],
                                         c.text_messange_color, c.text_messange_font, c.text_messange_size)
            temp.draw(self.screen)

    def set_text(self, text):
        self.text = ''
        i = 1
        while i < len(text):
            if text[i] == 'n':
                i += 2
            else:
                self.text += text[i - 1]
                i += 1

    def lines(self):
        out = list()
        temp = len(self.text)
        temp1 = self.text
        while temp > 0:
            # print(temp1)
            if temp >= c.char_in_line():
                # print(1)
                out.append(temp1[0:c.char_in_line()])
                temp1 = temp1[c.char_in_line():]
                temp -= c.char_in_line()
            else:
                # print(2)
                out.append(temp1[0:])
                temp = 0
        return out

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def set_rep_button(self, state):
        self.repeat_button_active = state

    def set_next_button(self, state):
        self.next_button_active = state

    def repeat(self, obj):
        self.command = 'repeat'

    def next(self, obj):
        self.command = 'next'

    def fill(self):
        self.screen.fill((0, 0, 0))
