size: tuple[int] # linhas, colunas

class Robot:
    def __init__(self):
        self._position: tuple[int] = (0, 0)
        self.target: int = 0
        self.mode = "scan"
    
    @property
    def line(self) -> int:
        return self._position[0]
    
    @line.setter
    def line(self, new_line):
        global size
        if new_line < 0:
            new_line = 0
        elif new_line >= size[0]:
            new_line = size[0] - 1
        
        self._position = (new_line, self._position[1])

    @property
    def column(self) -> int:
        return self._position[1]
    
    @column.setter
    def column(self, new_column: int):
        global size
        if new_column < 0:
            new_column = 0
        elif new_column >= size[1]:
            new_column = size[1] - 1
        
        self._position = tuple((self._position[0], new_column))

    @property
    def x(self):
        global size
        return (self._position[0] * size[1]) + self._position[1]
    
    @x.setter
    def x(self, new_x):
        global size
        column = new_x % size[1]
        line = (new_x - column) // size[1]
        self._position = (line, column)

    def scan_near(self, matrix) -> int:
        global size

        if self.column > 0:
            if matrix[self.x - 1]:
                return self.x - 1

        if self.line > 0:
            if matrix[self.x - size[1]]:
                return self.x - size[1]
        
        if self.column < size[1] - 1:
            if matrix[self.x + 1]:
                return self.x + 1
        
        if self.line < size[0] - 1:
            if matrix[self.x + size[1]]:
                return self.x + size[1]
        
        return self.x

    

    def is_on_target(self) -> bool:
        return self.x == self.target

def print_matrix(matrix, robot_position):
    global size

    for line in range(size[0]):    
        l = ['o' if p else '.' for p in matrix[line * size[1]:][:size[1]]]
        if robot_position[0] == line:
            l[robot_position[1]] = 'r'
        print(" ".join(l))
    print()
    # print("---")

def main():
    global size

    size = (int(input()), 0)
    matrix = []

    for _ in range(size[0]):
        matrix += [(c == 'o') for c in input().split()]

    size = (size[0], len(matrix) // size[0])

    robot: Robot = Robot()

    print_matrix(matrix, (0, 0))

    scan_done = False
    next_h = True


    if robot.scan_near(matrix) not in [robot.x, robot.x + 1]: robot.mode = "clean"

    while not scan_done:
        matrix[robot.x] = False
        if robot.mode == "scan":

            if robot.line % 2 == 0:
                if robot.column < size[1] - 1:
                    robot.x += 1
                    if robot.column == size[1] - 1: next_h = False
                else:
                    if robot.line < size[0] - 1:
                        robot.line += 1
                        next_h = True
                    else:
                        scan_done = True
                        continue
            else:
                if robot.column > 0:
                    robot.x -= 1
                    if robot.column == 0: next_h = False
                else:
                    if robot.line < size[0] - 1:
                        robot.line += 1
                        next_h = True
                    else:
                        scan_done = True
                        continue
            
            robot.target = robot.x
            
            if True in matrix and next_h:
                vertical_scan = robot.scan_near(matrix)

                v_range = [robot.x - size[1], robot.x + size[1]]

                if vertical_scan in v_range: robot.mode = "clean"

        elif robot.mode == "clean":
            position = robot.scan_near(matrix)
            
            if position == robot.x:
                robot.mode = "scan" if robot.is_on_target() else "return"
                continue

            robot.x = position

        elif robot.mode == "return":

            target_column: int = robot.target % size[1]
            target_line: int = (robot.target - target_column) // size[1]

            if robot.column > target_column:
                robot.column -= 1
            elif robot.column < target_column:
                robot.column += 1
            elif robot.line > target_line:
                robot.line -= 1
            elif robot.line < target_line:
                robot.line += 1
            
            if robot.scan_near(matrix) != robot.x: robot.mode = "clean"
            elif robot.is_on_target(): robot.mode = "scan"
        
        print_matrix(matrix, (robot.line, robot.column))

    while robot.x < (len(matrix) - 1):
        robot.x += 1
        print_matrix(matrix, (robot.line, robot.column))


if __name__ == "__main__":
    main()