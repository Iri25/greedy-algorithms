class Service:

    def __init__(self, repository):
        '''
        Creates a new service object.
        :param repository: the repository
        '''
        self.repository = repository

    def get_add_list(self):
        '''
        Gets an adjacent list
        :return: the adjacent list
        '''
        return self.repository.get_adjacent_list()

    def tsp(self, city):
        '''
        TSP algorithm
        :param city: the starting city
        :return: the optimal traversing path that visits all the cities
                 the value of the optimal path through all the cities
        '''
        visited = [0] * (self.repository.size + 1)
        visited[0] = 1
        visited[city] = 1
        copy_city = city

        road = [city]
        result = 0
        while True:
            minimum = 1000000
            count = 1
            for i in self.get_add_list()[city - 1]:
                if minimum >= i != 0 and visited[count] == 0:
                    next_city = count
                    minimum = i
                count = count + 1
            visited[next_city] = 1
            city = next_city
            result = result + minimum
            road.append(city)
            ok = 1
            for i in visited:
                if i == 0:
                    ok = 0
            if ok == 1:
                break
        result = result + self.get_add_list()[city - 1][copy_city - 1]
        return road, result

    def print_tsp(self, city):
        '''
        Prints TSP
        :param city: the starting city
        :return: TSP printing
        '''
        road, result = self.tsp(city)

        f = open("Data/output.txt", "w")
        res = ""
        res = res + str(len(road))
        res = res + "\n"
        for i in road:
            res = res + str(i) + ","
        res = res[:-1]
        res = res + "\n"
        res = res + str(result)
        f.write(res)
        f.close()

    def shortest_path(self):
        '''
        Gets the shortest path
        :return: the optimal traversing path from the source city to the destination city
                 the value of the optimal path from the source city to the destination city
        '''
        visited = [0] * (self.repository.size + 1)
        visited[0] = 1
        visited[self.repository.start] = 1

        road = [self.repository.start]
        result = 0
        while visited[self.repository.finish] == 0:
            minimum = 10000
            count = 1
            for i in self.get_add_list()[self.repository.start - 1]:
                if minimum >= i != 0 and visited[count] == 0:
                    next_city = count
                    minimum = i
                count = count + 1

            if self.get_add_list()[self.repository.start - 1][self.repository.finish - 1] < minimum + self.get_add_list()[next_city - 1][self.repository.finish - 1]:
                result = result + self.get_add_list()[self.repository.start - 1][self.repository.finish - 1]
                road.append(self.repository.finish)
                break

            visited[next_city] = 1
            self.repository.start = next_city
            result = result + minimum
            road.append(next_city)
        return road, result

    def print_shortest_path(self):
        '''
        Prints shortest path
        :return: the shortest path
        '''
        road, result = self.shortest_path()

        f = open("Data/output.txt", "a")
        res = "\n"
        res = res + str(len(road))
        res = res + "\n"
        for i in road:
            res = res + str(i) + ","
        res = res[:-1]
        res = res + "\n"
        res = res + str(result)
        f.write(res)
        f.close()


