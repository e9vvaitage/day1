
#Write a function to find the sum of all the numbers from 4212 to 18912512

#num=4212
#num2=18912513
#total=sum(range(num+num2))
#print(total)

num=4212
num2=18912512
total=0
for i in range(num,num2+1):
	total=total+i
print(total)
