def get_magic_triangle(rows):
    pascal_triangle = []
    for row in range(rows):
        current_row = [1]
        if len(pascal_triangle) > 0:
            last_row = pascal_triangle[-1]
            for i in range(len(last_row) - 1):
                num = last_row[i] + last_row[i + 1]
                current_row.append(num)
            current_row.append(1)
        pascal_triangle.append(current_row)

    return pascal_triangle


print(get_magic_triangle(5))
