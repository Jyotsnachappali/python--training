''''def movezeros(nums):
    x=[]
    y=[]
    for i in range (len(nums)):
        if nums[i]==0:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=y+x
    print(z)
nums=[0,1,0,3,12]
movezeros(nums)
                '''

print('start')
try:
    x = int(input())
    y = int(input())
    print(x/y)
except Exception as e:
    print(e)
