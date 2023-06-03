import time
start = time.time()

n = 100000
cnt = 1

for i in range(n):
    for j in range(n):
        print("연산 횟수" + str(cnt))
        cnt += 1
end = time.time()
print("시간 :", end-start, "sec")
#
# 시간복잡도는 코드의 계산식 갯수, 계산식의 중복에 따라서 나뉨,
# 따라서 ex01은 for문 하나, ex02는  for문 3개라 복잡도 3배
# ex03은 for*for이기때문에 ex01의 제곱만큼 오래걸린다
