if __name__ == '__main__':
    N = int(input())
    commands = []
    [commands.append(input().strip().lower().split()) for _ in range(N)]
    my_list = []
    for c in commands:
        if c[0]=='insert':
            my_list.insert(int(c[1]), str(c[2]))
        elif c[0]=='print':
            print(list(map(int, my_list)))
        elif c[0]=='reverse':
            my_list.reverse()
        elif c[0]=='pop':
            my_list.pop()
        elif c[0]=='sort':
            my_list.sort(key=int)
        elif c[0]=='append':
            my_list.append(str(c[1]))
        elif c[0]=='remove':
            my_list.remove(str(c[1]))
        else:
            raise ValueError('Unknown command: {}'.format(c[0]))