class Cell():
    def __init__(self, state=1, pollutionValue=0, tuple_loc=(0, 0)):
        self._state = state
        self._last_state = self._state
        self._pollution_value = pollutionValue
        self._last__pollution_value = self._pollution_value
        self._lat = tuple_loc[0]
        self._lng = tuple_loc[1]
        self._current_step = 0
        self._last_step = 0

    def set_state(self, state):
        self._last_state = self._state
        self._state = state

    def set_pollution_values(self, pv):
        self._last__pollution_value = self._pollution_value
        self._pollution_value = pv

    def add_step_count(self):
        self._current_step += 1

    def get_step_count(self):
        return self._current_step

    def step(self, state, pollutionV):
        self.set_state(state)
        self.set_pollution_values(pollutionV)
        self.add_step_count()

    def get_lat_long(self):
        return (self._lat, self._lng)

    # def __repr__(self):


class Grid():
    def __init__(self, width=100, height=100, list_of_starters_cells=[Cell()]):
        self._hash = {loc: Cell(tuple_loc=loc)
                      for loc in self.build_hash(width, height)}
        for c in list_of_starters_cells:
            self._hash[c.get_lat_long()] = c

        self._current_grid_step = 0
        self._width = width
        self._heigth = height

    def add_grid_step(self):
        self._current_grid_step += 1
        return self._current_grid_step

    def get_grid_step(self):
        return self._current_grid_step

    def build_hash(self, width, heigth):
        r = []
        for w in range(width):
            for h in range(heigth):
                r.append((w, h))
        return r

    def get_hash(self):
        return self._hash

    def getCell(self, tuple_loc):
        return self._hash[tuple_loc]

    def getAllCells(self):
        return self.get_hash().values()

    def getVerticalNeighbors(self, tuple_loc):
        result = []
        try:
            l = tuple_loc[0]-1
            c = tuple_loc[1]
            up = self.get_hash()[(l, c)]
            result.append(up)
        except IndexError:
            pass
        try:
            l = tuple_loc[0]
            c = tuple_loc[1]-1
            left = self.get_hash()[(l, c)]
            result.append(left)
        except IndexError:
            pass
        try:
            l = tuple_loc[0]+1
            c = tuple_loc[1]
            down = self.get_hash()[(l, c)]
            result.append(down)
        except IndexError:
            pass
        try:
            l = tuple_loc[0]
            c = tuple_loc[1]+1
            rigth = self.get_hash()[(l, c)]
            result.append(rigth)
        except IndexError:
            pass
        return result

    def getObliqueNeighbors(self, tuple_loc):
        result = []
        try:
            l = tuple_loc[0]-1
            c = tuple_loc[1]-1
            up_left = self.get_hash()[(l, c)]
            result.append(up_left)
        except IndexError:
            pass
        try:
            l = tuple_loc[0]+1
            c = tuple_loc[1]-1
            down_left = self.get_hash()[(l, c)]
            result.append(down_left)
        except IndexError:
            pass
        try:
            l = tuple_loc[0]+1
            c = tuple_loc[1]+1
            down_rigth = self.get_hash()[(l, c)]
            result.append(down_rigth)
        except IndexError:
            pass
        try:
            l = tuple_loc[0]-1
            c = tuple_loc[1]+1
            up_rigth = self.get_hash()[(l, c)]
            result.append(up_rigth)
        except IndexError:
            pass
        return result

    def getAllNeighbors(self, tuple_loc):
        return self.getVerticalNeighbors(tuple_loc) + self.getObliqueNeighbors(tuple_loc)


class Rule():
    def __init__(self, rule_vertical_function, m, rule_oblique_fuction=lambda x: x, md=None):
        self._rule_v_func = rule_vertical_function
        self._rule_obl_func = rule_oblique_fuction
        self._m_variable = m
        self._md_variable = md

    def get_rule_v(self):
        return self._rule_v_func

    def get_rule_obl(self):
        return self._rule_obl_func

    def get_m_var(self):
        return self._m_variable

    def get_md_var(self):
        return self._md_variable


class Processor():
    def __init__(self, width=100, height=100, list_of_starters_cells=[Cell()], init_cell=(0, 0)):
        self._grid = Grid(width, height, list_of_starters_cells)
        self._init_cell = init_cell

        def f(x, y): return x+y
        m = 0.1
        d = 0.2
        md = m*d
        self._rule = Rule(f, m, f, md)
        self._pass = []

    def stepInit(self):
        self.grid.add_grid_step()
        self.step(self._init_cell)

    def step(self, tuple_loc):
        if (tuple_loc in self._)
        grid=self._grid
        vertical_cells=grid.getVerticalNeighbors(tuple_loc)
        oblique_cells=grid.getObliqueNeighbors(tuple_loc)
        mapV=map(self._rule.get_rule_v(), vertical_cells)
        mapO=map(self._rule.get_rule_obl(), oblique_cells)


# def f(x, y): return x+y
#         m = 0.1
#         d = 0.2
#         md = m*d
#         self._rule = Rule(f, m, f, md)
# print(Grid().get_hash())
