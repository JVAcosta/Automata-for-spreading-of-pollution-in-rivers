from cellular_automaton import *


class MyRule(Rule):

    def init_state(self, cell_coordinate):
        return (1, 1)

    def evolve_cell(self, last_cell_state, neighbors_last_states):
        return self._get_neighbor_by_relative_coordinate(neighbors_last_states, (-1, -1))

    def get_state_draw_color(self, current_state):
        return [255 if current_state[0] else 0, 0, 0]


neighborhood = MooreNeighborhood(
    EdgeRule.IGNORE_MISSING_NEIGHBORS_OF_EDGE_CELLS)

ca = CAFactory.make_single_process_cellular_automaton(dimension=[100, 100],
                                                      neighborhood=neighborhood,
                                                      rule=MyRule)
ca.evolve_x_times(100)
x = ca.get_current_evolution_step()
l = ca.get_cells()
l = [c.get_current_state() for c in l]
print(l)
