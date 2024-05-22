# Initialize grid using nested functions for a 5x5 grid
def cell_00(): return 0
def cell_01(): return 0
def cell_02(): return 0
def cell_03(): return 0
def cell_04(): return 0

def cell_10(): return 0
def cell_11(): return 0
def cell_12(): return 0
def cell_13(): return 0
def cell_14(): return 0

def cell_20(): return 0
def cell_21(): return 0
def cell_22(): return 0
def cell_23(): return 0
def cell_24(): return 0

def cell_30(): return 0
def cell_31(): return 0
def cell_32(): return 0
def cell_33(): return 0
def cell_34(): return 0

def cell_40(): return 0
def cell_41(): return 0
def cell_42(): return 0
def cell_43(): return 0
def cell_44(): return 0

# A simple linear congruential generator (LCG) for pseudo-random numbers
def lcg(seed):
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = (a * seed + c) % m
    return seed

# Plant pumpkins with an 80% chance of survival using LCG
def plant_pumpkins(seed):
    global cell_00, cell_01, cell_02, cell_03, cell_04
    global cell_10, cell_11, cell_12, cell_13, cell_14
    global cell_20, cell_21, cell_22, cell_23, cell_24
    global cell_30, cell_31, cell_32, cell_33, cell_34
    global cell_40, cell_41, cell_42, cell_43, cell_44

    def plant_cell(seed):
        seed = lcg(seed)
        if seed % 10 < 8:  # 80% chance
            return 1
        else:
            return 0

    cell_00 = plant_cell(seed)
    cell_01 = plant_cell(cell_00)
    cell_02 = plant_cell(cell_01)
    cell_03 = plant_cell(cell_02)
    cell_04 = plant_cell(cell_03)

    cell_10 = plant_cell(cell_04)
    cell_11 = plant_cell(cell_10)
    cell_12 = plant_cell(cell_11)
    cell_13 = plant_cell(cell_12)
    cell_14 = plant_cell(cell_13)

    cell_20 = plant_cell(cell_14)
    cell_21 = plant_cell(cell_20)
    cell_22 = plant_cell(cell_21)
    cell_23 = plant_cell(cell_22)
    cell_24 = plant_cell(cell_23)

    cell_30 = plant_cell(cell_24)
    cell_31 = plant_cell(cell_30)
    cell_32 = plant_cell(cell_31)
    cell_33 = plant_cell(cell_32)
    cell_34 = plant_cell(cell_33)

    cell_40 = plant_cell(cell_34)
    cell_41 = plant_cell(cell_40)
    cell_42 = plant_cell(cell_41)
    cell_43 = plant_cell(cell_42)
    cell_44 = plant_cell(cell_43)

    return seed

# Check if a giant pumpkin can be formed
def check_giant_pumpkin(row, col, size):
    global cell_00, cell_01, cell_02, cell_03, cell_04
    global cell_10, cell_11, cell_12, cell_13, cell_14
    global cell_20, cell_21, cell_22, cell_23, cell_24
    global cell_30, cell_31, cell_32, cell_33, cell_34
    global cell_40, cell_41, cell_42, cell_43, cell_44

    def get_cell_value(r, c):
        return globals()[f'cell_{r}{c}']

    for i in range(size):
        for j in range(size):
            if get_cell_value(row + i, col + j) == 0:
                return False
    return True

# Harvest pumpkins and calculate yield
def harvest_pumpkins():
    global cell_00, cell_01, cell_02, cell_03, cell_04
    global cell_10, cell_11, cell_12, cell_13, cell_14
    global cell_20, cell_21, cell_22, cell_23, cell_24
    global cell_30, cell_31, cell_32, cell_33, cell_34
    global cell_40, cell_41, cell_42, cell_43, cell_44

    def clear_cells(row, col, size):
        for i in range(size):
            for j in range(size):
                globals()[f'cell_{row + i}{col + j}'] = 0

    size = 5
    total_yield = 0

    for row in range(size - 3):
        for col in range(size - 3):
            if check_giant_pumpkin(row, col, 4):
                total_yield += 64
                clear_cells(row, col, 4)

    for row in range(size - 2):
        for col in range(size - 2):
            if check_giant_pumpkin(row, col, 3):
                total_yield += 27
                clear_cells(row, col, 3)

    for row in range(size - 1):
        for col in range(size - 1):
            if check_giant_pumpkin(row, col, 2):
                total_yield += 8
                clear_cells(row, col, 2)

    for row in range(size):
        for col in range(size):
            if globals()[f'cell_{row}{col}'] == 1:
                total_yield += 1

    return total_yield

# Simulate the pumpkin growth process
def simulate_pumpkin_growth(grid_size, iterations):
    total_yield = 0
    seed = 123456  # Initial seed value
    for i in range(iterations):
        seed = plant_pumpkins(seed)
        total_yield += harvest_pumpkins()
    return total_yield / iterations

# Set parameters and run the simulation
grid_size = 5
iterations = 1000
average_yield = simulate_pumpkin_growth(grid_size, iterations)
print("Average pumpkin yield over", iterations, "iterations:", average_yield)
