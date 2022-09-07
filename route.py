simple_route = {
    'route': [11 * [-1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 11 * [-1]],
    'start': [2, 1],
    'meta': [[1, 10], [2, 10], [3, 10]]}


class Route:
    def __init__(self, route):
        self._route = route['route']
        self._start = route['start']
        self._meta = route['meta']

    def print_route(self):
        for line in self._route:
            for element in line:
                match element:
                    case -1:
                        print('*', end='')
                    case 0:
                        print(':', end='')
                    case 2:
                        print('|', end='')
            print('', end='\n')

    def get_route(self):
        return self._route

    def get_start_point(self):
        return self._start

    def get_end_point(self):
        return self._meta
