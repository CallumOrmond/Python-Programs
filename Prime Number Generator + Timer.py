import time 

def prime_and_time():
    current = 1
    yield (1, 0)

    while True:
        current = current + 1

        prime = True
        start_time = time.time()
        for i in range(2, current):
            if current % i == 0:
                prime = False
                

        if prime == True:
            end_time = time.time()
            yield (current, round(end_time - start_time, 8))
            
P = prime_and_time()

for i in range(100):
    print(next(P))