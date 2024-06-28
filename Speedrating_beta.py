'''beta'''
import pygame
from pygame.locals import *
import keyboard
import json
pygame.init()
clock=pygame.time.Clock()#fps
pygame.display.set_caption('Speedrating beta')
screen=pygame.display.set_mode((400,500),pygame.SRCALPHA)
surface=pygame.Surface((400,500),pygame.SRCALPHA)
icon_surface=pygame.image.load('icon2.png')
pygame.display.set_icon(icon_surface)
font = pygame.font.Font(None, 30)
font_record=pygame.font.Font(None, 27)
font_button=pygame.font.Font(None,36)
font_home_button=pygame.font.Font(None,18)
font2=pygame.font.Font(None,20)
font3=pygame.font.Font(None,45)

def print_text(screen, font, x, y, text, fcolor=(124,3,254)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))
def print_text_button(screen, font, x, y, text, fcolor=(255,255,254)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))
def print_text_button2(screen, font, x, y, text, fcolor=(0,0,0)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))
def print_text_record(screen, font, x, y, text, fcolor=(255,255,255)):
    imgText = font.render(text, True, fcolor,(0,0,0))
    screen.blit(imgText, (x, y))

def time(a):
    new_new_list = a
    formatted_new_new_list="{:6.3f}".format(new_new_list)#Specify the number of decimal places
    new_new_list2 = formatted_new_new_list[:-6]
    new_new_list3 = formatted_new_new_list[-6:]
    return f"{new_new_list2}:{new_new_list3}"
def on_key_event(event):
    input_text += str(event.name)

mainrunning=True


