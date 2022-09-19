count_of_triangles_that_contain_origin = 0
triangle_gen = (row for row in open('./p102_triangles.txt'))

def next_triangle():
    tri = [int(x) for x in next(triangle_gen).split(',')]
    return (tri[0:2]), (tri[2:4]), (tri[4:6])

def print_coords():
    a, b, c = next_triangle()
    print(a, b, c)

def triangle_contains_origin(a, b, c):
    return True

def main():
    count = 0
    while True:
        try:
            a, b, c = next_triangle()
            count += 1 if triangle_contains_origin(a, b, c) else 0
        except StopIteration:
            break
    print(count)

if __name__ == '__main__':
    main()