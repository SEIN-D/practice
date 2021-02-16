def std_weight(height, gender):
    if gender == "male":
        return height * height * 22
    else:
        return height * height * 21
        
height, gender = float(input()), input()
weight = round(std_weight(height/100, gender), 2)
print("Standard weight of {0} cm {1} is {2} kg.".format(height, gender, weight))

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

score = {"Math":0, "English":50, "Coding":100}
for subject, score in score.items():
    # print(subject, score)
    print(subject.ljust(10), str(score).rjust(4), sep=":")

for num in range(1, 21):
    print("Waiting Number: " + str(num).zfill(3))

answer = input("Type any input value: ")
print(type(answer))
print("Input value is {0}.".format(answer))