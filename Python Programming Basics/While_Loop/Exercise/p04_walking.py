
total_steps = 0
reached_goal = False

command = input()
while command != "Going home":
    current_steps = int(command)

    total_steps += current_steps

    if total_steps < 10000:
        reached_goal = False

    elif total_steps > 10000:
        reached_goal = True
        break
    command = input()

if reached_goal:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
elif command == "Going home":
        command = input()
        current_steps = int(command)
        total_steps += current_steps
        if  total_steps > 10000:
            print(f"Goal reached! Good job!")
            print(f"{total_steps - 10000} steps over the goal!")
        else:
            print(f"{10000- total_steps} more steps to reach goal.")
else:
    print(f"{10000- total_steps} more steps to reach goal.")


