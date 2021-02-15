gun = 10

def checkpoint(soldiers):
    gun = 20
    gun = gun - soldiers
    print("[in function] Guns left: {0}".format(gun))

print("Total Guns: {0}".format(gun))
checkpoint(2)
print("Guns left: {0}".format(gun))