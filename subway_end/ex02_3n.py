import time
start = time.time()

n = 100000
cnt = 1

for i in range(n):
    print("연산횟수"+str(cnt))
    cnt += 1

for i in range(n):
    print("연산횟수"+str(cnt))
    cnt += 1

for i in range(n):
    print("연산횟수"+str(cnt))
    cnt += 1


end = time.time()
print("시간 :", end-start, "sec")
#31.5sec
