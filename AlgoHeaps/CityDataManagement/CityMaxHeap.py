from typing import List

from AlgoHeaps.CityDataManagement.AbstractCityHeap import AbstractCityHeap
from AlgoHeaps.CityDataManagement.City import City


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
        # implemented
        index = len(self.heapStorage)-1
        while self.has_parent(index) and \
                self.get_city_population(self.get_parent_index(index)) < self.get_city_population(index):
            self.swap_nodes(index, self.get_parent_index(index))
            index = self.get_parent_index(index)



    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        # implemented
        # root
        if index == 0:
            return
        parent_index = self.get_parent_index(index)


        if self.get_city_population(index) > self.get_city_population(parent_index):
            self.swap_nodes(index, parent_index)
            index = parent_index
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
        # IMPLEMENTED
        index = 0
        while self.has_left_child(index):
            # Find the index of the largest child
            largest_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.get_right_child_population(index) > self.get_left_child_population(index):
                largest_child_index = self.get_right_child_index(index)

            # If the value of the largest child is greater than the value of the current node, swap the nodes
            if self.get_city_population(largest_child_index) > self.get_city_population(index):
                self.swap_nodes(index, largest_child_index)
                index = largest_child_index
            else:
                break

    def heapify_down_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive downwards.
        """
        # implemented
        largest = index
        left_child = self.get_left_child_index(index)
        right_child = self.get_right_child_index(index)

        if left_child < len(self.heapStorage) and self.get_city_population(left_child) > self.get_city_population(largest):
            largest = left_child
        if right_child < len(self.heapStorage) and self.get_city_population(right_child) > self.get_city_population(largest):
            largest = right_child
        if largest != index:
            self.swap_nodes(index, largest)
            self.heapify_down_recursive(largest)


    def remove(self):
        """
        Remove a City from the Max-Heap
        """
        # implemented
        #
        # Store the value of the root node in a temporary variable
        root_city_to_be_removed = self.heapStorage[0]
        print(root_city_to_be_removed, " has been removed. Heapifying...")
        # Replace the root with the last element in the heap
        self.heapStorage[0] = self.heapStorage[-1]
        self.heapStorage.pop()

        # Maintain the heap property for the entire heap
        self.heapify_down_iterative()
        print("Root is ", self.heapStorage[0])





