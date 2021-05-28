import datetime
import sys
sys.setrecursionlimit(1000000) #array크기가 10000개를 체크할때 재귀함수가 1000번이 넘어가므로 재귀함수 제한을 1000000으로 늘렸다.


    
def Selection_sort(array):
    n = len(array) #array 의 길이를 확인한다.
    for i in range(0, n-1, 1): # i값을 0부터 n-1 까지 1씩 증가시킨다.
        minldx = i #minldx에 i값을 넣는다.
        for k in range(i+1, n, 1): # k값을 i+1부터 n까지 1씩 증가시킨다.
            if(array[minldx] > array[k]): # array[minldx]가 array[k] 보다 작다면
                minldx = k # minldx를 k값으로 변경한다
        tmp = array[i] # array[i]와 array[minldx]를 변경한다.
        array[i] = array[minldx]
        array[minldx] = tmp

    return array

def Quick_sort(array,s,n): 
    if n-s+1 <= 1: #array의 크기가 1보다 작거나 같으면 array값을 반환한다.
        return array

    else: #array의 크기가 1보다 크다면
        L,R,var = s+1,n,0
        pivot_number = s
        pivot = array[pivot_number]
        while L != R: # L이 R이 아닐때 계속 반복한다.

            while L < n: # L이 n 보다 작을때 계속 반복한다.
                if array[L] > pivot: # array[L]이 pivot보다 작거나 같다면 while (L < n)을 탈출한다.
                    break 
                L+=1 # while 구문을 탈출하기 전까지 L을 1씩 증가시킨다.

            while R > L: # R이 L 보다 클때 계속 반복한다.
                if array[R] < pivot: # array[R]이 pivot 보다 크거나 같다면 while (R > L)을 탈출한다.
                    break
                R-=1 # while 구문을 탈출하기 전까지 R을 1씩 감소시킨다.

            if L < R : # 만약 L이 R보다 작다면
                var = array[L] # array[L]값과 array[R]값을 교환한다.
                array[L] = array[R]
                array[R] = var
                             # L과 R이 같아져서 while (L != R) 탈출 했다.
        if array[L] > pivot: # array[L] 이 피봇보다 작다면
            L -= 1 #L을 1감소 시킨다.
        var = array[L] # array[L]과 피봇을 교환한다.
        array[L] = pivot
        array[pivot_number] = var
        Quick_sort(array,L+1,n) #L을 중심으로 좌우를 다시 Quick_sort 시킨다.
        Quick_sort(array,s,L-1)
        return array
                
            
array = [5,2,4,9,7,3,2,4,5,6,7,\
         ]
print("array =",array)
print("array의 길이는",len(array),"입니다.")
n = len(array)-1

start_time1 =datetime.datetime.now()
print("Selection_sort =",Selection_sort(array))
end_time1 = datetime.datetime.now()
elapse_time1 = end_time1 - start_time1
start_time2 =datetime.datetime.now()  #이 코드가 실행될때의 시간을 측정한다
print("Quick_sort =",Quick_sort(array,0,n))
end_time2 = datetime.datetime.now()   #이 코드가 실행될때의 시간을 측정한다.
elapse_time2 = end_time2 - start_time2 # end 와 start 사이의 시간을 측정한다. 즉 Quick_start의 실행 시간이다.
print(elapse_time1)   #Selection_sort 의 걸린 시간을 출력한다.
print(elapse_time2)   #Quick_sort 의 걸린 시간을 출력한다.
if Quick_sort(array,0,n) == Selection_sort(array):
    print("일치합니다")
else:
    print("일치하지않습니다.")
if elapse_time1 < elapse_time2:
    print("Selection_sort가 더 빠릅니다.")
else:
    print("Quick_sort가 더 빠릅니다.")


