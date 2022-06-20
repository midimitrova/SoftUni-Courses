hour_exam = int(input())
minutes_exam = int(input())
hour_arrive = int(input())
minutes_arrive = int(input())

late = "Late"
on_time = "On time"
early = "Early"

time_arrive = 0

time_arrival_minutes = hour_arrive * 60 + minutes_arrive
time_exam_minutes = hour_exam * 60 + minutes_exam

if time_arrival_minutes > time_exam_minutes:
    time_arrive = abs(time_arrival_minutes - time_exam_minutes)
    print(late)
    if time_arrive <= 59:
        print(f"{time_arrive} minutes after the start")
    elif time_arrive > 59:
        hour = time_arrive // 60
        minutes = time_arrive % 60
        print(f"{hour}:{minutes:02d} hours after the start")


elif time_arrival_minutes == time_exam_minutes:
    print(on_time)

elif time_arrival_minutes >= time_exam_minutes - 30:
    time_arrive = time_exam_minutes - time_arrival_minutes
    print(on_time)
    print(f"{time_arrive} minutes before the start")


elif time_exam_minutes > time_arrival_minutes:
    time_arrive = time_exam_minutes - time_arrival_minutes
    print(early)
    if time_arrive <= 59:
        print(f"{time_arrive} minutes before the start")
    elif time_arrive > 59:
        hour = time_arrive // 60
        minutes = time_arrive % 60
        print(f"{hour}:{minutes:02d} hours before the start")
