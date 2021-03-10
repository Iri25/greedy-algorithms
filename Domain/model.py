class Town:

    def __init__(self, start_edge, finish_edge, cost):
        '''
        Creates a new town object.
        :param start_edge: the beginning of the edge
        :param finish_edge: the end of the edge
        :param cost: the cost of the edge
        '''
        self.start_edge = start_edge
        self.finish_edge = finish_edge
        self.cost = cost

    def get_start_edge(self):
        '''
        Gets the beginning of the edge
        :return: the beginning of the edge
        '''
        return self.start_edge

    def get_finish_edge(self):
        '''
        Gets the end of the edge
        :return: he end of the edge
        '''
        return self.finish_edge

    def get_cost(self):
        '''
        Gets the cost of the edge
        :return: the cost of the edge
        '''
        return self.cost

    def set_start_edge(self, start):
        '''
        Sets the beginning of the edge
        :param start: the new beginning of the edge
        :return: the new beginning of the edge
        '''
        self.start_edge = start

    def set_finish_edge(self, end):
        '''
        Gets the end of the edge
        :param end: the new end of the edge
        :return: the new end of the edge
        '''
        self.finish_edge = end

    def set_cost(self, cost):
        '''
        Gets the cost of the edge
        :param cost: the new cost of the edge
        :return: the new cost of the edge
        '''
        self.cost = cost

