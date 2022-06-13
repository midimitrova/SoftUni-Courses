free_days = int(input())

playing_minutes_for_year = 30000
playing_minutes_work_day = 63
playing_minutes_free_day = 127
all_days_for_year = 365
work_days = all_days_for_year - free_days
time_playing = work_days * playing_minutes_work_day + free_days * playing_minutes_free_day




if  playing_minutes_for_year > time_playing:
    diffrence = playing_minutes_for_year - time_playing
    hours = diffrence // 60
    minutes = diffrence % 60
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    diffrence = time_playing - playing_minutes_for_year
    hours = diffrence // 60
    minutes = diffrence % 60
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")




