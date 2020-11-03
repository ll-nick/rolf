import pygame
from time import sleep
pygame.init()
gamepad = pygame.joystick.Joystick(0)
gamepad.init()
buttons = {'1':0, '2':0, '3':0, '4':0,
            'L1':0, 'R1':0,'L2':0, 'R2':0,
            'select':0, 'start':0, 'leftStick':0, 'rightStick':0,
            'axis0':0.,'axis1':0.,'axis2':0.,'axis3':0.,'axis4':0.,'axis5':0.,'axis6':0.}
axiss = [0.,0.,0.,0.,0.,0.,0.,0.]

def getGamepad(name = ''):
    global buttons
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            axiss[event.axis] = round(event.value, 2)
        elif event.type == pygame.JOYBUTTONDOWN:
            #print(event.dict, event.joy, event.button, 'PRESSED')
            for x,(key, val) in enumerate(buttons.items()):
                if x < 12:
                    if gamepad.get_button(x):buttons[key] = 1
        elif event.type == pygame.JOYBUTTONUP:
            #print(event.dict, event.joy, event.button, 'RELEASED')
            for x,(key, val) in enumerate(buttons.items()):
                if x < 12:
                    if event.button==x:buttons[key] = 0

    buttons['axis0'],buttons['axis1'],buttons['axis2'],buttons['axis3'],buttons['axis4'],buttons['axis5'],buttons['axis6'] = [axiss[0],axiss[1],axiss[2],axiss[3],axiss[4],axiss[5],axiss[6]]

    if name == '':
        return buttons
    else:
        return buttons[name]

def getSpeed():
    return getGamepad('axis3')

def getTurn():
    return getGamepad('axis2')

def getStop():
    return getGamepad('rightStick')

def main():
    print(getGamepad())
    sleep(0.1)

if __name__ == '__main__':
    while True:
        main()