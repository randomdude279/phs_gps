#imports and changes the recursion limit
import sys

sys.setrecursionlimit(20000)


class Node:
    def __init__(self, nodeID, connectedTo, classroom=[], render_coords = [0,0]):
        self.nodeID = str(nodeID)
        self.connectedTo = connectedTo
        self.classroom = classroom
        self.render_coords = render_coords 

        #for debuging

    #def #print_attributes(self):
    ##print(self.nodeID)
    ##print(self.connectedTo)
    ##print(self.classroom)


class Route:
    def __init__(self, routeString, routeArray):
        self.routeString = routeString
        self.routeArray = routeArray
        self.arrayLength = len(routeArray)
        # more stuff will likely be added


nodes = {}
nodes['1'] = Node(1, [2], ["Aud", "64", "63"], ["238","365"])
nodes['2'] = Node(2, [1, 3], ["61", "62", "Globe", "Foyer"],["243","320"])
nodes['3'] = Node(3, [2, 4, 10], ["54", "Health"],["243","269"])
nodes['4'] = Node(4, [3, 5, 24], ["52", "55", "44"],["134","272"])
nodes['5'] = Node(5, [4, 6, 23], ["36", "42"],["182","195"])
nodes['6'] = Node(6, [5, 7], ["37", "Media Center", "MC"],["216","195"])
nodes['7'] = Node(7, [6, 8], ["Senior Bench", "SB", "16", "17"],["296","190"])
nodes['8'] = Node(8, [7, 9, 10, 20], ["18", "15", "14"],["356","197"])
nodes['9'] = Node(9, [8, 15, 14], ["20", "19"],["425","198"])
nodes['10'] = Node(10, [3, 8, 11], ["13", "12", "57", "58"],["356","275"])
nodes['11'] = Node(11, [10, 12], ["Boy's Lockers", "BLR"],["408","275"])
nodes['12'] = Node(12, [11, 13], ["Gym", "Girl's Lockers", "GLR"], ["464","273"])
nodes['13'] = Node(13, [12, 15, 14], ["Gym Exit"],["521","272"])
nodes['14'] = Node(14, [13, 15, 9], ["Science Building","Sci"],["539","429"])
nodes['15'] = Node(15, [13, 14], ["Portables"],["584","24"])
nodes['16'] = Node(16, [18], ["33A", "33B", "33", "26", "26A"],["470","93"])
nodes['17'] = Node(17, [18], ["Weight Room", "Weights", "32", "31", "29"],["147","70"])
nodes['18'] = Node(18, [16, 17, 19], ["28"],["428","100"])
nodes['19'] = Node(19, [20, 18], ["27", "26"],["354","104"])
nodes['20'] = Node(20, [8, 19, 21], ["23", "24", "22", "21"],["356","145"])
nodes['21'] = Node(21, [22, 20], ["Cafeteria"],["281","141"])
nodes['22'] = Node(22, [21, 5], ["34", "35"],["182","142"])
nodes['23'] = Node(23, [5], ["Bus Exit", "45", "Exit"], ["761","192"])
nodes['24'] = Node(24, [4], ["51"],["100","275"])


def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2


def Recursive(routes, nodeHistory=[], endpoint='', debugTab=0):
    global nodes
    #print(' ' * debugTab + 'ATTEMPTING: ' + str(nodeHistory))

    # CHECK IF THE CURRENT CONFIG IS GOOD
    if str(nodeHistory[-1]) == endpoint:
        #if we have found a viable route
        routes.append(Route('', nodeHistory))
        #print(' ' * debugTab + 'Route found: '+str(nodeHistory))
        return None
        #terminate searching and move back up one level of recursivity

    # GET ALL NEXT STEPS
    possibleNextSteps = []
    possibleNextSteps2 = []

    for i in nodes[str(nodeHistory[-1])].connectedTo:
        possibleNextSteps.append(i)
        possibleNextSteps2.append(i)
        # when we did pNS = nodes[...].connectedTo

    #print(nodes[str(nodeHistory[-1])].connectedTo)

    #print(' ' * debugTab + f'Considering {possibleNextSteps}')
    # MAKE SURE WE DON'T LOOP BACK ON PRIOR NODES
    for i in possibleNextSteps:
        if str(i) in nodeHistory:
            possibleNextSteps2.remove(i)

    possibleNextSteps = possibleNextSteps2
    #print(' ' * debugTab + f'Going to try {possibleNextSteps}')
    # IF THERE IS NO WAY TO GET BACK WITHOUT BACKTRACKING, STOP
    if len(possibleNextSteps) == 0:
        #print(' ' * debugTab + 'This routing is dead.')
        return None

    # TRY ALL ROUTES CONSIDERED
    for i in possibleNextSteps:
        #print(' ' * debugTab + '└',end='')
        #pass all the same information, including the refernce to the output array
        Recursive(routes, nodeHistory + [str(i)], endpoint, debugTab + 4)
