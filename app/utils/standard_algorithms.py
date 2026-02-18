

class StandardAlgorithms:
    def insertion_sort(array: list, attr: str) -> list:
        for i in range(1, len(array)):
            current = array[i]
            current_value = getattr(current, attr)
            while i > 0 and current_value < getattr(array[i-1], attr):
                array[i] = array[i-1]
                i-=1
            array[i] = current
        return array


    def binary_search(array: list, attr: str, target) -> int:
        low = 0
        high = len(array)-1

        while low <= high:
            mid = (low + high)//2

            if getattr(array[mid], attr) == target:
                return mid
            elif getattr(array[mid], attr) > target:
                high = mid-1
            else:
                low = mid+1

        return -1
    
    def find_max(array: list, attr: str):
        max_value = 0
        for item in array:
            value = getattr(item, attr)
            if value > max_value:
                max_value = value
        return max_value
