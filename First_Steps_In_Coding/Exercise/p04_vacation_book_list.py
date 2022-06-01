total_pages = int(input())
pages_for_one_hour = int(input())
number_of_days = int(input())
total_time_for_read = total_pages/pages_for_one_hour
hours_for_day = total_time_for_read/number_of_days
x = int(hours_for_day)
print(x)