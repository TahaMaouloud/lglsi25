def triangle(n):
    return '\n'.join('*' * (i + 1) for i in range(n))

if __name__ == "__main__":
    print(triangle(int(input())))
