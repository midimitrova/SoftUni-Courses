lenght = int(input())
width = int(input())
high = int(input())
percentage = float(input())

volume_in_centimetres = lenght * width * high
volume_in_littres = volume_in_centimetres * 0.001
busy_area = percentage
free_area = volume_in_littres - (volume_in_littres * percentage/100)

print(free_area)
