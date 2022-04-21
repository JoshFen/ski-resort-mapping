from geopy.distance import geodesic
class Graph:
    def __init__(self):
      self.graph = {}

    def to_string(self):
        for keys in self.graph:
            print('Node: ')
            print(keys)
            if len(self.graph[keys].keys()) < 1:
                print('here')
            else:
                for cons in self.graph[keys]:
                    print('Connections: ')
                    print(cons)
                print('---------------------------------------')

    def get_vertices(self):
        vertices = []
        for key in  self.graph.keys():
            vertices.append(key.node_id)

        return vertices

    def generate_edges(self):
        edges = []
        for key in self.graph:
            s_id = key.node_id
            for con in self.graph[key]:
                edges.append((key, con))
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex] = {}

    def add_edge(self, origin, end):
        self.graph[origin][end] = self.distance(origin, end)



    def distance(self, origin, end):
        p1 = (origin.lat ,origin.lon)
        p2 = (end.lat, end.lon)

        return geodesic(p1,p2)

    def delete_extras(self, node):
        if self.graph[node].keys is None:
            del self.graph[node]

    def dijkstra(self, start, end):
        print('222222222222222222')
        print(start)
        print(end)
        print('222222222222222222')
        parent = {}  # previous node to assist in finding the shortest path
        distance = {}  # shortest path from one node to another
        path = []  # path list to store the path
        s = set()
        queue = []  # creating nodes variable

        i1 = (90.0000, 1235.0000)
        i2 = (0.0000, 45.0000)
        infinity = geodesic(i1, i2)  # Large distance value for distance calculating.

        for vertex in self.graph:  # Iterates for each node/vertex in the graph.
            distance[vertex] = infinity  # Sets the distance to infinity (this case two furthest points on earth).
            parent[vertex] = None  # Sets parent to null since unknown.
            queue.append(vertex)  # Appends the node to the queue.

        i1 = (90.0000, 0.0)
        i2 = (90.0000, 0.0)
        distance[start] = geodesic(i1, i2)  # Sets origins distance to 0.

        while queue:  # Iterates while the queue is not empty.
            cur = queue[0]  # Set current node to first element in the queue.
            for node in queue:  # Iterates for each node in the queue.
                if distance[node] < distance[cur]:  # Finds the node with the smallest distance in the queue.
                    cur = node  # Cur is now this node.

            for neighbor, dist in self.graph[cur].items():  # Iterates for each connection of the current node.
                if distance[cur] + dist < distance[neighbor]:  # Checks the for smallest distance.
                    distance[neighbor] = dist + distance[cur]  # Sets the nodes distance to the smallest distance.
                    parent[neighbor] = cur  # Sets currents new parent node.

            queue.remove(cur)  # Removes visited node from the queue.

        path.append(end)
        while parent[end]:
            path.append(parent[end])
            end = parent[end]

        return path



