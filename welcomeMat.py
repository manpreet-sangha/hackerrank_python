# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().strip().split(" "))

pattern = ".|."
welcome = "WELCOME"

for i in range(1, N + 1):
    if i <= N // 2:
        # Top half: increasing pattern
        count = 2 * i - 1
        print((pattern * count).center(M, "-"))
    elif i == N // 2 + 1:
        # Middle: WELCOME
        print(welcome.center(M, "-"))
    else:
        # Bottom half: decreasing pattern (mirror of top)
        count = 2 * (N - i) + 1
        print((pattern * count).center(M, "-"))
        
    
        