def solution(A):
    sum_left, sum_right = 0, sum(A)
    for index, value in enumerate(A):
        sum_right -= value
        if sum_left == sum_right:
            return index
        sum_left += value
    return -1
