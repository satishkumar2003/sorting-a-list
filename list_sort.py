if __name__ == '__main__':
    arr = []
    n = int(input("Enter the number of elements in the list: "))
    for _ in range(n):
        element = int(input("Enter number: "))
        arr +=[element,]
    type = input("Ascending or descending? (a/d): ")
    for i in range(n):
        for j in range(0, n-i-1):
            a,b=j,j+1
            if type=='d':
                a,b=b,a
            if arr[a] > arr[b] :
                arr[a], arr[b] = arr[b], arr[a]
    print("Sorted list = ",arr)