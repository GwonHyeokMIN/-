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
A.data,B.data,C.data,D.data,E.data,F.data,G.data = "A","B","C","D","E","F","G"  #A 그래프 에는 "A" 라는 데이터를 입력한다
A.ne.append("B"), A.ne.append("C")  #A에 이웃한 그래프의 데이터를 입력해둔다
B.ne.append("A"), B.ne.append("D"), B.ne.append("E")
C.ne.append("A"), C.ne.append("E")
D.ne.append("B"), D.ne.append("G")
E.ne.append("B"), E.ne.append("C"), E.ne.append("G")
G.ne.append("D"), G.ne.append("E"), G.ne.append("F")
F.ne.append("G")
A.iv,B.iv,C.iv,D.iv,E.iv,F.iv = B,C,D,E,F,G #vertex를 찾기쉽게 A다음 B vertex 이런식으로 둔다.
visited = [] #방문했던 vertex를 담아둘 list
stack = [] #다음 방문할 vertex를 참고하기 위한 list 

def graph_print(): # readline으로 확인한 graph 들의 vertex와 이웃한 vertex를 확인하는 함수
    current = A
    while current != None:
        print(current.data,": {",end = "")
        n = len(current.ne)
        for i in range(0,n):
            print("(",current.data,",",current.ne[i],")",end="")
        print("}")
        current = current.iv

def print_graph(): #BFS,DFS를 돌리고 graph.nei 에 입력된 vertex와 이웃한 vertex를 확인하는 함수 
    current = A
    while current != None:
        print(current.data,": {",end = "")
        n = len(current.nei)
        for i in range(0,n):
            print("(",current.data,",",current.nei[i],")",end="")
        print("}")
        current = current.iv

def graph_edge(): # 생성된 총 edge 개수에 2배가 되는 수를 구하는 함수
    current = A
    var = 0
    while current != None:
        var += len(current.nei)
        current = current.iv
    return var

def graph_visited(vertex): #vertex가 visited 했는지 안했는지 확인하는 함수
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
        
def graph_search(vertexdata): # vertexdata 값을 vertex값으로 바꾸어 주는 함수
    current = A
    while current.iv != None:
        if current.data == vertexdata:
            break
        else:
            current = current.iv
    return current
    

def graph_DFS(vertex):
    if (graph_edge() == 12): # 7개 vertex로 구성된 graph의 DFS이므로 edge는 6개가 나온다.
        return
    else:
        visited.append(vertex.data) # vertex.data를 visited에 추가한다.
        n = len(vertex.ne)
        for i in range(0,n): #vertex의 이웃한 vertex를 각각 확인해본다.
            if graph_visited(graph_search(vertex.ne[i])) == False: #vertex의 이웃한 vertex가 방문하지 않았다면
                stack.append(vertex.data) #vertex.data 를 stack에 추가
                vertex.nei.append(vertex.ne[i])                       #vertex와 vertex.ne[i] 를 nei에서 연결시켜준다
                graph_search(vertex.ne[i]).nei.append(vertex.data)    #vertex.ne[i]와 vertex 를 nei에서 연결시켜준다
                vertex = graph_search(vertex.ne[i]) #vertex를 vertex.ne[i]로 둔다.
                graph_DFS(vertex)  #graph_DFS(vertex) 를 실행한다.
                break #for 구문 탈출
            elif (i == n-1) and (graph_visited(graph_search(vertex.ne[i])) == True) == 1:#vertex의 이웃한 vertex가 이미 방분했다면
                m = len(stack) #stack 의 길이를 m 이라고한다.
                vertex = graph_search(stack[m-1]) #vertex를 stack의 맨 끝값이라고 한다.
                stack.pop() #stack의 맨끝값을 뺀다.
                graph_DFS(vertex) #graph_DFS(vertex) 를 실행한다.
                
                
def graph_BFS(vertex):
    visited.append(vertex.data) #vertex.data를 visited에 추가한다.
    n = len(vertex.ne) 
    for i in range(0,n): # vertex의 이웃한 vertex를 각각 확인한다.
        if graph_visited(graph_search(vertex.ne[i])) == False: #vertex의 이웃한 vertex가 방문하지 않았다면
            vertex.nei.append(vertex.ne[i])                     #vertex와 vertex.ne[i] 를 nei에서 연결시켜준다
            graph_search(vertex.ne[i]).nei.append(vertex.data)  #vertex.ne[i]와 vertex 를 nei에서 연결시켜준다
            stack.append(vertex.ne[i])  #vertex의 이웃한 vertex를 stack에 추가한다.
            visited.append(vertex.ne[i]) #vertex의 이웃한 vertex를 visited에 추가한다.
            
    if len(stack)>=1:    #stack 이 1이상일떄
        save = stack[0] #save 를 stack[0]이라고 한다.
        del stack[0] #stack[0]을 제거한다.
        graph_BFS(graph_search(save)) #graph_BFS(save) 를 실행한다.


