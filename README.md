# greedy-local-search
Python application with a 3-layered architecture: data access layer ([Domain package](https://github.com/Iri25/ai-greedy-Iri25/tree/master/Domain)), persistence layer ([Repository package](https://github.com/Iri25/ai-greedy-Iri25/tree/master/Repository)) and business layer ([Service package](https://github.com/Iri25/ai-greedy-Iri25/tree/master/Service)). The input and output data are saved in txt files ([Data package](https://github.com/Iri25/ai-greedy-Iri25/tree/master/Data)). To start the application, run in the [main.cpp](https://github.com/Iri25/ai-greedy-Iri25/blob/master/main.py) file.

The key concepts are heuristic methods and the Greedy local search technique.

Application for the Greedy local search heuristic method which solves the shortest path problem. A project manager must arrive at a discussion with a potential client. His agenda is very busy, having a lot of meetings. Being pressed for time, he wants to take the shortest route to the customer's destination. Based on the address he has, the iMap app gives him several routes to reach his destination, each route marked with an estimated travel time. The application allows the following operations:
1. Find the shortest path that starts from a location, visits all locations (each location is visited only once, except the start location which is visited exactly 2 times), and returns to the start location.
2. Identify the shortest route that starts from one location (source) and arrives at another location (destination), each location in the route being visited only once.
