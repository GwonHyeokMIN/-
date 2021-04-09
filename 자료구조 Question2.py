class Node():
    def __init__(self):
        self.data=None
        self.next=None
        self.prev=None

def insertNode(): 
    global head,end                    
    vari=input("1.head insert, 2.middle insert, 3.end insert")
    if (vari!="1")and(vari!="2")and(vari!="3")==1:
        print("1~3만 입력 하십시오.")
        return
    insertData=input("추가하실 노드의 데이터를 입력해주십시오:")
    newnode=Node()                                                   
    newnode.data=insertData
    if vari=="1":
        if(head==None)and(end==None)==1:
            head=newnode
            end=newnode
        else:      
            newnode.next=head              
            head.prev=newnode              
            head=newnode                  
    elif vari=="2":
        if(head==None)and(end==None)==1:
            head=newnode
            end=newnode
        elif(head==end):
            print("1개의 노드 밖에없어 중간에 입력 하실 수 없습니다.")           
        else:
            prevData=input("추가하실 노드의 prev 노드를 입력 해주십시오:")
            current1=head                                                    
            while current1.data!=prevData:                                  
                current1=current1.next
            current2=current1.next                                           
            newnode.next=current2                                           
            current2.prev=newnode
            newnode.prev=current1                                            
            current1.next=newnode                                                                                                                     
    elif vari=="3":
        if(head==None)and(end==None)==1:
            head=newnode
            end=newnode
        else:      
            newnode.prev=end             
            end.next=newnode             
            end=newnode

def deleteNode():
    global head,end                                                 
    deleteData=input("제거하실 노드의 데이터를 입력해주십시오:")
    if (head==None)and(end==None)==1:
        print("비어있습니다.")
    elif head==end:
        del(head)
        del(end)
        head=None
        end=None
    elif head.next==end:
        if head.data==deleteData:
            head.next=None
            end.prev=None
            del(head)
            head=end
        elif end.data==deleteData:
            head.next=None
            end.prev=None
            del(end)
            end=head
    elif head.data==deleteData:     
        current=head.next         
        current.prev=None         
        head.next=None            
        del(head)                 
        head=current                                              
    elif end.data==deleteData:      
        current=end.prev          
        end.prev=None
        current.next=None
        del(end)
        end=current
    elif ((head.data != deleteData)and(end.data != deleteData)):
        current=head
        while current.data!=deleteData:
            current=current.next
        current1=current.prev
        current2=current.next
        current1.next=current2
        current2.prev=current1
        del(current)
    else:
        print("찾으시는 데이터가 존재하지않습니다.")


def searchNode():
    global head
    searchData=input("찾고싶은 노드의 데이터를 입력하시오:")
    current=head
    if (head==None)and(end==None)==1:
        print("no")
    elif head==end:
        if current.data==searchData:
            print("yes")
        elif current.data!=searchData:
            print("no")
    else:
        while current.data != end:
            current=current.next
            if current.data==searchData:
                break
        if current.data==searchData:
            print("yes")
        elif current.data!=searchData:
            print("no")
    
def printNode():
    global head,end
    if (head==None)and(end==None)==1:
        print("empty")
    
    else:
        current = head
        print("Data:[\"",current.data,"\"",end="")
        while current.next !=None:
            current =current.next
            print(", \"",current.data,"\"",end="")
        print("]")

def reverseNode():
    global head,end
    if (head==None)and(end==None)==1:
        printNode()
    elif head==end:
        printNode()
    else:
        vare=end
        varh=head
        end=varh
        head=vare
        vare.next=vare.prev
        vare.prev=None
        varh.prev=varh.next
        while (vare!=varh.next):
            vare=vare.next
            savevar=vare.next
            vare.next=vare.prev
            vare.prev=savevar
        varh.next=None
        printNode()
        
node1=Node()
node1.data="apple"

node2=Node()
node2.data="banana"
node2.prev=node1
node1.next=node2

node3=Node()
node3.data="carrot"
node3.prev=node2
node2.next=node3

node4=Node()
node4.data="graph"
node4.prev=node3
node3.next=node4

head=node1
end=node4

var,vari,vard,count=0,0,0,0
while True:
    var=input("1.Insert, 2.Delete, 3.Search, 4.Print, 5.Inverse, 6.Exit\n")
    if var=="1":
        insertNode()

    elif var=="2":
        deleteNode()

    elif var=="3":
        searchNode()

    elif var=="4":
        printNode()

    elif var=="5":
        reverseNode()

    elif var=="6":
        print("Exit.\n")
        break
    
    else:
        print("1~6의 숫자만 입력 하십시오")
        
