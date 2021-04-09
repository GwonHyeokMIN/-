def isStackFull():
    global SIZE,array,toparray
    if(toparray>=SIZE-1):       
        return True
    else:
        return False

def isStackEmpty():
    global SIZE,array,toparray
    if(toparray==-1):            #top=-1이면 stack은 비어있는상태#
        return True
    else:
        return False
    
def push(data):
    global SIZE,array,toparray
    if(isStackFull()):
        print(array)
        print("스택이 꽉 찼습니다.")
        return
    toparray +=1
    array[toparray]=data
    print(array)

def pop():
    global SIZE,array,toparray
    if(isStackEmpty()):
        print(array)
        print("스택이 비었습니다.")
        return None
    data=array[toparray]
    array[toparray]=None
    toparray-=1
    print(array)
    return data

def stackarray():
    global SIZE,array,toparray
    while True:
        vara=input("스택의 데이터를 적어주십시오")
        if (vara=="[")or(vara=="{")or(vara=="(")or(vara=="<")==True:
            push(vara)
        elif (vara=="]")or(vara=="}")or(vara==")")or(vara==">")==True:
            if (vara=="]")and(array[toparray]=="[")==True:
                pop()
                print("Ture")
                if toparray == -1:
                    break
            elif (vara=="}")and(array[toparray]=="{")==True:
                pop()
                print("Ture")
                if toparray == -1:
                    break
            elif (vara==")")and(array[toparray]=="(")==True:
                pop()
                print("Ture")
                if toparray == -1:
                    break
            elif (vara==">")and(array[toparray]=="<")==True:
                pop()
                print("Ture")
                if toparray == -1:
                    break
            else:
                print("False")
                break
        else:
            print("[,{,(,<,>,),},] 만 입력해주십시오")

SIZE=10     #Queuearray,Queuecircular랑 같이 사용#
array=[None,None,None,None,None,None,None,None,None,None]  #Queuearray, Queuecircular랑 같이 사용#
toparray=-1
#=============================================================================================#
class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printlist(top):
    current1 = top
    print("Data:",current1.data,end="")
    while current1.link !=None:
        current1 =current1.link
        print(", ",current1.data,end="")
    print("\n")
def deletelist(current,top):

    current1=current.link
    top.link=current1
    del(current)
    current=current1
    top.data-=1
    
def stacklist():
    top=Node()
    top.data=0
    head=top
    current=top
    end=top
    
    while True:
        expr=input("[,{,(,<,>,),},]을 입력 하십시오:")
        if ((expr=="[")or(expr=="{"))or((expr=="(")or(expr=="<")):
            newnode=Node()
            newnode.data=expr
            if current == top:
                top.link = newnode
                current=newnode
                end=newnode
                top.data+=1
                printlist(top)
            elif current != top:
                newnode.link = current
                top.link = newnode
                current = newnode
                top.data+=1
                printlist(top)

        elif ((expr=="]")or(expr=="}"))or((expr==")")or(expr==">")):
            if current == top:
                top.data-=1
                printlist(top)
                print("False")
                break
            elif ((expr=="]")and(top.link.data=="[")):
                deletelist(top.link,top)
                printlist(top)
                print("True")
                if top.data==0:
                    break

            elif ((expr=="}")and(top.link.data=="{")):
                deletelist(top.link,top)
                printlist(top)
                print("True")
                if top.data==0:
                    break
            elif ((expr==")")and(top.link.data=="(")):
                deletelist(top.link,top)
                printlist(top)
                print("True")
                if top.data==0:
                    break
            elif ((expr==">")and(top.link.data=="<")):
                deletelist(top.link,top)
                printlist(top)
                print("Ture")
                if top.data==0:
                    break
            else:
                printlist(top)
                print("False")
                break

#=============================================================================================#         
def isQueueFull():
    global SIZE,array,reararray
    if(reararray==SIZE-1):
        return True
    else:
        return False

def isQueueEmpty():
    global SIZE,array,reararray
    if(reararray==-1):
        return True
    else:
        return False

def enQueue(data):
    global SIZE,array,reararray
    if(isQueueFull()):
        print(array)
        print("예약이 꽉 찼습니다.")
        return
    reararray+=1
    array[reararray]=data
    print(array)

