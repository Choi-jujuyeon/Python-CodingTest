import sys
n = int(sys.stdin.readline())
arr = sorted(set(sys.stdin.readline().strip() for _ in range(n)), key=lambda x: (len(x), x))
print("\n".join(arr))