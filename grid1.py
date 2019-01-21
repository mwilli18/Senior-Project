def ask_size():
    while True:
        try:
            grid_size = int(input("input grid length and width\n"))
            if grid_size < 2:
                print("invalid int")
            else:
                return grid_size
        except ValueError:
            print ("invalid input")

def make_grid(size):
    return [[0] * size for _ in range(size)]

def print_grid(grid):
    for row in grid:
        print(row)

grids = make_grid(ask_size())
print_grid(grids)



#grid = numpy.zeros(shape=(4,4))
#can also be used if the numpy extension is installed. 
