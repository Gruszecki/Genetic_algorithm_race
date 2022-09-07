from game import Game, Car
from route import Route

simple_route = {
    'route': [11 * [-1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 11 * [-1]],
    'start': [2, 1],
    'meta': [[1, 10], [2, 10], [3, 10]]
}
route = Route(simple_route)
game = Game(route=route, cars_amount=40, iterations=100)
