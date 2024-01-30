import numpy as np
import pygame
import math
from utils import scale_image, blit_rotate_center
import Walls
import Goals

# Constants
pygame.init()
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
LOGO = scale_image(pygame.image.load("imgs/logo_big.png"), 0.8)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)

FINISH = pygame.image.load("imgs/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130, 250)

RED_CAR = scale_image(pygame.image.load("imgs/mario_top.png"), 0.55)
RED_CAR = pygame.transform.rotate(RED_CAR, 90)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()

FPS = 60


# Classes
class AbstractCar:
    def __init__(self, max_vel, rotation_vel):
        self.distance = 0
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.old = (self.x, self.y)
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = self.max_vel
        self.move()

    def move_backward(self):
        self.vel = -self.max_vel / 2
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        poi = mask.overlap(car_mask, offset)
        return poi

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0


#################################################################################ggg


class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (160, 200)

    def reduce_speed(self):
        pass

    def bounce(self):
        pass


#############################################################################
class myLine:
    def __init__(self, pt1, pt2):
        self.pt1 = (pt1[0], pt1[1])
        self.pt2 = (pt2[0], pt2[1])
##############################################################################

class KartGame:
    def __init__(self):
        self.walls = Walls.getWalls()
        self.goals = Goals.getGoals()
        #self.goals[-1].isactiv = False
        self.current_point = 0
        self.collisions = 0
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mario Kart!")
        self.finished = False
        self.clock = pygame.time.Clock()
        self.player_car = PlayerCar(3, 4)
        self.images = [(GRASS, (0, 0)), (TRACK, (0, 0)),
                       (FINISH, FINISH_POSITION)]

        self._draw_points(self.WIN)

    def _draw_points(self, win):
        for point in self.walls:
            point.draw(win)
        for point in self.goals:
            point.draw(win)

    def _update_path_point(self):
        pass

    def reset(self):
        self.collisions = 0
        self.finished = False
        self.player_car = PlayerCar(3, 4)
        pass

    def wall_collision(self, wall):

        self.player_car.width = self.player_car.img.get_width()
        self.player_car.height = self.player_car.img.get_height()

        self.p1 = (self.player_car.x - self.player_car.width / 2, self.player_car.y - self.player_car.height / 2)
        self.p2 = (self.player_car.x + self.player_car.width / 2, self.player_car.y - self.player_car.height / 2)
        self.p3 = (self.player_car.x + self.player_car.width / 2, self.player_car.y + self.player_car.height / 2)
        self.p4 = (self.player_car.x - self.player_car.width / 2, self.player_car.y + self.player_car.height / 2)

        line1 = myLine(self.p1, self.p2)
        line2 = myLine(self.p2, self.p3)
        line3 = myLine(self.p3, self.p4)
        line4 = myLine(self.p4, self.p1)

        x1 = wall.x1
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2

        lines = []
        lines.append(line1)
        lines.append(line2)
        lines.append(line3)
        lines.append(line4)

        for li in lines:

            x3 = li.pt1[0]
            y3 = li.pt1[1]
            x4 = li.pt2[0]
            y4 = li.pt2[1]

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

            if (den == 0):
                den = 0
            else:
                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

                if t > 0 and t < 1 and u < 1 and u > 0:
                    return (True)

        return (False)

    def is_collision(self, car=None):
        if car is None:
            car = self.player_car

        if not (0 <= car.x <= WIDTH and 0 <= car.y <= HEIGHT):
            return True

        # if car.collide(TRACK_BORDER_MASK) is not None:
        # return False
        for wall in self.walls:
            if self.wall_collision(wall):
                return True
        index = 1
        for goal in self.goals:

            if index > len(self.goals):
                index = 1
            if goal.isactiv:
                if self.wall_collision(goal):
                    goal.isactiv = False
                    self.goals[index - 2].isactiv = True
                    self.player_car.distance += 1

            index = index + 1

        finish_poi_collide = car.collide(FINISH_MASK, *FINISH_POSITION)
        if finish_poi_collide is not None:
            if finish_poi_collide[1] == 0:
                return True

            # CAR finishes the lap
            else:
                car.reset()
                # print("finish")
                self.finished = True
                return True
        return False

    def _draw_gui(self, win, images, player_car):
        for img, pos in images:
            win.blit(img, pos)
        self._draw_points(win)
        player_car.draw(win)
        pygame.display.update()

    def _update_ui(self):
        self._draw_gui(self.WIN, self.images, self.player_car)

    # not used
    def _move(self):
        keys = pygame.key.get_pressed()
        arr = np.array([0, 0, 0])

        if keys[pygame.K_a]:
            arr[1] = 1
        if keys[pygame.K_d]:
            arr[2] = 1
        if keys[pygame.K_w]:
            arr[0] = 1

        return arr

    def play_step(self):
        keys = pygame.key.get_pressed()
        moved = False
        reward = 0

        action = self._move()
        action = np.array(action, dtype=np.bool_)

        if action[1]:
            self.player_car.rotate(left=True)
            # action[0] = True
        if action[2]:
            self.player_car.rotate(right=True)
            # action[0] = True
        if action[0]:
            moved = True
            self.player_car.move_forward()

        if moved:
            self._update_path_point()
            reward = self.current_point
            self.player_car.old = (self.player_car.x, self.player_car.y)

        # check if game over
        game_over = False
        score = self.player_car.distance * 100 / len(self.goals)
        if self.is_collision():
            game_over = True
            reward = -1 if not self.finished else reward
            return reward, game_over, score

        self.clock.tick(FPS)
        self._update_ui()
        return reward, game_over, score


# Game Loop
def main():
    game = KartGame()
    run = True
    # game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        r, game_over, score = game.play_step()

        if game_over:
            break

    print(f"Final Score {score} %")

    pygame.quit()


if __name__ == "__main__":
    main()
