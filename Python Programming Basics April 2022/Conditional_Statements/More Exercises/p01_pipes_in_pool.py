volume_pool = int(input())
debit_first_pipe = int(input())
debit_second_pipe = int(input())
hours_without_worker = float(input())

volume_first_pipe = debit_first_pipe * hours_without_worker
volume_second_pipe = debit_second_pipe * hours_without_worker
total_full_littre = volume_first_pipe + volume_second_pipe

total_in_percentage = total_full_littre / volume_pool

if total_full_littre <= volume_pool:
    print(f"The pool is {total_in_percentage * 100:.2f}% full. Pipe 1: {volume_first_pipe / total_full_littre * 100:.2f}%. "
          f"Pipe 2: {volume_second_pipe / total_full_littre * 100:.2f}%.")
else:
    print(f"For {hours_without_worker:.2f} hours the pool overflows with {total_full_littre - volume_pool:.2f} liters.")