arr = [str(i) for i in range(0, 10)]


# arr.extend([-1 for _ in range(50001)])




# def diminished(N):
#     N = str(N)
#     for i in range(0, len(N)-1):
#         if N[i] <= N[i+1]:
#             return False
#     return True
#
#
# def order(N):
#         num = 0
#         idx = -1
#         while True:
#             if diminished(num):
#                 idx += 1
#                 if idx == N:
#                     return num
#             num += 1
#
# N = int(input())
# print(order(N))
