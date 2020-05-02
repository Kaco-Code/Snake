import pygame
from random import randint, randrange
from pygame.locals import *


class Ai:
    def __init__(self):

        self.stop        = False
        self.size_window = [800, 600]
        self.ekor_ular   = []

        self.posisi_batu = [] 
        self.posisi_ular = []
        self.width       = 40


    def _random_pos(self, x, y, replace=False):
        if replace:
            x = randint(0, self.size_window[0])
            y = randint(0, self.size_window[1])

            a = x % self.width
            if a != 0: x = x - a
            a = y % self.width
            if a != 0: y = y - a

        return [x, y]
        


    def parsePos(self, pos_ular, pos_batu):
        x_u = pos_ular[0]
        y_u = pos_ular[1]
        x_b = pos_batu[0]
        y_b = pos_batu[1]

        if x_u == x_b and y_b != y_u:
            if y_u < y_b:
                y_u += self.width
            else:
                y_u -= self.width

        elif x_u != x_b and y_b == y_u:
            if x_u < x_b:
                x_u += self.width
            else:
                x_u -= self.width
        else:
            xx = x_u - x_b
            yy = y_u - y_b
            if yy > xx:
                if x_u < x_b:
                    x_u += self.width
                else:
                    x_u -= self.width
            else:
                if y_u < y_b:
                    y_u += self.width
                else:
                    y_u -= self.width

        self.posisi_ular = [x_u, y_u] 
 
    def run(self):

        pygame.init()
        pygame.display.set_caption('Ai snakeeee .')

        layar  = pygame.display.set_mode(self.size_window)
        skor   = 0
        jalan  = False
        ular   = False
        batu   = False

        # loop
        while not(self.stop):
            layar.fill((0, 0, 0))
            pygame.time.delay(150)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.stop = True
                if event.type == KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[K_SPACE]:
                        if jalan:
                            jalan = False
                        else:
                            jalan = True
                    else:
                        layar.blit(pygame.font.SysFont('Sans Serif', 50).render('tekan SPACE', False, (255, 255, 255)), (self.size_window[0] / 2, self.size_window[1] / 2))

            
            if not(ular):
                ular = True    
                self.posisi_ular = self._random_pos(0, 0, replace=True)
        
            if not(batu):
                batu = True    
                self.posisi_batu = self._random_pos(0, 0, replace=True)
            
            # pygame.draw.rect(layar, (255, 255, 255), (*self.posisi_ular, self.width, self.width))            
            # pygame.draw.ellipse(layar, (0, 255, 0), (*self.posisi_batu, self.width, self.width))

            if jalan:
                self.parsePos(self.posisi_ular, self.posisi_batu)

                if self.posisi_ular == self.posisi_batu:
                    skor += 1
                    self.posisi_batu = self._random_pos(0, 0, replace=True)
                    

            if skor:
                self.ekor_ular.reverse()
                for _ in range(skor):
                    pygame.draw.rect(layar, (255, 255, 0), (*self.ekor_ular[_], self.width, self.width))
                self.ekor_ular.reverse()
                
            self.ekor_ular.append(self.posisi_ular)

            pygame.draw.ellipse(layar, (0, 255, 0), (*self.posisi_batu, self.width, self.width))
            pygame.draw.rect(layar, (255, 255, 255), (*self.posisi_ular, self.width, self.width))            
            
            layar.blit(pygame.font.SysFont('Sans Serif', 20).render('skor: %d' % skor, False, (255, 255, 255)), (10, 10))

            
            pygame.display.update()

        pygame.quit()
                    
if __name__ == "__main__":
    game = Ai()
    game.run()