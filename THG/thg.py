import turtle
import tkinter
from unittest.mock import Mock
from .style_config import *
from .nodes_drawer import draw_nodes
from .arcs_drawer import draw_arc_from_origin_to_dest
from .matrix import get_matrix_header_letters, get_empty_matrix


class Graph:
    def __init__(self,nodes,connections):
        self.nodes = nodes
        self.connections = connections
        self.dect = {value:key for key,value in enumerate(self.nodes)}
        self.dect_rev = {key:value for key,value in enumerate(self.nodes)}
    # init from number of nodes
    @classmethod
    def initFromNodesNumber(cls,num_of_nodes,connections):
        list_of_nodes = get_matrix_header_letters(num_of_nodes)
        return cls(list_of_nodes, connections)
    @classmethod
    def initCompletGraph(cls,nodes):
        connections = []
        for node in nodes:
            for node2 in nodes:
                if (node != node2):
                    connections.append((node,node2))
        return cls(nodes, connections)
    @classmethod
    def initWithDergree2(cls,nodes):
        connections = []
        for i in range(0,len(nodes)-1):
            connections.append((nodes[i], nodes[i+1]))
        connections.append((nodes[-1], nodes[0]))
        return cls(nodes, connections)


    def speed(self, speed_num):
        self.speed_num = speed_num
  

    def get_degree(self,node):
        x = self.create_matrix()
        successor = 0
        predecessor = 0
        node_position = self.dect[node]
        for i in range(0,len(self.nodes)):
            successor+= x[node_position][i]
            predecessor+= x[i][node_position]
        return successor + predecessor

    def is_aulerian(self):
        degrees = []
        for node in self.nodes:
            degrees.append(self.get_degree(node))
        print(degrees)
        odd_number_counter = 0
        for i in degrees:
            if ((i%2) != 0):
                odd_number_counter +=1
        if (odd_number_counter == 0):
            return True
        else:
            return False

    def have_aulerian_chain(self):
        degrees = []
        for node in self.nodes:
            degrees.append(self.get_degree(node))
        odd_number_counter = 0
        for i in degrees:
            if ((i%2) != 0):
                odd_number_counter +=1
        if (odd_number_counter == 2):
            return True
        else:
            return False



    def draw(self,*args):
        
        # drawing speed control
        try:
            if (self.speed_num >= 0) and (self.speed_num <=10):
                turtle.speed(self.speed_num)
            else:
                turtle.speed(0)
        except:
            turtle.speed(0)
        # drawing the nodes
        couples_array = draw_nodes(len(self.nodes), self.nodes)
        #dect = {value:key for key,value in enumerate(self.nodes)}
        for connect in self.connections:
            start = self.dect[connect[0]]
            end = self.dect[connect[1]]
            draw_arc_from_origin_to_dest(start,end,couples_array,'black')

        if 'aulerian_chain' in args:
            if self.have_aulerian_chain():

                degrees = []
                for node in self.nodes:
                    degrees.append(self.get_degree(node))
                odd_degree_nodes = []
                for i in range(0,len(degrees)):
                    if ((degrees[i]%2) != 0):
                        odd_degree_nodes.append(self.dect_rev[i])
                arcs = self.connections
                chemin = []
                tmp = odd_degree_nodes[0]
                while (len(arcs)> 1):
                    for arc in arcs:
                        if (arc[0] == tmp) and (arc != (odd_degree_nodes[1],odd_degree_nodes[0])):
                            chemin.append(arc)
                            tmp = arc[1]
                            arcs.remove(arc)
                            break
                chemin.append((tmp,odd_degree_nodes[1]))
                for c in chemin:
                    start = self.dect[c[0]]
                    end = self.dect[c[1]]
                    draw_arc_from_origin_to_dest(start,end,couples_array,'red')
            else:
                print("We can't draw this because is not aulerain")    
        tkinter.mainloop()

    def create_matrix(self):
        """_summary_
            this function take the the nodes of the graph object and it connections and it generate un adjacency matrix
        Returns:
            Matrix: a square matrix where there is 1 in each connection 
        """
        # l is a list that countains an sequer array shape(num_of_nodes,num_of_nodes)
        l = get_empty_matrix(len(self.nodes))
        #dect = {value:key for key,value in enumerate(self.nodes)}
        for x in self.connections:
            row_char = x[0]
            column_char = x[1]
            row_value = self.dect[row_char]
            column_value = self.dect[column_char]
            #print(f'the column value : {column_value}, and the row value : {row_value}')
            l[row_value][column_value] = 1
        return l

    def print_matrix(self,matrix):
        print("")
        l = matrix
        # The number of entries on any line of the matrix gives us the number of nodes. It is a square matrix anyway
        #number_of_nodes = len(l)

        # print header
        headers = self.nodes
        for i in range(0, len(self.nodes)):
            print("\t", headers[i], sep="", end="")
        print("")

        # print an underline for the header
        for i in range(0, len(self.nodes)):
            print("\t-", sep="", end="")

        # print another empty line
        print("")

        # Below we are printing the content of the matrix
        i = -1  # intialise a counter i
        for sub_list in l:
            i = i + 1
            print("\n", headers[i], "|\t", end="")
            for data in sub_list:
                print(data, "|\t", end="")
            # print empty line
            print("")

    def have_circle(self, *args):
        successor_dict = {}
        for node in self.nodes:
            sub_list = []
            for arc in self.connections:
                if arc[0] == node:
                    sub_list.append(arc[1])
            successor_dict[node] = sub_list
        i=0
        while (i < len(self.nodes)):
            if len(successor_dict) == 1:
                if 'show_steps' in args:
                        print(successor_dict)
                successor_dict = {}
                break
            try:
                if (successor_dict[self.nodes[i]] == []):
                    tmp = self.nodes[i]
                    if 'show_steps' in args:
                        print(successor_dict)
                    for node2 in self.nodes:
                        try:  
                            successor_dict[node2].remove(tmp)
                        except:
                            pass
                    del successor_dict[tmp]
                    i=0
                else:
                    i+=1
            except:
                break
        if 'show_steps' in args:
                        print(successor_dict)
        if (successor_dict == {}):
            return False
        else:
            return True 
        



    


