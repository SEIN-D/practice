from random import *
aboard = 0
for people in range(1, 51):
    time = randint(5, 50)
    if time in range(5, 16):
        matching = "O"
        aboard += 1
    else:
        matching = " "
    print("[{0}] {1}번째 손님 (소요시간: {2}분)".format(matching, people, time))
print("\n총 탑승 승객: {0}명".format(aboard))

from random import *
aboard = 0
for people in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간: {1}분)".format(people, time))
        aboard += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(people, time))
print("\n총 탑승 승객: {0}명".format(aboard))
