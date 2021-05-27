class graph():
    def __init__(self):
        self.data = None
        self.ne = []
        self.nei = []
        self.iv = None
        
#f = open('graph_info.txt', 'r')
#line_data = f.readline()
#line_save=[]
#while line_data:
    #line_save.append(line_data)
    #print("%s" %line_data, end="")
    #print("\n")
    #line_data = f.readline()
#f.close

    
A,B,C,D,E,F,G,current = graph(),graph(),graph(),graph(),graph(),graph(),graph(),graph()
A.data,B.data,C.data,D.data,E.data,F.data,G.data = "A","B","C","D","E","F","G"
A.ne.append("B"), A.ne.append("C")
B.ne.append("A"), B.ne.append("D"), B.ne.append("E")
C.ne.append("A"), C.ne.append("E")
D.ne.append("B"), D.ne.append("G")
E.ne.append("B"), E.ne.append("C"), E.ne.append("G")
G.ne.append("D"), G.ne.append("E"), G.ne.append("F")
F.ne.append("G")
A.iv,B.iv,C.iv,D.iv,E.iv,F.iv = B,C,D,E,F,G
visited = []
stack = []

def graph_print():
    current = A
    while current != None:
        print(current.data,": {",end = "")
        n = len(current.ne)
        for i in range(0,n):
            print("(",current.data,",",current.ne[i],")",end="")
        print("}")
        current = current.iv

def print_graph():
    current = A
    while current != None:
        print(current.data,": {",end = "")
        n = len(current.nei)
        for i in range(0,n):
            print("(",current.data,",",current.nei[i],")",end="")
        print("}")
        current = current.iv

def graph_edge():
    current = A
    var = 0
    while current != None:
        var += len(current.nei)
        current = current.iv
    return var

def graph_visited(vertex):
    global visited
    n = len(visited)
    if n == 0:
        return False
    else:
        for i in range (0,n):
            if vertex.data == visited[i]:
                return True #vertex가 이미 지나온 vertex인경우 True 값을 반환한다.
            elif ((i == n-1) and (vertex.data != visited[i])) == 1:
                return False #vertex가 지나온 vertex가 아닌경우 False 값을 반환한다.
        
def graph_search(vertexdata):
    current = A
    while current.iv != None:
        if current.data == vertexdata:
            break
        else:
            current = current.iv
    return current
    

def graph_DFS(vertex):
    if (graph_edge() == 12):
        return
    else:
        visited.append(vertex.data)
        n = len(vertex.ne)
        for i in range(0,n):
            if graph_visited(graph_search(vertex.ne[i])) == False:
                stack.append(vertex.data)
                vertex.nei.append(vertex.ne[i])
                graph_search(vertex.ne[i]).nei.append(vertex.data)
                vertex = graph_search(vertex.ne[i])
                graph_BFS(vertex)
                break
            elif (i == n-1) and (graph_visited(graph_search(vertex.ne[i])) == True) == 1:
                m = len(stack)
                vertex = graph_search(stack[m-1])
                stack.pop()
                graph_BFS(vertex)
                
                
def graph_BFS(vertex):
    visited.append(vertex.data)
    n = len(vertex.ne)
    for i in range(0,n):
        if graph_visited(graph_search(vertex.ne[i])) == False:
            vertex.nei.append(vertex.ne[i])
            graph_search(vertex.ne[i]).nei.append(vertex.data)
            stack.append(vertex.ne[i])
            visited.append(vertex.ne[i])
            
    if len(stack)>=1:
        save = stack[0]
        del stack[0]
        graph_BFS(graph_search(save))
        
        


