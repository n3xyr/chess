import time
import pygame

class chessClock:
    def __init__(self, clockTime, clockIncrement):
        self.whiteTime = clockTime
        self.blackTime = clockTime
        self.increment = clockIncrement
        self.turn = 'white'
    

    def setTurn(self, turn):
        self.turn = turn


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


    def getColorY(self, color):
        if color == 'white':
            return 8
        else:
            return 0


    def convertTime(self, time):
        ms = str(time % 1)[:2]
        s = str(time % 60)
        m = str((time // 60) % 60)
        h = str(time // 3600)

        if h:
            return h + ':' + m + ':' + s
        elif m:
            return m + ':' + s
        elif s > 20:
            return s
        else:
            return s + '.' + ms


    def drawClock(self, surface, TOPMARGIN, LEFTMARGIN, TILESIZE, color, TEXTCOLOR, BGCOLOR):
        txtSize = 0.3
        robotoFont = pygame.font.SysFont('Roboto', int(txtSize * TILESIZE))
        sizeX, sizeY = robotoFont.size('      ')
        
        clockRect = pygame.Rect((int(LEFTMARGIN + 8 * TILESIZE - sizeX - txtSize * TILESIZE), int(TOPMARGIN + self.getColorY(color) * TILESIZE - sizeY - txtSize * TILESIZE), int(sizeX + 2 * txtSize * TILESIZE), int(sizeY)))
        time = self.getDisplayTime(color)
        timeTxt = robotoFont.render(self.convertTime(time), True, TEXTCOLOR)
        timeRect = timeTxt.get_rect(midright = (clockRect.right - txtSize * TILESIZE, clockRect.centery))

        pygame.draw.rect(surface, BGCOLOR, clockRect, border_radius= TILESIZE // 25)
        surface.blit(timeTxt, timeRect)

