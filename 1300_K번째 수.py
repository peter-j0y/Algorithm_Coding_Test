import sys
from collections import deque
from bisect import bisect_left, bisect_right
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
queue = deque()
for i in range(1,N+1):
    queue.append(i)

print(queue)