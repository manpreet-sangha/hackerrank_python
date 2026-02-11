from unittest import result


s = "abcdefghijklmnopqrstuvwxyz"
max_width = int(input())

def func(string, max_width):
    chunks = [string[i:i+max_width] for i in range(0, len(string), max_width)]
    return "\n".join(chunks)

result = func(s, max_width)
print(result)