'''
#############################################################
#-----------------------------------------------------------|
#O----------------------------------------------------------|
#-----------------------------------------------------------|
#############################################################
'''
import random
import os
import sys
import time
from route import Route, simple_route

route = Route(simple_route)


def print_car(x: int, y: int, symbol: str):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x+1, y+1, symbol))

def convert_direction(direction: str):
    match direction:
        case 'U':
            return -1, 0
        case 'R':
            return 0, 1
        case 'D':
           return 1, 0
        case 'L':
            return 0, -1
        case 'UR':
            return -1, 1
        case 'DR':
            return 1, 1
        case 'DL':
            return 1, -1
        case 'UL':
            return -1, -1


class Car:
    MOVES = ['U', 'R', 'D', 'L', 'UR', 'DR', 'DL', 'UL']

    def __init__(self):
        self.x, self.y = route.get_start_point()
        self.genes = [random.choice(self.MOVES) for _ in range(20)]

    def __str__(self):
        return self.genes


class Game:
    car = Car()
    os.system('cls')
    route.print_route()
    print_car(car.x, car.y, 'O')

    for gene in car.genes:
        move = convert_direction(gene)
        car.x += move[0]
        car.y += move[1]

        time.sleep(0.5)

        os.system('cls')
        route.print_route()

        match route.get_route()[car.x][car.y]:
            case -1:
                car.x -= move[0]
                car.y -= move[1]
                print_car(car.x, car.y, '@')
                print('Watch out!')
            case 0:
                print_car(car.x, car.y, 'O')
                print('...')
            case 2:
                print_car(car.x, car.y, 'O')
                print('End point reached!')
                break


