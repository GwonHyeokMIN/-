import datetime

def Quick_sort(array,s,n): #s는 array의 시작점 n은 array의 끝점
    global L,R,var #재귀 함수를 사용할때 변수가 변경되는것을 방지하기 위해 전역변수 선언을 사용한다.
    L,R,var = s,n,0 #var은 array의 값을 교환할때 사용되는 변수이다.
    if (n+1-s)%2 == 0: #array의 값이 짝수일때 array의 pivot 위치를 선언한다.
        pivot_number = ((n+1-s)//2)+s-1
    else: #array의 개수가 홀수 일때, array의 pivot 위치를 선언한다.
        pivot_number = ((n+1-s)//2)+s
    pivot = array[pivot_number]
    if n <= 1: #array의 개수가 1보다 작으면 멈춘다.
        return array

    else: #array의 개수가 2보다 클때,
        for i in range (s, n+1, 1): #i를 s 부터 n까지 1씩 증가 시킨다.
            if i == R: #i 가 맨 끝값에 도착했을때,
                if array[R] >= array[pivot_number]: #array[i=n=R]이 피봇 값보다 크거나 같다면
                                            #array[R]값이 가장크기 때문에 이값을 빼고 
                    Quick_sort(array,s,R-1) #나머지로 Quick_sort를 돌린다.
                    return array
                else: #array[i=n=R]이 피봇 값 보다 작다면
                    var = array[R]  #피봇 값과 array[R]값을 교환한다.
                    array[R] = array[pivot_number]
                    array[pivot_number] = var #교환된 array[R]값이 가장크기 때문에
                    Quick_sort(array,s,R-1) #이 값을 빼고 나머지로 Quick_sort 한다.
                    return array
            else: #i 가 n에 도착하기 전에
                if array[i] > array[pivot_number]: #array[i]값이 피봇값보다 크다면
                    L = i #그 값을 L로 둔다.
                    break

        for i in range (n, s-1, -1): #i를 n 부터 s까지 1씩 감소 시킨다.
            if i == L: #i 가 L값에 도착했을때,
                var = array[pivot_number] # L과 피봇값을 교환한다.
                array[pivot_number] = array[L]
                array[L] = var  #교환된 값을 기준으로 왼쪽은작고 오른쪽은 크다
                Quick_sort(array,s,L-1)  #왼쪽 부분을 Quick_sort시킨다
                Quick_sort(array,L+1,n)  #오른쪽 부분을 Quick_sort시킨다
                return array

            else: #i가 L값에 도착하기 전에
                if array[i] <= array[pivot_number]: #array[i]값이 피봇값보다 작다면
                    if array[i] <= array[pivot_number]: #array[i]값이 피봇값보다 작다면
                        R = i
                        var = array[R] #R 과 L의 값을 서로 바꿔준다.
                        array[R] = array[L]
                        array[L] = var
                        Quick_sort_swap(array,L+1,R-1,pivot_number) # 피봇값 을 기준으로 좌우가 구분될때 까지 계속한다.
                        if result == 2:
                            Quick_sort(array,s,R-1)
                            return array
                        elif result == 3:
                            var = array[R]
                            array[R] = array[pivot_number]
                            array[pivot_number] = var
                            Quick_sort(array,s,R-1)
                            return array
                        elif result == 4:
                            var = array[pivot_number]
                            array[pivot_number] = array[L]
                            array[L] = var
                            Quick_sort(array,s,L-1)
                            Quick_sort(array,L+1,n)
                            return array
                        else:
                            Quick_sort(array,s,n) # Quick_sort 시킨다.
                            return array

def Quick_sort_swap(array,s,n,pivot_number): # L값과 R값을 바꾸는 함수 이다.
    global result
    L,R,var,result = s,n,0,0
    if n-s+1 <= 1:
        result = 1
        return result
    else:
        for i in range (s,n+1): #i를 s부터 n 까지 1씩 증가시킨다.
            if i == R:
                if array[R] >= array[pivot_number]:
                    result = 2
                    return result
                else:
                    result = 3
                    return result
            else: # L이 끝까지 가지 않은경우
                if array[i] > array[pivot_number]: # L값이 피봇값보다 큰경우
                    L = i #L을 i라고한다.
                    for j in range (n,s-1,-1): # j를 n부터 s까지 1씩 감소시킨다.
                        if j == L:
                            result = 4
                            return result
                        else: #R 이 L까지 가지않은경우
                            if array[j] <= array[pivot_number]: #R값이 피봇보다 작거나 같은경우
                                R = j #R을 j라고한다.
                                var = array[R]
                                array[R] = array[L]
                                array[L] = var #L값과 R값을 바꾼다.
                                Quick_sort_swap(array,L+1,R-1,pivot_number) #L+1부터 R-1까지 Quick_sort_swap 시킨다.
                    
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
                
            
array = [1,2,4,9,7,23,14,12,41,521,231,41,23,15,12,512,312,31,4122,412,31,4,\
         1,2,4,9,7,23,14,12,41,521,231,41,23,15,12,512,312,31,4122,412,31,4,\
         1,2,4,9,7,23,14,12,41,521,231,41,23,15,12,512,312,31,4122,412,31,4,\
         ]
print("array =",array)
print("array의 길이는",len(array),"입니다.")
n = len(array)-1

start_time1 =datetime.datetime.now()  #이 코드가 실행될때의 시간을 측정한다
print("Quick_sort =",Quick_sort(array,0,n))
end_time1 = datetime.datetime.now()   #이 코드가 실행될때의 시간을 측정한다.
elapse_time1 = end_time1 - start_time1 # end 와 start 사이의 시간을 측정한다. 즉 Quick_start의 실행 시간이다.
start_time2 =datetime.datetime.now()
print("Selection_sort =",Selection_sort(array))
end_time2 = datetime.datetime.now()
elapse_time2 = end_time2 - start_time2
print(elapse_time1)   #Quick_sort 의 걸린 시간을 출력한다.
print(elapse_time2)   #Selection_sort 의 걸린 시간을 출력한다.
if Quick_sort(array,0,n) == Selection_sort(array):
    print("일치합니다")
else:
    print("일치하지않습니다.")
if elapse_time1 > elapse_time2:
    print("Selection_sort가 더 빠릅니다.")
else:
    print("Quick_sort가 더 빠릅니다.")
               

