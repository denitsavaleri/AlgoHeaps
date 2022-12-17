from typing import List
from AlgoHeaps.CityDataManagement.City import City
from AlgoHeaps.CityDataManagement.AbstractCityHeap import AbstractCityHeap


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative upwards.
        """
        # TODO: implement me!
        # i think it works
        index = len(self.heapStorage)-1
        while self.has_parent(index) and \
                self.get_city_population(self.get_parent_index(index)) < self.get_city_population(index):
            self.swap_nodes(index, self.get_parent_index(index))
            index = self.get_parent_index(index)



    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        # TODO: implement me!
        parent_index = self.get_parent_index(index)
        self.get_city_population(index)

        if self.get_city_population(index) > self.get_city_population(parent_index):
            self.swap_nodes(index, parent_index)
            index -= 1
            self.heapify_up_recursive(index)




    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions for a Max-Heap via Floyds Heap Construction Algorithmus.
        
        """
        # TODO: implement me!
        ...

    def heapify_down_iterative(self):
        """
        Establish heap conditions for a Max-Heap iterative downwards.
        """
        # TODO: implement me!
        # i think it works
        largest = 0
        for i in range(0,len(self.heapStorage)):
            if self.get_city_population(i) < self.get_left_child_population(i):
                largest = self.get_left_child_index(i)
            if self.get_city_population(i) < self.get_right_child_population(i):
                largest = self.get_right_child_index(i)
            self.swap_nodes(i, largest)

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # TODO: implement me!
        # index = root
        largest = index
        left_child = self.get_left_child_index(index)
        right_child = self.get_right_child_index(index)

        if left_child < len(self.heapStorage) and self.heapStorage[left_child].population > self.heapStorage[largest].population:
            largest = left_child
        if right_child < len(self.heapStorage) and self.heapStorage[right_child].population > self.heapStorage[largest].population:
            largest = right_child
        if largest != index:
            self.swap_nodes([index], largest)
            self.heapify_down_recursive(largest)


    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # TODO: implement me!


