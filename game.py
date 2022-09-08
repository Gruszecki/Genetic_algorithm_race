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

    def __init__(self, start_point, genes=None):
        self.x, self.y = start_point

        if genes is None:
            self.genes = [random.choice(self._MOVES) for _ in range(50)]
        else:
            self.genes = genes

    def __str__(self):
        return f'dist: {self.distance}, moves: {self.amount_of_moves}, end reached: {self.end_reached}'


class Game:
    def __init__(self, route, cars_amount, iterations):
        self._route = route
        self._cars_amount = cars_amount
        self._iterations = iterations
        self._car_generation = []

        for _ in range(self._cars_amount):
            self._car_generation.append(Car(self._route.get_start_point()))

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
            move = self.convert_direction(gene)
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

        car.amount_of_moves = amount_of_moves
        car.distance = car.y

    def show_race(self, car):
        os.system('cls')
        self._route.print_route()
        print_car(car.x, car.y, 'O')

        for gene in car.genes:
            move = self.convert_direction(gene)
            car.x += move[0]
            car.y += move[1]

            time.sleep(1)

            os.system('cls')
            self._route.print_route()

            match self._route.get_route()[car.x][car.y]:
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
            print(car)

    def make_children(self, generation):
        new_generation = []
        better_sort = generation[:int(len(generation)/2)]

        for i in range(0, len(better_sort), 2):
            # Crossing
            child_1 = better_sort[i].genes[:int(len(better_sort[i].genes)/2)] + better_sort[i+1].genes[int(len(better_sort[i].genes)/2):]
            child_2 = better_sort[i+1].genes[:int(len(better_sort[i].genes)/2)] + better_sort[i].genes[int(len(better_sort[i].genes)/2):]

            child_3 = []
            child_4 = []
            for iter, (gen_1, gen_2) in enumerate(zip(better_sort[i].genes, better_sort[i+1].genes)):
                if iter % 2:
                    child_3.append(gen_1)
                    child_4.append(gen_2)
                else:
                    child_3.append(gen_2)
                    child_4.append(gen_1)

            # Mutation
            child_1[int(random.uniform(0, len(child_1)-0.01))] = random.choice(better_sort[i]._MOVES)
            child_2[int(random.uniform(0, len(child_2)-0.01))] = random.choice(better_sort[i]._MOVES)
            child_3[int(random.uniform(0, len(child_3)-0.01))] = random.choice(better_sort[i]._MOVES)
            child_4[int(random.uniform(0, len(child_4)-0.01))] = random.choice(better_sort[i]._MOVES)

            # Creating new generation
            new_generation.append(Car(self._route.get_start_point(), child_1))
            new_generation.append(Car(self._route.get_start_point(), child_2))
            new_generation.append(Car(self._route.get_start_point(), child_3))
            new_generation.append(Car(self._route.get_start_point(), child_4))

        return new_generation

    def start_learning(self):
        sorted_generation = []
        for i in range(self._iterations):
            for car_no, car in enumerate(self._car_generation):
                car.amount_of_moves = 0
                car.distance = 0
                car.end_reached = False
                car.x, car.y = self._route.get_start_point()

                self.race(car)
                print(f'iter: {i}, car No: {car_no}, dist: {car.distance}, moves: {car.amount_of_moves}, end reached: {car.end_reached}')

            sorted_generation = sorted(self._car_generation, key=lambda c: (c.end_reached, -c.amount_of_moves, c.distance), reverse=True)
            self._car_generation = self.make_children(sorted_generation)

        for car in sorted_generation:
            car.x, car.y = self._route.get_start_point()
        return sorted_generation
