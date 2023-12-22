import random

total_simulations = 1000000
halfway_success_rate = 70

has_reached_75 = False

for _ in range(total_simulations):

  successful = 35
  shots = 50

  for _ in range(50):
    if random.random() < 0.8:
        successful += 1
    shots += 1

  success_rate = successful * 100 / shots

  if success_rate == 75:
      has_reached_75 = True
      break

if has_reached_75:
    print("Yes")
else:
    print("No")
