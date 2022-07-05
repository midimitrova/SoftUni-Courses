from math import ceil

number_easter_bread = int(input())

total_used_sugar = 0
total_used_flour = 0
package_sugar = 0
package_flour = 0
max_used_sugar = 0
max_used_flour = 0


for materials in range(1, number_easter_bread + 1):
    used_sugar = int(input())
    used_flour = int(input())

    total_used_sugar += used_sugar
    total_used_flour += used_flour

    if used_sugar > max_used_sugar:
        max_used_sugar = used_sugar
    if used_flour > max_used_flour:
        max_used_flour = used_flour

package_sugar = ceil(total_used_sugar / 950)
package_flour = ceil(total_used_flour / 750)

print(f"Sugar: {package_sugar}")
print(f"Flour: {package_flour}")
print(f"Max used flour is {max_used_flour} " \
            f"grams, max used sugar is {max_used_sugar} grams.")







