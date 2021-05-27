class graph():
    def __init__(self):
        self.data = None
        self.ne = []
        self.iv = None
        
f = open('graph_info.txt', 'r')
line_data = f.readline()
line_save=[]
while line_data:
    line_save.append(line_data)
    print("%s" %line_data, end="")
    print("\n")
    line_data = f.readline()
f.close

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
exist = []
save = []

def print_graph():
    global A,B,C,D,E,F,G,current
    current = A
    while current.iv != None:
        print(current.data,": {",end = "")
        n = len(current.ne)
        for i in range(0,n):
            print("(",current.data,",",current.ne[i],")",end="")
        print("}")
        current = current.iv

def graph_Search():
    global A,B,C,D,E,F,G,current,exist
    n = len(current.ne)
    m = len(exist)
    for i in range(0,n):
        for j in range(0,m):
            if current.ne[i] == exist[j]:
                break
            elif (j == m-1) and (current.ne[i] != exist[j]) ==1:
                return False # exist 에 존재하지 않음
        if (i == n-1) and (j == m-1) and (current.ne[i] == exist[j]) ==1:
            return True # exist 에 전부 존재함

def graph_BFS():
    global A,B,C,D,E,F,G,current,exist,save
    vertex = input(print("BFS를 시작할 지점을 입력하시오: "))
    current = A
    while current.iv != None:
        if current.data == vertex:
            break
        else:
            current = current.iv
    exist.append(current.data)
    save.append(current.data)
    while len(exist) <= 7:
        print(exist)
        if graph_Search() == False:# 이미 지나온 vertex를 제외한 이웃한 vertex로 이동한다.
            n = len(current.ne)
            m = len(exist)
            var = True
            for i in range(0, n):
                for j in range(0, m):
                    if (j == m-1) and (current.ne[i] != exist[j]) ==1:
                        if current.iv != None:
                            if current.data == current.ne[i]:
                                break
                            else:
                                current = current.iv
                        var = False
                        break
                if var == False:
                    break
            exist.append(current.data)
            save.append(current.data)
                    
        elif graph_Search() == True:# 더이상 갈 수있는 edge가 없으면 그전 단계로 돌아간다.
            save.pop()
            n = len(save)
            while current.iv != None:
                if current.data == save[n-1]:
                    break
                else:
                    current = current.iv

graph_BFS()
    
            
        


