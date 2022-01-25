# https://www.daleseo.com/sort-bubble/
# 거품 정렬을 통해 어떻게 가장 큰 값을 맨 뒤로 보내는지에 대해서 알아보겠습니다.
# 맨 첫번째 값부터 시작해서 다음 값들과 차례로 비교하면서 앞의 값이 더 크면 뒤의 값과 자리를 바꾸면 됩니다.

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]