''''''
while mainrunning:
    scan = 0
    scan2 = 0
    line = 0
    ranking_number = 0
    car_chose_number = 0
    map_chose_number=0
    point = [120, 100]
    fr = open('car_list.txt', 'r+')
    car_list = eval(fr.read())
    print(car_list)
    frr=open('map_list.txt','r+')
    map_list=eval(frr.read())

    #map_list = ['Goliath', 'us']
    # car_list=['Quadra V-Tech',"Ford Mustang'71"]

    input_text = ''
    input_text_new_car = ""
    after_click_carlist = False
    after_click_carlist1 = False

    if False:
        print("kkoo")
        keyboard.on_press(on_key_event)
        keyboard.on_release(on_key_event)
        keyboard.wait('esc')
        keyboard.unhook_all()

    tips = 0
    running = True
    test = False
    click = False
    after_click_checkrecord = False
    after_click_map1 = False
    last_box = True
    after_click = False
    after_click_adding = False
    after_click_settings = False
    after_click_maplist0 = False
    add_possess = False
    add_map = False
    add_car = False
    add_possess_car = False
    add_possess_map=False
    delete=False

    add_car_box = pygame.Rect(point[0], point[1] + 50, 160, 38)
    add_map_box = pygame.Rect(point[0], point[1] + 120, 160, 38)
    ok_box = pygame.Rect(point[0] + 60, point[1] + 160, 160 - 110, 30)
    inside_box = pygame.Rect(120 + 8, 100 + 8, 160 - 10, 38 - 10)
    record_box = pygame.Rect(50, 40, 300, 410)
    record_box_side = pygame.Rect(50, 40, 300, 410)
    bri_adding_box = pygame.Rect(point[0], point[1] + 40, 160, 38)
    carname_box = pygame.Rect(point[0], point[1] + 50, 175, 38)
    input_record_box = (point[0] - 20, point[1] + 60, 160 + 60, 38)
    box_sape = pygame.Rect(point[0], point[1] + 30, 160, 38)
    box_sape2 = pygame.Rect(point[0], point[1] + 210, 160, 38)
    home_box= pygame.Rect(10, 10, 38, 38)
    ranking_box1=pygame.Rect(120 - 65, 100 + 13 - 58 , 290, 20)
    ranking_box2 = pygame.Rect(120 - 65, 100 + 13 - 58+30, 290, 20)
    ranking_box3 = pygame.Rect(120 - 65, 100 + 13 - 58+60, 290, 20)
    ranking_box4 = pygame.Rect(120 - 65, 100 + 13 - 58+90, 290, 20)
    ranking_box5 = pygame.Rect(120 - 65, 100 + 13 - 58+120, 290, 20)
    ranking_box6 = pygame.Rect(120 - 65, 100 + 13 - 58+150, 290, 20)
    ranking_box7 = pygame.Rect(120 - 65, 100 + 13 - 58+180, 290, 20)
    ranking_box8 = pygame.Rect(120 - 65, 100 + 13 - 58+210, 290, 20)
    ranking_box9 = pygame.Rect(120 - 65, 100 + 13 - 58+240, 290, 20)
    ranking_box10 = pygame.Rect(120 - 65, 100 + 13 - 58+270, 290, 20)
    ranking_box11 = pygame.Rect(120 - 65, 100 + 13 - 58+300, 290, 20)
    ranking_box12 = pygame.Rect(120 - 65, 100 + 13 - 58+330, 290, 20)
    ranking_box13 = pygame.Rect(120 - 65, 100 + 13 - 58+360, 290, 20)

    '''running'''
    while running:

        clock.tick(60)
        screen.fill([64, 64, 64])
        image = pygame.image.load('image.jfif')
        screen.blit(image,(0,0))
        fr = open(f'{map_list[map_chose_number]}_new_list.txt', 'r+')
        new_list = eval(fr.read())
        if True:
            #print_text(screen, font, 15, 86, f'carnumber:{car_chose_number}')
            #print_text(screen, font, 15, 66, f'mapnumber:{map_chose_number}')
            #home button
            pygame.draw.rect(screen, (0, 0, 0), home_box, 0)
            print_text_button(screen, font_home_button,  10, 37, "HOME")
            print_text_button(screen, font_home_button, 10, 10, "Esc")
        # show button
        if not after_click:
            # check button
            box = pygame.Rect(point[0], point[1], 160, 38)
            pygame.draw.rect(screen, (0, 0, 0), box, 0)
            print_text_button(screen, font_button, 120 + 10, 100 + 13, "check record")
            # adding button
            box_adding = pygame.Rect(point[0], point[1] + 90, 160, 38)
            pygame.draw.rect(screen, (0, 0, 0), box_adding, 0)
            print_text_button(screen, font_button, point[0] + 77, point[1] + 13 + 90, "adding")
            # settings button
            box_settings = pygame.Rect(point[0], point[1] + 180, 160, 38)
            pygame.draw.rect(screen, (0, 0, 0), box_settings, 0)
            print_text_button(screen, font_button, point[0] + 60, point[1] + 13 + 180, "settings")

        # print(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYUP:
                if not event.key==pygame.K_BACKSPACE:
                    if len(input_text)==2:
                        input_text+=':'
                    if len(input_text)==5:
                        input_text+='.'
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key==pygame.K_BACKSPACE:
                    input_text_new_car=input_text_new_car[:-1]
                    input_text=input_text[:-1]

                #car or map is inputed
                if add_car or add_map:
                    if not event.key==pygame.K_BACKSPACE:
                        print('yes')
                        letter_and_other = chr(event.key)
                        input_text_new_car += letter_and_other
                #record is inputed
                elif event.type == pygame.KEYDOWN and not event.key==pygame.K_BACKSPACE:
                    input_text += event.unicode

                elif event.type == pygame.KEYUP:
                    # print(f"key{event.key}released")
                    pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 4:
                    #print_text(screen, font, 22, 66, 'up')
                    if not scan2==0 and after_click_map1:
                        scan2 -= 1
                        ranking_number -= 1
                    if not car_chose_number == 0 and not after_click_carlist and after_click_maplist0:
                        car_chose_number -= 1
                    if not map_chose_number == 0 and not after_click_maplist0 and not after_click_map1:
                        map_chose_number -= 1

                if event.button == 5:
                   # print_text(screen, font, 22, 66, 'down')
                    if after_click_map1:
                        scan2 += 1
                        ranking_number += 1
                    if car_chose_number < len(car_list) - 1 and not after_click_carlist and after_click_maplist0:
                        car_chose_number += 1
                    if map_chose_number < len(map_list) - 1 and not after_click_maplist0 and not after_click_map1:
                        map_chose_number += 1

                if event.button == 1:
                    #print_text(screen, font, 22, 66, 'click')

                    tips += 1
                    #print_text(screen, font, 22, 86, f'pos{tips}')
                    click = True
            if event.type == MOUSEBUTTONUP:
                click = False
                last_box = False
        '''MAIN button #1'''
        if not after_click_adding and not after_click_settings:
            if box.collidepoint(pygame.mouse.get_pos()):
                # print('yes')
                #print_text(screen, font, 22, 66, 'pos')
                # print('tips',tips)
                if not after_click:
                    #pygame.draw.rect(screen, (255, 255, 255), inside_box, 0)
                    box = pygame.Rect(point[0], point[1], 160, 38)
                    pygame.draw.rect(screen, (105,105,105,118), box, 0)
                    print_text_button(screen, font_button, 120 + 10, 100 + 13, "check record",fcolor=(255,255,255))
                    #print_text_button2(screen, font_button, 120 + 10, 100 + 13, "check record")
                if click:
                    after_click_checkrecord = True
                    after_click = True

        ''' MAIN button #2'''
        if not after_click_checkrecord and not after_click_settings:
            if box_adding.collidepoint(pygame.mouse.get_pos()):

                if not after_click:
                    #pygame.draw.rect(screen, (255, 255, 255), inside_box2, 0)
                    box_adding = pygame.Rect(point[0], point[1] + 90, 160, 38)
                    pygame.draw.rect(screen, (105, 105, 105, 118), box_adding, 0)
                    print_text_button(screen, font_button, point[0] + 77, point[1] + 13 + 90, "adding",fcolor=(255,255,255))
                if click:
                    after_click = True
                    after_click_adding = True
        ''' MAIN button #3'''
        if not after_click_checkrecord and not after_click_adding:
            if box_settings.collidepoint(pygame.mouse.get_pos()):
                if not after_click_settings:
                    box_settings = pygame.Rect(point[0], point[1] + 180, 160, 38)
                    pygame.draw.rect(screen, (105, 105, 105, 118), box_settings, 0)
                    print_text_button(screen, font_button, point[0] + 60, point[1] + 13 + 180, "settings",fcolor=(255,255,255))

                if click:
                        after_click = True
                        after_click_settings = True

        '''// MAIN button #1'''
        if after_click_checkrecord:
            if not after_click_map1:
                print_text(screen, font3, 120 - 90, 100 , 'M-A-P-S: ')
                print_text(screen, font2, 120 - 0, 100+30, ' sliding the mouse wheel')
                carname_box2 = pygame.Rect(point[0] - 48, point[1] + 60, 257, 52)
                pygame.draw.rect(screen, (0, 0, 0), carname_box2, 0)
                print_text_button(screen, font, 120 - 40, 100 + 80, f"{map_list[map_chose_number]}")
                if carname_box2.collidepoint(pygame.mouse.get_pos()):
                    carname_box2 = pygame.Rect(point[0] - 48, point[1] + 60, 257, 52)
                    pygame.draw.rect(screen, (105, 105, 105, 118), carname_box2, 0)
                    print_text_button(screen, font, 120 - 40, 100 + 80, f"{map_list[map_chose_number]}",fcolor=(255,255,255))
                    if click:
                        after_click_map1 = True
        if after_click_map1 and tips > 1:
            pygame.draw.rect(surface, (64, 64, 64,178), record_box)
            screen.blit(surface,(0,0))
            pygame.draw.rect(screen, (0, 0, 0), record_box_side, 5)

            # print(new_list)
            new_list.sort(key=lambda x: x[1])
            #record list
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58,
                                  f'{1 + ranking_number}:  'f"{new_list[0 + scan2][0]}---{time(new_list[0 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box1, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 ,
                                      f'{1+ranking_number}:  'f"{new_list[0+scan2][0]}---{time(new_list[0+scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 30,
                                  f'{2 + ranking_number}:  'f"{new_list[1 + scan2][0]}---{time(new_list[1 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box2, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58+30,
                                  f'{2 + ranking_number}:  'f"{new_list[1 + scan2][0]}---{time(new_list[1 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 60,
                                  f'{3 + ranking_number}:  'f"{new_list[2 + scan2][0]}---{time(new_list[2 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box3, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 60,
                                  f'{3 + ranking_number}:  'f"{new_list[2 + scan2][0]}---{time(new_list[2 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 90,
                                  f'{4 + ranking_number}:  'f"{new_list[3 + scan2][0]}---{time(new_list[3 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box4, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 90,
                                  f'{4 + ranking_number}:  'f"{new_list[3 + scan2][0]}---{time(new_list[3 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 120,
                                  f'{5 + ranking_number}:  'f"{new_list[4 + scan2][0]}---{time(new_list[4 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box5, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 120,
                                  f'{5 + ranking_number}:  'f"{new_list[4 + scan2][0]}---{time(new_list[4 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 150,
                                  f'{6 + ranking_number}:  'f"{new_list[5 + scan2][0]}---{time(new_list[5 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box6, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 150,
                                  f'{6 + ranking_number}:  'f"{new_list[5 + scan2][0]}---{time(new_list[5 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 180,
                                  f'{7 + ranking_number}:  'f"{new_list[6 + scan2][0]}---{time(new_list[6 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box7, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 180,
                                  f'{7 + ranking_number}:  'f"{new_list[6 + scan2][0]}---{time(new_list[6 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 210,
                                  f'{8 + ranking_number}:  'f"{new_list[7 + scan2][0]}---{time(new_list[7 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box8, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 210,
                                  f'{8 + ranking_number}:  'f"{new_list[7 + scan2][0]}---{time(new_list[7 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 240,
                                  f'{9 + ranking_number}:  'f"{new_list[8 + scan2][0]}---{time(new_list[8 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box9, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 240,
                                  f'{9 + ranking_number}:  'f"{new_list[8 + scan2][0]}---{time(new_list[8 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 270,
                                  f'{10 + ranking_number}:  'f"{new_list[9 + scan2][0]}---{time(new_list[9 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box10, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 270,
                                  f'{10 + ranking_number}:  'f"{new_list[9 + scan2][0]}---{time(new_list[9 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 300,
                                  f'{11 + ranking_number}:  'f"{new_list[10 + scan2][0]}---{time(new_list[10 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box11, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 300,
                                  f'{11 + ranking_number}:  'f"{new_list[10 + scan2][0]}---{time(new_list[10 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 330,
                                  f'{12 + ranking_number}:  'f"{new_list[11 + scan2][0]}---{time(new_list[11 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box12, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 330,
                                  f'{12 + ranking_number}:  'f"{new_list[11 + scan2][0]}---{time(new_list[11 + scan2][1])}")
            except:
                pass
            try:
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 360,
                                  f'{13 + ranking_number}:  'f"{new_list[12 + scan2][0]}---{time(new_list[12 + scan2][1])}")
                pygame.draw.rect(screen, (0, 0, 0), ranking_box13, 0)
                print_text_record(screen, font_record, 120 - 65, 100 + 13 - 58 + 360,
                                  f'{13 + ranking_number}:  'f"{new_list[12 + scan2][0]}---{time(new_list[12 + scan2][1])}")
            except:
                pass

        '''// MAIN button #2'''
        if after_click_adding:
            if not after_click_maplist0:
                print_text(screen, font3, 120 - 90, 100, 'M-A-P-S: ')
                print_text(screen, font2, 120 - 0, 100 + 30, ' sliding the mouse wheel')
                carname_box2 = pygame.Rect(point[0] - 48, point[1] + 60, 257, 52)
                pygame.draw.rect(screen, (0, 0, 0), carname_box2, 0)
                print_text_button(screen, font, 120 - 40, 100 + 80, f"{map_list[map_chose_number]}")

            if carname_box2.collidepoint(pygame.mouse.get_pos()):
                if not after_click_maplist0:
                    carname_box2 = pygame.Rect(point[0] - 48, point[1] + 60, 257, 52)
                    pygame.draw.rect(screen, (105, 105, 105, 118), carname_box2, 0)
                    print_text_button(screen, font, 120 - 40, 100 + 80, f"{map_list[map_chose_number]}",
                                      fcolor=(255, 255, 255))
                if click and tips>1:
                    after_click_maplist0 = True
            if after_click_maplist0:
                if not after_click_carlist and not after_click_carlist1 and not after_click_checkrecord:
                    print_text(screen, font3, 120 - 90, 100, 'C-A-R-S: ')
                    print_text(screen, font2, 120 - 0, 100 + 30, ' sliding the mouse wheel')
                    #pygame.draw.rect(screen, (64, 64, 64), box_sape, 0)
                    carname_box2 = pygame.Rect(point[0] - 48, point[1] + 60, 257, 52)
                    pygame.draw.rect(screen, (0, 0, 0), carname_box2, 0)
                    print_text_button(screen, font, 120 - 40, 100 + 80, f"{car_list[car_chose_number]}")
                    #pygame.draw.rect(screen, (64, 64, 64), box_sape2, 0)
                if carname_box2.collidepoint(pygame.mouse.get_pos()):
                    if not after_click_carlist and not after_click_carlist1 and not after_click_checkrecord:
                        #print_text(screen, font, 15, 66, 'carlist')
                        carname_box2 = pygame.Rect(point[0] - 48, point[1] + 60, 257, 52)
                        pygame.draw.rect(screen, (105, 105, 105, 118), carname_box2, 0)
                        print_text_button(screen, font, 120 - 40, 100 + 80, f"{car_list[car_chose_number]}",
                                          fcolor=(255, 255, 255))
                    if click and tips > 2:
                        after_click_carlist = True
            if after_click_carlist or after_click_carlist1:
                if not after_click_checkrecord:
                    input_record_box = (point[0]-20, point[1] + 60, 160 + 60, 38)
                    pygame.draw.rect(screen, (0, 0, 0), input_record_box, 0)
                    print_text_button(screen, font, 120 - 10, 100 + 80, f"Record {input_text}")

                    pygame.draw.rect(screen, (0, 0, 0), ok_box, 0)
                    print_text_button(screen, font, 120 + 70, 100 + 170, f"OK")
                if ok_box.collidepoint(pygame.mouse.get_pos()):
                    if not after_click_checkrecord:
                        #print_text(screen, font, 22, 66, 'ok')
                        pygame.draw.rect(screen, (105, 105, 105, 118), ok_box, 0)
                        print_text_button(screen, font, 120 + 70, 100 + 170, f"OK", fcolor=(255, 255, 255))
                    if click and tips > 3:
                        add_possess = True

                        running = False

        '''// MAIN button #3'''
        if after_click_settings:
            if not add_map and not add_car and not after_click_checkrecord and not after_click_adding:
                add_car_box = pygame.Rect(point[0], point[1] + 50, 160, 38)
                pygame.draw.rect(screen, (0, 0, 0), add_car_box, 0)
                print_text_button(screen, font_button, point[0], point[1] + 50, 'add car')

                pygame.draw.rect(screen, (0, 0, 0), add_map_box, 0)
                print_text_button(screen, font_button, point[0], point[1] + 120, 'add map')
            if not add_map and not add_car and not after_click_checkrecord and not after_click_adding:
                if add_map_box.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, (105, 105, 105, 118), add_map_box, 0)
                    print_text_button(screen, font_button, point[0], point[1] + 120, 'add map',fcolor=(255, 255, 255))
                    if click:
                        add_map = True
            if not add_car and not add_map and not after_click_checkrecord and not after_click_adding:
                if add_car_box.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, (105, 105, 105, 118), add_car_box, 0)
                    print_text_button(screen, font_button, point[0], point[1] + 50, 'add car',fcolor=(255, 255, 255))
                    if click:
                        add_car = True
            if add_car:
                if not after_click_checkrecord and not after_click_adding :
                    pygame.draw.rect(screen, (0, 0, 0), input_record_box, 0)
                    print_text_button(screen, font, 120 - 10, 100 + 80, f"New car:{input_text_new_car}")
                    pygame.draw.rect(screen, (0, 0, 0), ok_box, 0)
                    print_text_button(screen, font, 120 + 70, 100 + 170, f"OK")
                if ok_box.collidepoint(pygame.mouse.get_pos()):
                    #print_text(screen, font, 22, 66, 'ok')
                    pygame.draw.rect(screen, (105, 105, 105, 118), ok_box, 0)
                    print_text_button(screen, font, 120 + 70, 100 + 170, f"OK", fcolor=(255, 255, 255))
                    if click and tips > 2:
                        add_possess_car = True
                        running = False
            if add_map:
                if not after_click_checkrecord and not after_click_adding:
                    pygame.draw.rect(screen, (0, 0, 0), input_record_box, 0)
                    print_text_button(screen, font, 120 - 10, 100 + 80, f"New map:{input_text_new_car}")
                    pygame.draw.rect(screen, (0, 0, 0), ok_box, 0)
                    print_text_button(screen, font, 120 + 70, 100 + 170, f"OK")
                if ok_box.collidepoint(pygame.mouse.get_pos()):
                    #print_text(screen, font, 22, 66, 'ok')
                    pygame.draw.rect(screen, (105, 105, 105, 118), ok_box, 0)
                    print_text_button(screen, font, 120 + 70, 100 + 170, f"OK",fcolor=(255, 255, 255))
                    if click and tips > 2:
                        add_possess_map = True
                        running = False
        pygame.display.update()

    print('outttt')
    if add_possess:
        if after_click_carlist:  # car [0] add possess
            string=input_text
            element=':'
            new_string=string.replace(element,'')
            fr = open(f'{map_list[map_chose_number]}.json', 'r+')
            dic_bri = eval(fr.read())  # type dic
            input_text_last = float(new_string)  # type float
            #dic_bri[car_list[car_chose_number]]=[]
            dic_bri[car_list[car_chose_number]] = dic_bri[car_list[car_chose_number]][0:] + [
                input_text_last]  # control content
            dicc_bri = str(dic_bri)  # type str

            with open(f'{map_list[map_chose_number]}.json', 'w') as f2:
                f2.write(dicc_bri)
                f2.close()

        # resort
        fr = open(f'{map_list[map_chose_number]}_new_list.txt', 'r+')
        new_list = eval(fr.read())
        new_list = []
        while scan < len(car_list):
            if not dic_bri[car_list[scan]]==[]:
                num=min(dic_bri[car_list[scan]])
                new_list.append((car_list[scan], num))
            else:
               pass
            scan += 1
        neww_list = str(new_list)
        with open(f'{map_list[map_chose_number]}_new_list.txt', 'w') as f2:
            f2.write(neww_list)
            f2.close()
    if add_possess_car:
        # write new in carlist
        car_list.append(input_text_new_car)
        carr_list = str(car_list)

        print(type(car_list))
        print(len(car_list))
        print(car_list[1])

        with open('car_list.txt', 'w') as f2:
            f2.write(carr_list)
            f2.close()

        # write new car in all map
        map_chose_number=0
        while map_chose_number<len(map_list):
            fr = open(f'{map_list[map_chose_number]}.json', 'r+')
            dic_bri = eval(fr.read())  # type dic
            dic_bri[input_text_new_car] = []
            dicc_bri = str(dic_bri)  # type str
            with open(f'{map_list[map_chose_number]}.json', 'w') as f2:
                f2.write(dicc_bri)
                f2.close()
            map_chose_number+=1
    print('control')
    if add_possess_map:
        # write new in maplist
        map_list.append(input_text_new_car)
        mapp_list = str(map_list)
        with open('map_list.txt', 'w') as f2:
            f2.write(mapp_list)
            f2.close()
        with open(f'{input_text_new_car}.json','w+') as f3:
            f3.write('{}')
            f3.close()
        with open(f'{input_text_new_car}_new_list.txt','w+') as f3:
            f3.write('[]')
            f3.close()
        # write all car in new map
        fr = open(f'{input_text_new_car}.json', 'r+')
        dic_bri = eval(fr.read())  # type dic
        car_chose_number = 0
        while car_chose_number<len(car_list):
            dic_bri[car_list[car_chose_number]] = []
            car_chose_number += 1
        dicc_bri = str(dic_bri)  # type str
        with open(f'{input_text_new_car}.json', 'w') as f2:
            f2.write(dicc_bri)
            f2.close()
exit()



