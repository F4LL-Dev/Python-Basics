class box:
    def __init__(self, length, width, colour):
        self.length = length
        self.width = width
        self.colour = colour
        self.parameter = 2 * (length + width)
        self.area = (length * width)
