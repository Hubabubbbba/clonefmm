import networkx as nx
import numpy as np

class Section():

    def __init__(self, _obj) -> None:
        self.section = _obj


    def complement(self):
        pass


    def inverse(self):
        for edge_env in self.section.values():
            edge_env['R+'], edge_env['R-'] = edge_env['R-'], edge_env['R+']
        return self.section
    

    def narrowing(self, set):
        #TODO Добавить валидацию
        pass
    

    def intersection(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def union(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def difference(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def symmetric_difference(self, second_section):
        #TODO Добавить валидацию
        pass
    

    def multiple(self, second_section):
        #TODO Добавить валидацию
        pass
