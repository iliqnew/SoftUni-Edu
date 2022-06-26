exp_needed = float(input())
battles = int(input())

for i in range(1, battles+1):
    exp_got = float(input())
    if i % 3 == 0:
        exp_got += exp_got * 0.15
    elif i % 5 == 0:
        exp_got -= exp_got * 0.1
    if i % 15 == 0:
        exp_got += exp_got * 0.05
    exp_needed -= exp_got
    if exp_needed <= 0:
        print(f"Player successfully collected his needed experience for {i} battles.")
        break
if exp_needed > 0:
    print(f"Player was not able to collect the needed experience, {exp_needed:.2f} more needed.")

