# Defining The List
k = [3,1,2,55,34,24,67,12,78]

n=len(k)
# Performing Insertion Sort 

for i in range(1,n):
    temp = k[i]
    j=i-1
    for z in range(j,-1,-1):

        if k[i] < k[z]:
            k[i] = k[z]
            k[z]=temp
    print("Step ",i,":-",k)    


