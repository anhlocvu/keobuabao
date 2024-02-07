import random as rd
import pygame
import time
import sys
pygame.mixer.init()
music = pygame.mixer.Sound("sound/music.mp3")
music.set_volume(0.30)
music.play(-1)

tiencuoc = int(input("nhập tiền cược: "))
if tiencuoc > 100:
    tiencuoc = 100
    print("số tiền không được lớn hơn 100")
coins = pygame.mixer.Sound("sound/coins.mp3")
coins.play()
print("số tiền hiện tại của bạn là")
print(tiencuoc)
time.sleep(1.5)
m = pygame.mixer.Sound("sound/m.mp3")
m.play()
while True:
    nguoichoi = input("nhập lựa chọn của bạn: nhớ nhập có dấu nha ông nội")
    
    maytinh = rd.randint(1, 3)
    if maytinh == 1:
        maytinh = 'kéo'
    if maytinh == 2:
        maytinh = 'búa'
    if maytinh == 3:
        maytinh = "bao"
    print("người chơi ra:",nguoichoi)
    print("đối thủ ra:",maytinh)
    if nguoichoi == maytinh:
        print('hòa,', 'hai cái '+nguoichoi+' không làm gì được nhau')
        hoa=pygame.mixer.Sound("sound/hoa.wav")
        hoa.play()
    elif (nguoichoi == 'kéo') and (maytinh == 'búa'):
        print('thua', 'búa đập gẫy kéo')
        thua = pygame.mixer.Sound("sound/thua.mp3")
        thua.play()
        tiencuoc -= 50
    elif (nguoichoi == 'búa') and (maytinh == 'bao'):
        print('thua','cái bao bao cây búa')
        thua = pygame.mixer.Sound("sound/thua.mp3")
        thua.play()
        
        tiencuoc -= 50
    elif (nguoichoi == 'bao') and (maytinh == 'kéo'):
        print('thua','cái kéo cắt mẹ cái bao rồi còn gì')
        thua = pygame.mixer.Sound("sound/thua.mp3")
        thua.play()
        
        tiencuoc -= 50
    else:
        v = pygame.mixer.Sound("sound/votay.ogg")
        v.play()
        print('xin chúc mừng! bạn đã thắng')
        tiencuoc += 50
    print("số tiền hiện tại là")
    print(tiencuoc)
    if tiencuoc<=0:
        thua = pygame.mixer.Sound("sound/thua.mp3")
        thua.play()
        print("'hết tiền rồi nha")
        time.sleep(1.5)
        music.set_volume(0.25)
        time.sleep(1.5)
        music.set_volume(0.10)
        time.sleep(1.5)
        music.set_volume(0)
        sys.exit()
