from collections import deque

peaks = [80, 90, 100, 60, 70]
peaks_names = {80: 'Vihren', 90: 'Kutelo', 100: 'Banski Suhodol', 60: 'Polezhan', 70: 'Kamenitza'}

quantities_of_the_daily_portions_stack = [int(x) for x in input().split(', ')]
quantities_of_the_daily_stamina_deque = deque([int(x) for x in input().split(', ')])

mountain_peaks = 5
conquered_peaks = deque()

idx_peak = 0
while mountain_peaks > 0 and quantities_of_the_daily_stamina_deque and quantities_of_the_daily_portions_stack:
    current_portion = quantities_of_the_daily_portions_stack.pop()
    current_stamina = quantities_of_the_daily_stamina_deque.popleft()

    if current_portion + current_stamina >= peaks[idx_peak]:
        conquered_peaks.append(peaks_names[peaks[idx_peak]])
        idx_peak += 1
        mountain_peaks -= 1

if mountain_peaks == 0:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print('Conquered peaks:')
    while conquered_peaks:
        print(conquered_peaks.popleft())
