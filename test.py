def diamond(n:int):
    if n > 0 and n % 2 != 0:
        if n == 1:
            return '*\n'
        x = ' '
        z = []
        count = n // 2
        for i in range(1,n+1,2):
            z.append(x * count + '*' * i + '\n')
            count -= 1
        count = 0
        p = []
        for i in range(n,0,-2):
            p.append(x * count + '*' * i + '\n')
            count += 1

        return ''.join(z + p[1:])


def main():
    print(diamond(5))


if __name__ == '__main__':
    main()