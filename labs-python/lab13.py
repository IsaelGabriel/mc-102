import os

class Image:
    def __init__(self, path: str = ""):
        if len(path) == 0: return

        path = os.getcwd() + os.sep + path

        if "/" in path and os.sep != "/":
            path = path.replace("/", os.sep)

        file = open(path)
        self._lines: list[str] = file.read().split("\n")    
        file.close()

        ''' Remove whitespaces '''
        for i in range(len(self._lines)):
            self._lines[i] = " ".join(self._lines[i].split())

        self._header = "P2\n# Imagem criada pelo lab13"

        self._dimensions: tuple[int, int] = tuple(map(int, self._lines[2].split()[::-1]))
        
        self._max_value: int = int(self._lines[3])

        self._values: list = []

        for y in range(self._dimensions[0]):
            line: list[int] = list(map(int, self._lines[4 + y].split()))
            self._values.append(line)
        
    
    def select_all(self, tolerance: int, color: int) -> list:
        for y in range(self._dimensions[0]):
            for x in range(self._dimensions[1]):
                if self._values[y][x] >= color - tolerance and self._values[y][x] <= color + tolerance:
                    self._values[y][x] *= -1
                    self._values[y][x] -= 1

    def goes_to(self, position: tuple[int, int], origin: tuple[int, int]) -> bool:
        for i in range(3):
            y = position[0] + i - 1
            if y >= 0 and y < self._dimensions[0]:
                for j in position(3):
                    x = position[1] + i - 1
                    if x >= 0 and x < self._dimensions[1]:
                        if self._values[y, x] < 0:
                            if self.goes_to((y, x), origin):
                                return True

        return False 

    def select(self, tolerance: int, seed: tuple[int, int], start_color: int, value_limit: tuple[int,int]):
        for y in range(self._dimensions[0]):
            for x in range(self._dimensions[1]):
                if self._values[y][x] < 0:
                    if not self.goes_to((y, x), seed):
                        self._values[y][x] += 1
                        self._values[y][x] *= -1

    def bucket(self, color: int, tolerance: int, seed: tuple[int, int]):
        start_color = self._values[seed[0]][seed[1]]
        value_limit = (start_color - tolerance, start_color + tolerance)

        self.select(tolerance, seed, start_color, value_limit)

        for y in range(self._dimensions[0]):
            for x in range(self._dimensions[1]):
                if self._values[y][x] < 0:
                    self._values[y][x] = color


    def negative(self, tolerance: int, seed: tuple[int, int], start_color: int = -1, value_limit: tuple[int,int] = None):
        start_color = self._values[seed[0]][seed[1]]
        value_limit = (start_color - tolerance, start_color + tolerance)

        self.select(tolerance, seed, start_color, value_limit)

        for y in range(self._dimensions[0]):
            for x in range(self._dimensions[1]):
                if self._values[y][x] < 0:
                    self._values[y][x] += self._max_value + 1

    def cmask(self, tolerance: int, seed: tuple[int, int]):
        start_color = self._values[seed[0]][seed[1]]
        value_limit: tuple[int, int] = (start_color - tolerance, start_color + tolerance)

        self.select(tolerance, seed, start_color, value_limit)
        
        for y in range(self._dimensions[0]):
            for x in range(self._dimensions[1]):
                self._values[y][x] = 0 if self._values[y][x] < 0 else 255

        


    def copy(self):
        new_image = Image()
        new_image._lines = self._lines.copy()
        new_image._dimensions = self._dimensions

        return new_image
    
    def __str__(self) -> str:
        text = "\n".join([self._header, " ".join(map(str, self._dimensions[::-1])), str(self._max_value)])

        for y in range(self._dimensions[0]):
            text += "\n" + " ".join(map(str, self._values[y]))

        return text

def update(img: Image): 
    operation: list[str] = input().split()

    if operation[0] == "bucket":
        color: int = int(operation[1])
        tolerance: int = int(operation[2])
        seed: tuple[int, int] = (int(operation[4]), int(operation[3]))

        img.bucket(color, tolerance, seed)

    elif operation[0] == "negative":
        tolerance: int = int(operation[1])
        seed: tuple[int, int] = (int(operation[3]), int(operation[2]))

        img.negative(tolerance, seed)

    elif operation[0] == "cmask":
        tolerance: int = int(operation[1])
        seed: tuple[int, int] = (int(operation[3]), int(operation[2]))

        img.cmask(tolerance, seed)

    elif operation[0] == "save":
        print(str(img), end="")

    #img.reset_selection_matrix()

def main() -> None:
    img = Image(input())

    operation_quantity: int = int(input())

    ''' _ is the name of the variable because it won't be used '''
    for _ in range(operation_quantity):
        update(img)


if __name__ == "__main__":
    main()