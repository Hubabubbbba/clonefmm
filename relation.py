import networkx as nx
import numpy as np
from classes.matrix import Matrix
from classes.digraph import DiGraph
from classes.section import Section


class Relation:

    def __init__(self, _obj):

        if (isinstance(_obj, np.matrix)):
            if _obj.shape[0] != _obj.shape[1]:
                raise ValueError('The matrix must be square')
            elif set(_obj.flatten().tolist()[0]) != {0,1}:
                raise ValueError('The matrix must consist of "0" and "1" ')
            self.obj = Matrix(_obj)
            
        elif (isinstance(_obj, nx.classes.DiGraph)):
            #TODO добавить валидацию на граф, кто сможет придумать
            self.obj = DiGraph(_obj)
        
        elif (isinstance(_obj, dict)):
            # Исходный объект является представлением сечениями
             #TODO добавить валидацию на представление сечением, кто сможет придумать
            self.obj = Section(_obj)

        else:
            raise ValueError("Incorrect type")

    

    def complement(self):
        """
        Операция дополнения
        """
        return self.obj.complement()
    

    def inverse(self):
        """
        Операция обращения
        """
        return self.obj.inverse()
    

    def narrowing(self, set):
        """
        Операция сужения на множество
        """
        return self.obj.narrowing(set)
    

    def intersection(self, second_relation):
        """
        Операция пересечения
        """
        return self.obj.intersection(second_relation)
    

    def union(self, second_relation):
        """
        Операция объединения
        """
        return self.obj.union(second_relation)
    

    def difference(self, second_relation):
        """
        Операция разности
        """
        return self.obj.difference(second_relation)
    

    def symmetric_difference(self, second_relation):
        """
        Операция симетрической разности
        """
        return self.obj.symmetric_difference(second_relation)
    

    def multiple(self, second_relation):
        """
        Операция произведения
        """
        return self.obj.multiple(second_relation)
