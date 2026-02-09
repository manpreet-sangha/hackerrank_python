import random

n = int(input())
s = set(map(int, input().split()))
N = int(input())

def execute_command(s, command):
    
    if command.strip() == "pop":
        s.pop()
        #print("pop")
        return s
    else:
        op, num = command.strip().split()[0], int(command.split()[1])
    
    if op == "discard":
        s.discard(num)
        return s
        #print("discard " + str(num))
    elif op == "remove":
        try:
            s.remove(num)
            #print("remove "+ str(num))
            return s
        except KeyError:
            #print("remove (keyerror) "+ str(num))
            return s

for i in range(N):
    command = str(input().strip())
    s = execute_command(s, command)

print(sum(s))