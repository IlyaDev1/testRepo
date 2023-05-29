class Window:
    __attr = {
        'name': 'WindowName',
        'x': 1920,
        'y': 1080,
        'count': 0
    }

    def __init__(self):
        self.__dict__ = self.__attr
        self.__attr['count'] += 1

    def setX(self, value):
        self.__attr['x'] = value