def deQueue():
    global SIZE,array,reararray
    if(isQueueEmpty()):
        print(array)
        print("예약이 없습니다.")
        return None
    for i in range(0,reararray):
        array[i]=array[i+1]
    array[reararray]=None
    reararray -=1
    print(array)
    return 0

def Queuearray():
    global SIZE,array,reararray
    while True:
        vara=(input("1.손님 예약, 2.예약 손님  입장"))
        if vara=="1":
            name=input("예약하시는 손님의 이름을 적어주십시오")
            enQueue(name)
        elif vara=="2":
            deQueue()
        else:
            print("1~2의 숫자만 입력 하십시오.")
        
reararray=-1
#=============================================================================================#
def isQueueFullcircular():
    global SIZE,array,front,rear
    if(rear==front)and(array[front]!=None)==1:
        return True
    else:
        return False
   
def isQueueEmptycircular():
    global SIZE,array,front,rear
    if(rear==front)and(array[rear]==None)==1:
        return True
    else:
        return False

def enQueuecircular(data):
    global SIZE,array,front,rear
    if(isQueueFullcircular()):
        print(array)
        print("예약이 꽉 찼습니다.")
        return
    if rear==9:
        rear=0
    else:
        rear+=1
    array[rear]=data
    print(array)

def deQueuecircular():
    global SIZE,array,front,rear
    if(isQueueEmptycircular()):
        print(array)
        print("예약이 없습니다.")
        return None
    if front==9:
        front=0
    else:
        front+=1
    data=array[front]
    array[front]=None
    print(array)
    return data

def Queuecircular():
    global SIZE,array,front,rear
    while True:
        vara=input("1.손님 예약, 2.예약 손님  입장")
        if vara=="1":
            name=input("예약하시는 손님의 이름을 적어주십시오")
            enQueuecircular(name)
        elif vara=="2":
            deQueuecircular()
        else:
            print("1~2의 숫자만 입력 하십시오.")

rear=9
front=9
#=============================================================================================#
def isQueueEmptylist():
    global frontlist,rearlist
    if (frontlist.data==None)and(rearlist.data==None)==1:
        return True
    else:
        return False

def printQueuelist():
    global frontlist,rearlist,savelist
    print("[ ",end="")
    savelist=frontlist
    if (isQueueEmptylist()!=True):
        while (frontlist!=rearlist):
            print(frontlist.data,",",end="")
            frontlist=frontlist.link
    frontlist=savelist
    if rearlist.data!=None:
        print(rearlist.data,"]")
    elif rearlist.data==None:
        print("]")
    
        
def enQueuelist(data):
    
    global frontlist,rearlist
    newnode=Node()
    newnode.data=data
    if (rearlist.data!=None)and(frontlist.data!=None)==1:
        rearlist.link=newnode
        newnode.link=frontlist
        rearlist=newnode
        printQueuelist()
    else:
        rearlist=newnode
        frontlist=newnode
        printQueuelist()

def deQueuelist():
    global frontlist,rearlist
    if(isQueueEmptylist()):
        printQueuelist()
        print("예약이 없습니다")
    elif(rearlist.data!=None)and(frontlist.data!=None)==1:
        if(rearlist!=frontlist):
            rearlist.link=frontlist.link
            frontlist.link=None
            del(frontlist)
            frontlist=rearlist.link
            printQueuelist()
        else:
            rearlist.link=None
            rearlist.data=None
            frontlist.link=None
            frontlist.data=None
            printQueuelist()
    
    
def Queuelist():
    global frontlist,rearlist
    while True:
        varl=(input("1.손님 예약, 2.예약손님 입장"))
        if varl=="1":
            name=input("예약하시는 손님의 이름을 적어주십시오")
            enQueuelist(name)
        elif varl=="2":
            deQueuelist()
        else:
            print("1~2의 숫자만 입력 하십시오.")

rearlist=Node()
frontlist=Node()
savelist=Node()
#=============================================================================================#

while True:
    var=(input("1.Stack with array,2.Stack with linked list 3.Queue with array, 4.Queue with circular array 5.Queue with linked list 6.Exit"))

    if var=="1":
        stackarray()

    elif var=="2":
        stacklist()

    elif var=="3":
        Queuearray()

    elif var=="4":
        Queuecircular()

    elif var=="5":
        Queuelist()
        
    elif var=="6":
        break
    else:
        print("1~6까지 숫자만 입력 하십시오")
