#  Day 24 practice - break & loop control

# 1. print till 7, then stop
num = int(input("enter number:"))
for i in range(1,num+1):
    if i == 7:
        break
    print(i)

# 2. find 7 in list 
nums = [3,8,2,7,5]
for i in nums:
    if i == 7:
        print("found")
        break

# 3. first even number
num = int(input("enter number:"))
for i in range(1,num+1):
    if i % 2 == 0:
        print(i)
        break

# 4. input loop stop at 0
while True:
    num = int(input("enter number:"))
    if num == 0:
        print("stopped")
        break 
    print(num)

# 5. print till 5 using break 
i = 1 
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# 6. chek even number in list
data = [1,3,5,7]
found = False
for i in data:
    if i % 2 == 0:
        print("even found")
        found = True
        break
if not found:
    print("no even")
