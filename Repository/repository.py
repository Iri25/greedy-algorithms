from Domain.model import Town

class Repository:

    def __init__(self, filename):
        '''
        Creates a new repository object.
        :param filename: the input file
        '''
        self.filename = filename
        self.repository = []
        self.size = 0
        self.start = 0
        self.finish = 0

    def load_file(self):
        '''
        Loads data from the input file
        :return:
        '''
        f = open(self.filename, "r")
        x = f.readline()
        self.size = int(x)
        for i in range(self.size):
            count = 1
            for j in f.readline().strip().split(","):
                edge = Town(i + 1, count, int(j))
                self.repository.append(edge)
                count = count + 1
        self.start = int(f.readline())
        self.finish = int(f.readline())
        f.close()

    def get_start(self):
        '''
         Gets the beginning of the road
        :return: the beginning of the road
        '''
        return self.start

    def get_finish(self):
        '''
        Gets the end of the road
        :return: the end of the road
        '''
        return self.finish

    def get_adjacent_list(self):
        '''
        Creates an adjacent list
        :return: the adjacent list
        '''
        list = []
        f = open(self.filename, "r")
        x = f.readline()
        for i in range(int(x)):
            list.append([])
            for j in f.readline().strip().split(","):
                list[i].append(int(j))
        return list
