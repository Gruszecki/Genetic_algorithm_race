from game import Game, Car
from route import Route, complex_route


route = Route(complex_route)
game = Game(route=route, cars_amount=40, iterations=500)
result_generation = game.start_learning()

for car in result_generation:
    print(car)
    # game.show_race(car)
