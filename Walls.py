import pygame


class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, win):
        pygame.draw.line(win, (0, 0, 255), (self.x1, self.y1), (self.x2, self.y2), 5)


def getWalls():
    walls = []

    wall1 = Wall(12, 501, 15, 130)
    wall2 = Wall(15, 130, 31, 58)
    wall3 = Wall(31, 58, 119, 14)
    wall4 = Wall(119, 14, 226, 64)
    wall6 = Wall(228, 54, 230, 349)
    wall7 = Wall(228, 54, 346, 20)
    wall8 = Wall(346, 20, 749, 20)
    wall9 = Wall(749, 20, 789, 70)
    wall10 = Wall(789, 70, 789, 260)
    wall11 = Wall(789, 260, 718, 309)
    wall12 = Wall(718, 309, 462, 309)
    wall13 = Wall(718, 309, 792, 374)
    wall14 = Wall(792, 374, 792, 704)
    wall15 = Wall(792, 704, 729, 782)
    wall16 = Wall(729, 782, 629, 782)
    wall17 = Wall(629, 782, 535, 720)
    wall18 = Wall(535, 720, 500, 550)
    wall19 = Wall(500, 550, 454, 767)
    wall20 = Wall(454, 767, 304, 787)
    wall21 = Wall(304, 787, 12, 501)

    wall5 = Wall(125, 142, 125, 448)
    wall22 = Wall(125, 448, 330, 640)
    wall23 = Wall(330, 640, 380, 423)
    wall24 = Wall(380, 423, 660, 423)
    wall25 = Wall(660, 423, 660, 673)

    wall26 = Wall(145, 468, 340, 468)
    wall27 = Wall(340, 468, 341, 310)
    wall28 = Wall(380, 423, 341, 310)
    wall29 = Wall(341, 310, 341, 140)
    wall30 = Wall(341, 140, 681, 140)
    wall31 = Wall(681, 140, 681, 200)
    wall32 = Wall(681, 200, 381, 200)
    wall33 = Wall(381, 200, 341, 240)

    walls.append(wall1)
    walls.append(wall2)
    walls.append(wall3)
    walls.append(wall4)
    walls.append(wall5)
    walls.append(wall6)
    walls.append(wall7)
    walls.append(wall8)
    walls.append(wall9)
    walls.append(wall10)
    walls.append(wall11)
    walls.append(wall12)
    walls.append(wall13)
    walls.append(wall14)
    walls.append(wall15)
    walls.append(wall16)
    walls.append(wall17)
    walls.append(wall18)
    walls.append(wall19)
    walls.append(wall20)
    walls.append(wall21)
    walls.append(wall22)
    walls.append(wall23)
    walls.append(wall24)
    walls.append(wall25)
    walls.append(wall26)
    walls.append(wall27)
    walls.append(wall28)
    walls.append(wall29)
    walls.append(wall30)
    walls.append(wall31)
    walls.append(wall32)
    walls.append(wall33)

    return (walls)