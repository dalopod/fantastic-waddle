import random

class worldGenerator:

        # Combine with generate later?
        def __init__(self):
            self.worldMap = None
            self.seed = None
            self.randomGen = None

        # Generates the world map by creating locations(nodes) and linking them together.
        def generate(self, numLocations):
            #self.randomGen = Random()
            #self.seed = seed
            self.worldMap = Graph()
            self.generateNodes(numLocations)
            self.connectNodes(numLocations)
            self.generateExtraPaths(numLocations)

        # Generate nodes     
        def generateNodes(self, numLocations):
            self.worldMap.root = self.generateSingleNode()
            self.worldMap.root.name = str(0)
            self.worldMap.nodes = []
            self.worldMap.nodes.append(self.worldMap.root)
            for i in range(1,numLocations):
                self.worldMap.nodes.append(self.generateSingleNode())
                self.worldMap.nodes[i].name = str(i)

        # Connect nodes
        def connectNodes(self, numLocations):
            for i in range(0, numLocations):
                neighborIndex = i
                while (i == neighborIndex):
                    neighborIndex = random.randrange(numLocations)
                    self.generatePathBetween(self.worldMap.nodes[i], self.worldMap.nodes[neighborIndex])
                

        # Generates locations(nodes) that contain a name, sublocations(subnodes), and entities. These are things like towns, forests, etc.
        def generateSingleNode(self):
            node = Node()
            
            return node

        # Generations sublocations(subnodes). These are things like buildings, dungeon rooms, monuments, etc.
        def generateSubNode(self):
            node = Node()
            
            return node

        # Generate a path between two points.
        def generatePathBetween(self, node1, node2):
            paths = self.generatePathNodes()
            pathsLength = len(paths)
            self.worldMap.connectNodes(node1, paths[0])
            self.worldMap.connectNodes(paths[pathsLength-1], node2)
        
        # Generate a number of paths 
        def generatePathNodes(self):
            paths = []
            node = self.generateSingleNode() # should pass a "path" or "road" parameter
            node.name = "path"
            self.worldMap.nodes.append(node)
            paths.append(node)
            return paths

        def generateExtraPaths(self, numLocations):
            numPaths = random.randrange(numLocations)
            for i in range(0, numPaths):
                firstLocation = random.randrange(len(self.worldMap.nodes))
                secondLocation = firstLocation
                while (firstLocation == secondLocation): # need (and not a city) clause here
                    secondLocation = random.randrange(len(self.worldMap.nodes))
                self.generatePathBetween(self.worldMap.nodes[firstLocation], self.worldMap.nodes[secondLocation])

        def visualizeWorld(self):
            self.worldMap.printGraph()
        
        


class Graph:

    def __init__(self):
        self.root = None
        self.nodes = []

    def connectNodes(self, node1, node2):
        node1.addNeighbor(node2)
        node2.addNeighbor(node1)

    def removeConnection(self, node1, node2):
        node1.removeNeighbor(node2)
        node2.removeNeighbor(node1)

    def printGraph(self):
        for i in range(0, len(self.nodes)):
            print("\nNode:" + self.nodes[i].name)
            for j in range(0, len(self.nodes[i].neighbors)):
                print("\n     " + self.nodes[i].neighbors[j].name)
        


class Node:

    def __init__(self):
        # Name of location
        self.name = None

        # Locations reachable by this location.
        self.neighbors = []

        # Sublocations for this location. For a town this might be buildings or districts, for a building this might be rooms.
        self.subGraph = None

        # List of entities. These are people, creatures, objects, etc.
        self.entities = []

    def addNeighbor(self, node):
        self.neighbors.append(node)

    def removeNeighbor(self, node):
        self.neighbors.remove(node)
