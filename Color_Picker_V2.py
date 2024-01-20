# Controlling positions

import pygame

'''
press b, q, n to change red value. press l,e, x to change green value. press z, g, h to change blue value.
press w, a, s, d to move text around. press m to clone text. press p to change color of text and background.
'''
# Game Setup
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
R = 0
B = 0
G = 0
H = -12


color =  R , G, B
letter = ['A', 'B', 'C', 'D', 'E', 'F' , 'G', 'H', 'I', 'J', 'K', 'L', 'M' ,'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
class Screen:
    def __init__(self, w, h, color, bg_color) :
        global R, G, B
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.label = (R, G, B)
        self.TextLabel = self.font.render(str(self.label), True, color, bg_color)
        self.TextRect = self.TextLabel.get_rect(center=(w, h))   # Change position
        self.w, self.h = w, h

    def getPosition(self):
        #print(self.TextRect)
        #print("Coordinates (L, T)", self.TextRect.left, self.TextRect.top)
        print("dimensions", self.TextRect.width, self.TextRect.height)
        
    def setColor(self, color):
        self.TextLabel = self.font.render(str(self.label), True, (0,0,0), color)
        self.TextRect = self.TextLabel.get_rect(center=(self.w, self.h))   # Change position
    def update_letter(self):
        self.label = letter[H]

# The main game loop

def main():

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    BACKGROUND = (255, 255, 255)
    PADDING = 20

    run = True

    sound1 = pygame.mixer.Sound('sm64_star_appears.wav')
    sound2 = pygame.mixer.Sound('sm64_happy_message.wav')
    sound3 = pygame.mixer.Sound('sm64_mario_weak.wav')
    sound4 = pygame.mixer.Sound('sm64_key_get.wav')

    w, h = WINDOW_WIDTH//2, WINDOW_HEIGHT//2
    global color, R, G, B, H
    bg_color = (255, 255, 255)

    lst = []
    while run :
        WINDOW.fill(BACKGROUND)
        # Get inputs
        
       
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_a:
                    if w > PADDING:
                        w = w - 10
                if event.key == pygame.K_d:
                    if w < WINDOW_WIDTH-PADDING:
                        w = w + 10
                if event.key == pygame.K_w:
                    if h > PADDING:
                        h = h - 10
                if event.key == pygame.K_s:
                    if h < WINDOW_HEIGHT-PADDING:
                        h = h + 10
                if event.key == pygame.K_f:
                    sound3.play()
                    H = H-1
                    if H < -26:
                        H = -1
                    test_screen.update_letter()
                if event.key == pygame.K_m:
                    sound4.play()
                    lst.append((bg_color, color, w, h))
                if event.key == pygame.K_o:
                    sound2.play()
                    H = H + 1
                    if H > -1:
                        H = -26
                    test_screen.update_letter()
                if event.key == pygame.K_b:
                    R += 5
                    if R > 255:
                       R = 255
                if event.key == pygame.K_q:
                    R -= 5
                    if R < 0:
                        R = 0
                if event.key == pygame.K_n:
                    R = 0
                if event.key == pygame.K_l:
                        G += 5
                        if G > 255:
                            G = 255
                if event.key == pygame.K_e:
                    G -= 5
                    if G < 0:
                            G = 0
                if event.key == pygame.K_x:
                    G = 0
                if event.key == pygame.K_z:
                    B += 5
                    if B > 255:
                      B = 255
                if event.key == pygame.K_g:
                    B -= 5
                    if B < 0:
                         B = 0
                if event.key == pygame.K_h:
                    B = 0
                if event.key == pygame.K_p:
                    sound1.play()
                    r = int(input("R:\t"))
                    g = int(input("G:\t"))
                    b = int(input("B:\t"))
                    BACKGROUND = (r,g,b)
                    if r < 100:
                        R = 250
                    elif r > 255:
                        r = 255
                        R = 255
                    else:
                        R = r - 100
                    if b < 100:
                        B = 250
                    elif b > 255:
                        b = 255
                        B =255
                    else:
                        B = b - 100
                    if g < 100:
                        G = 250
                    elif g > 255:
                        g = 255
                        G = 255
                    else:
                        G = g - 100
                    
                    color = R, G, B
                    bg_color = r,g,b
                    print("coordinates", w, h)
                    test_screen.getPosition()

        for obj_bg_color, obj_color, obj_w, obj_h in lst:
            test_screen = Screen(obj_w, obj_h, obj_color, obj_bg_color)
            WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)

        test_screen = Screen(w, h, color, bg_color)
        WINDOW.blit(test_screen.TextLabel, test_screen.TextRect)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()