import time

start = time.time()
lasttemps = 0
for i in range(30000000000):
    temps = time.time() - start
    if temps - lasttemps >= 1:
        lasttemps = temps
        print(int(temps))
