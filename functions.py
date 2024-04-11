from pyeda.inter import *
import graphviz
import os

def bool_var(number, prefix):
    # Generate boolean variables based on the given number and prefix
    if prefix is None:
        prefix = 'xx'
    
    binary = format(number, '05b')
    temp = []
    
    for i, bit in enumerate(binary):
       
        if bit == '0':
            part = f"~{prefix}{i+1}"
        else:
            part = f"{prefix}{i+1}"
        
        temp.append(part)
    return '&'.join(temp)


def closure(bdd):
    # Compute the closure of a BDD
    while True:
        prime = bdd
        temp = prime or bad_apple(prime, bdd)
        if temp.equivalent(prime):
            break
    return temp


def E_P_lists(temp, y):
    # Generate E/P lists based on the given temp and y
    list = []
    for i in temp:
        temp2 = bool_var(i, y)
        list.append(temp2)
    return '|'.join(list)


def edges():
    # Generate edges for the graph
    temp = []
    for i in range(0, 32):
        for j in range(0, 32):
            if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32:
                node_X = bool_var(i, 'xx')
                node_Y = bool_var(j, 'yy')
                temp.append( node_X + '&' + node_Y)
    return ('|'.join(temp))


def bad_apple(bdd1, bdd2):
   
    Z = [bddvar("zz1"), bddvar("zz2"), bddvar("zz3"), bddvar("zz4"), bddvar("zz5")]     # zz1..zz5 are the variables for the composed graph
    X = [bddvar("xx1"), bddvar("xx2"), bddvar("xx3"), bddvar("xx4"), bddvar("xx5")]     # this is where we are creating the variables for the composed graph
    Y = [bddvar("yy1"), bddvar("yy2"), bddvar("yy3"), bddvar("yy4"), bddvar("yy5")]     
                                                                                    
    bannana = bdd2.compose({X[0]: Z[0], X[1]: Z[1], X[2]: Z[2], X[3]: Z[3], X[4]: Z[4]})
    good_apple = bdd1.compose({Y[0]: Z[0], Y[1]: Z[1], Y[2]: Z[2], Y[3]: Z[3], Y[4]: Z[4]}) 
    
    bad_apple = (bannana & good_apple).smoothing(Z)           #The smoothing function is used to remove the variables that are not in the final expression.
    
    return (bad_apple)   # (RR(xx1,xx2,xx3,xx4,xx5,zz1,zz2,zz3,zz4,zz5)(Bannana) /\ RR(zz1,zz2,zz3,zz4,zz5,yy1,yy2,yy3,yy4,yy5)(good apple))(bad apple) i love zhe dang this guy cracks me up
                                                         


def BDD(X):
    # Convert an expression to a BDD
    return expr2bdd(expr(X))


def visualize_bdd(bdd, filename):
    # Visualize the BDD and save it to a file
    dot = bdd.to_dot()
    graph = graphviz.Source(dot)
    output_directory = os.path.join(os.getcwd(), 'test-output')
    os.makedirs(output_directory, exist_ok=True)  
    graph.render(filename=filename, format='png', view=False, directory=output_directory)
