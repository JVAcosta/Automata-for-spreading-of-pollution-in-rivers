import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import copy
img = mpimg.imread('C:\\Users\\joaov\\Documents\\projetos\\Python\\Automata-for-spreading-of-pollution-in-rivers\\base.PNG')
#for x in img:


not_river_rgb_np_array = ([1,1,1,1],[0,1,0,1],None) #[0. 1. 0. 1.] esse tbm
not_river =  np.array(not_river_rgb_np_array)
l = list(img)

def np_img_to_grid_list(np_list_image, not_river = []):
    result = []
    for line in np_list_image:
        line_r = []
        for pixel in line:
            list_pixel = list(pixel) 
            list_pixel = None if not(list_pixel in not_river) else 0
            line_r.append(list_pixel)
        result.append(line_r)
    return result

def set_up_grid_from_list(grid, init_value):
    new_line = []
    for pixel in grid[-1]:
        if pixel == 0:
            new_line.append(init_value)
        else:
            new_line.append(None)
    grid[-1] = new_line
    return grid

def getVerticalNeighbors(tuple_loc):
        result = []
        check = lambda x,y : (x,y) if x>=0 and y>=0 else None

        l = tuple_loc[0]-1
        c = tuple_loc[1]
        up = check(l ,c)
        result.append(up)
    
        l = tuple_loc[0]
        c = tuple_loc[1]-1
        left = check(l ,c)
        result.append(left)
    
        l = tuple_loc[0]+1
        c = tuple_loc[1]
        down =check(l ,c)
        result.append(down)
    
        l = tuple_loc[0]
        c = tuple_loc[1]+1
        rigth = check(l ,c)
        result.append(rigth)
        
        return result

def getObliqueNeighbors(tuple_loc):
        result = []
        check = lambda x,y : (x,y) if x>=0 and y>=0 else None

        l = tuple_loc[0]-1
        c = tuple_loc[1]-1
        up_left = check(l ,c)
        result.append(up_left)
    
        l = tuple_loc[0]+1
        c = tuple_loc[1]-1
        down_left = check(l ,c)
        result.append(down_left)
    
        l = tuple_loc[0]+1
        c = tuple_loc[1]+1
        down_rigth = check(l ,c)
        result.append(down_rigth)
    
        l = tuple_loc[0]-1
        c = tuple_loc[1]+1
        up_rigth = check(l ,c)
        result.append(up_rigth)
        
        return result
#m0.1 d0.2
def without_w_c_vertical(m, M, M_up, M_left, M_rigth, M_down):
    M_up = M_up - M if M_up else 0
    M_left = M_left - M if M_left else 0
    M_rigth = M_rigth - M if M_rigth else 0
    M_down = M_down - M if M_down else 0
    return  m*(M_up + M_left + M_rigth + M_down)

def without_w_c_oblique(m, d, M, M_up_left, M_down_left, M_down_rigth, M_up_rigth):
    M_up_left = M_up_left - M if M_up_left else 0
    M_down_left = M_down_left - M if M_down_left else 0
    M_down_rigth = M_down_rigth - M if M_down_rigth else 0
    M_up_rigth = M_up_rigth - M if M_up_rigth else 0
    return  m*d*(M_up_left + M_down_left + M_down_rigth + M_up_rigth)

def getPixelValue(grid,tuple_loc):
    if tuple_loc == None:
        return 0
    l, c = tuple_loc
    try:
        r = grid[l][c]
        if r == None:
            return 0
        return r
    except IndexError:
        return 0


def run(grid,m, d):
    new_grid = copy.deepcopy(grid) # all parts of gri
    lines = len(new_grid)
    columns = len(new_grid[0])
    for l in range(lines):
        for c in range(columns):
            M = grid[l][c]
            if M == None:
                continue

            list_v_neighbors = getVerticalNeighbors((l,c))
            
            v_values = tuple((getPixelValue(grid, t) for t in list_v_neighbors))
            
            M_up, M_left, M_rigth, M_down = v_values

            list_O_neighbors = getVerticalNeighbors((l,c))
            o_values = (getPixelValue(grid, t) for t in list_O_neighbors)
            M_up_left, M_down_left, M_down_rigth, M_up_rigth = o_values

            spread_v = without_w_c_vertical(m, M, M_up, M_left, M_rigth, M_down)

            spread_o = without_w_c_oblique(m, d, M, M_up_left, M_down_left, M_down_rigth, M_up_rigth)
            
            new_grid[l][c] = M + spread_v + spread_o
         
    return new_grid

def processor(base_grid, times, m , d):
    grid_list_t = []

    for i in range(times):
        new_t_grid = run(base_grid, m, d)
        # grid_list_t.append(new_t_grid)
        base_grid = new_t_grid
    grid_list_t.append(base_grid)
    return grid_list_t

def line_to_rgb(lista):
    l_r = []
    for i in lista:
        if i  == None:
            no_clean_water = [1.0, 1.0, 1.0]
            l_r.append(no_clean_water)
        elif i < 0.01:
            clean_water = [0.039215688, 0.29803923, 0.42352942]
            l_r.append(clean_water)
    
        else:
            no_clean_water = [0.8901961, 0.8862745, 0.8862745] 
            l_r.append(no_clean_water)
        
    return l_r

base_grid = np_img_to_grid_list(img, not_river_rgb_np_array)
grid = set_up_grid_from_list( base_grid ,3 )
m = 0.1
d = 0.2
result = processor(grid, 100, m, d)
rgb_result = []
for grid in result:
    r_grid = []
    for line in grid:
        rgb_line = line_to_rgb(line)
        r_grid.append(rgb_line)
    rgb_result.append(r_grid)

resultTest = rgb_result[0]
for i in result:
    print(i)

# print(grid[243][275])
# print(base_grid)
plt.show(plt.imshow(resultTest))