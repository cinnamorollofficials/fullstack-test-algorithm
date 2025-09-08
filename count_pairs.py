def count_pairs(n, k, arr):
    arr.sort()
    
    count = 0
    left = 0
    right = n - 1
    
    while left < right:
        if arr[left] + arr[right] > k:
            count += (right - left)
            right -= 1
        else:
            left += 1
            
    return count

def main():
    try:
        n, k = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        if len(arr) != n:
            print("Error: The number of elements in the array does not match n.")
            return

        result = count_pairs(n, k, arr)
        
        print(result)

    except (ValueError, IndexError):
        print("Invalid input. Please follow the specified format.")

if __name__ == "__main__":
    main()