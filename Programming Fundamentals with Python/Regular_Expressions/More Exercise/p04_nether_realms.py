import re

health_pattern = r"[^\d+\.\*\+/-]"
nums_pattern = r"(?P<nums>[+|-]?\d+(\.\d+)?)"
multiply_divide_pattern = r"[\*/]"

demons_info = [demon.strip() for demon in input().split(",")]

for demon in sorted(demons_info):
    nums = []
    health = 0
    damage = 0

    for char in re.findall(health_pattern, demon):
        health += ord(char)
    [nums.append(num[0]) for num in re.findall(nums_pattern, demon)]

    for num in nums:
        damage += float(num)

    for char in re.findall(multiply_divide_pattern, demon):
        if char == "*":
            damage *= 2
        else:
            damage /= 2

    print(f"{demon} - {health} health, {damage:.2f} damage")


