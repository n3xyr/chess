import time
import pygame

class chessClock:
    def __init__(self, clockTime, clockIncrement):
        self.clockTime = clockTime
        self.whiteTime = float(clockTime)
        self.blackTime = float(clockTime)
        self.increment = clockIncrement
        self.turn = 'white'
    

    def setTurn(self, turn):
        self.turn = turn


    def checkClock0(self):
        if self.whiteTime <= 1:
            return 'white'
        elif self.blackTime <= 1:
            return 'black'
        else: 
            return False


    def updateTime(self):
        delta = time.time() - self.lastTime
        if self.turn == 'white':
            self.whiteTime -= delta
        else:
            self.blackTime -= delta
        self.updateLastTime()


    def getDisplayTime(self, color):
        if color == 'white':
            return self.whiteTime
        else:
            return self.blackTime


    def updateLastTime(self):
        self.lastTime = time.time()


    def convertTime(self, time):
        ms = time % 1
        s = int((time //1) % 60)
        m = int((time // 60) % 60)
        h = int(time // 3600)

        if h != 0:
            return str(h) + ':' + str(m // 10) + str(m % 10) + ':' + str(s // 10) + str(s % 10)
        elif m != 0:
            return str(m) + ':' + str(s // 10) + str(s % 10)
        elif s > 20:
            return str(s)
        else:
            return str(s) + '.' + str(ms)[2:4]


    def drawClock(self, surface, TOPMARGIN, LEFTMARGIN, TILESIZE, color, TEXTCOLOR, BGCOLOR):
        txtSize = 0.3
        robotoMedium = pygame.font.Font('fonts/Roboto-Medium.ttf', int(txtSize * TILESIZE))
        sizeX, sizeY = robotoMedium.size(' ')
        if color == 'white':
            clockRect = pygame.Rect((int(LEFTMARGIN + 6.5 * TILESIZE - TILESIZE // 20), int(TOPMARGIN + 8 * TILESIZE + sizeY // 5), int(1.5 * TILESIZE), int(sizeY + 0.1 * TILESIZE)))
        else:
            clockRect = pygame.Rect((int(LEFTMARGIN + 6.5 * TILESIZE - TILESIZE // 20), int(TOPMARGIN - int(1.2 * sizeY + 0.1 * TILESIZE)), int(1.5 * TILESIZE), int(sizeY + 0.1 * TILESIZE)))
        
        time = self.getDisplayTime(color)
        timeTxt = robotoMedium.render(self.convertTime(time), True, TEXTCOLOR)
        timeRect = timeTxt.get_rect(midright = (clockRect.right - 0.05 * TILESIZE, clockRect.centery))

        pygame.draw.rect(surface, BGCOLOR, clockRect, border_radius= TILESIZE // 25)
        surface.blit(timeTxt, timeRect)