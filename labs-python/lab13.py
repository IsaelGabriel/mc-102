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

        self._dimensions: tuple[int, int] = tuple(map(int, self._lines[2].split()))[::-1]
        
        self._max_value: int = int(self._lines[3])

        self._values: list = []

        for y in range(self._dimensions[1]):
            line: list[int] = list(map(int, self._lines[4 + y].split()))
            self._values.append(line)

    def get_area(self, value_limit: tuple[int, int], seed: tuple[int, int], offset: int, area: list = []) -> list:
        if seed[0] > offset or seed[1] > offset: return []

        area_add = []

        for i in range(2 * offset + 2):
            y = seed[0] + i - offset
            if y < self._dimensions[0] and y >= 0:
                for j in range(2* offset + 2):
                    x = seed[1] + j - offset
                    if x < self._dimensions[1] and x >= 0:
                        if self._values[y][x] >= value_limit[0] and self._values[y][x] <= value_limit[1]:
                            area_add.append(self._values[y][x])
                    
        
        
        return area
                
    def bucket(self, color: int, tolerance: int, seed: tuple[int, int]):
        start_value = self._values[seed[0]][seed[1]]
        value_limit = (start_value - tolerance, start_value + tolerance)
        for position in self.get_area(value_limit, seed, tolerance)[0]:
            self._values[position[0]][position[1]] = color

    def copy(self):
        new_image = Image()
        new_image._lines = self._lines.copy()
        new_image._dimensions = self._dimensions

        return new_image
    
    def __str__(self) -> str:
        text = "\n".join([self._header, " ".join(map(str, self._dimensions)), str(self._max_value)])

        for y in range(self.height):
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
        position: tuple[int, int] = (int(operation[3]), int(operation[2]))
        start_value: int = img[position]

        img.negative(start_value, position, tolerance)

    elif operation[0] == "cmask":
        tolerance: int = int(operation[1])
        position: tuple[int, int] = (int(operation[3]), int(operation[2]))
        start_value: int = img[position]

        img.cmask(start_value, position, tolerance)

    elif operation[0] == "save":
        print(str(img), end="")

def main() -> None:
    img = Image(input())

    operation_quantity: int = int(input())

    ''' _ is the name of the variable because it won't be used '''
    for _ in range(operation_quantity):
        update(img)


if __name__ == "__main__":
    main()