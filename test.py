from THG import Graph


# this graphe has 7 nodes , with some connections between the them in order to not get the aulerian cirlce or graphe
"""
nodes = ['1','2','3','4','5','6','7']
connections = []
for i in range(0,3):
    for j in range(3,7):
        connections.append((nodes[i], nodes[j]))
g1 = Graph(nodes,connections)
g1.speed(0)
b, deg = g1.is_aulerian()
print(f'is the graphe aulerian "{b}" and this is Why :  {deg}')
b,deg = g1.have_aulerian_chain()
print(f'is the graphe have an aulerian chain "{b}" and this is Why :  {deg}')
g1.draw()  
"""


# this graphe has 5 nodes , with some connects between them in order to get an aulerian graphe
"""
nodes = ['A','B','C','D','E']
connections = [('A','B'),('B','A'),('A','C'),('C','A'),('B','C'),('C','B'),('D','C'),('C','D'),('E','C'),('C','E'),('D','E'),('E','D')]
g1 = Graph(nodes,connections)
b, deg = g1.is_aulerian()
print(f'is the graphe aulerian "{b}" and this is Why :  {deg}')
g1.draw()
"""
# this graphe has 5 nodes , with some connects between them in order to get an aulerian chain
"""
nodes = ['1','2','3','4','5'] 
connections = [('1','3'),('1','5'),('2','4'),('3','2'),('4','1'),('5','2')]
g1 = Graph(nodes,connections)
b, deg = g1.have_aulerian_chain()
print(f'is the graphe have an aulerian chain "{b}" and this is Why :  {deg}')
g1.speed(7)
g1.draw('aulerian_chain')
"""

# we check if this graphe have a circle (False)
"""
nodes = ['1','2','3','4']
connections = [('1','3'),('1','2'),('2','3'),('4','3'),('4','1')]
g1 = Graph(nodes,connections)
print('this graphe has a circle : ',g1.have_circle('show_steps'))
g1.draw()
"""



# we check if this graphe have a circle (True) + print the matrix adjacence
"""
nodes = ['1','2','3','4','5'] 
connections = [('1','3'),('1','5'),('2','4'),('3','2'),('4','1'),('5','2')]
g1 = Graph(nodes,connections)
m = g1.create_matrix()
g1.print_matrix(m)
print('\n')
print('this graphe has a circle : ',g1.have_circle('show_steps'))
g1.draw()

"""



# draw a complete Graphe
"""
nodes = ['X1','X2','X3','X4','X5','X6']
g1 = Graph.initCompletGraph(nodes)
g1.draw()
"""

# draw the second degree Graphe
"""
nodes = ['X1','X2','X3','X4','X5','X6']
g1 = Graph.initWithDergree2(nodes)
g1.draw()
"""










