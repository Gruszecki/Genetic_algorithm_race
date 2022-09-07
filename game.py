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


def print_car(x: int, y: int, symbol: str):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x+1, y+1, symbol))


class Car:
    _MOVES = ['U', 'R', 'D', 'L', 'UR', 'DR', 'DL', 'UL']
    distance = 0
    amount_of_moves = 0
    end_reached = False

    def __init__(self, start_point):
        self.x, self.y = start_point
        self.genes = [random.choice(self._MOVES) for _ in range(20)]

    def __str__(self):
        return self.genes


class Game:
    def __init__(self, route, cars_amount, iterations):
        self._route = route
        self._cars_amount = cars_amount
        self._iterations = iterations
        self.car_generation = []

        for _ in range(self._cars_amount):
            self.car_generation.append(Car(self._route.get_start_point()))

    def convert_direction(self, direction: str):
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

    def race(self, car):
        amount_of_moves = 0

        for gene in car.genes:
            move = convert_direction(gene)
            car.x += move[0]
            car.y += move[1]

            match self._route.get_route()[car.x][car.y]:
                case -1:
                    car.x -= move[0]
                    car.y -= move[1]
                case 0:
                    pass
                case 2:
                    car.end_reached = True
                    break

            amount_of_moves += 1

        car.distance = car.y

    def show_race(self, car):
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
                    pass
                case 2:
                    print_car(car.x, car.y, 'O')
                    car.end_reached = True
                    print('End point reached!')
                    break
