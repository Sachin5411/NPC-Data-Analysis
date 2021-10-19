# print("Hello world",end="$")
# print("This is my second line")

# print("HI" , "I m","sachin")

# my_var = 5
# a=5
# b=6
# print(a+b)

#data type
# # int , float , string , bool
# a=5.5
# a="Any string"
# a=5
# a=True
# print(type(a))

# rain = True

# if rain==True:
#     print("take your umbrella with you")
# elif rain==False:
#     print("nothing")
# else:
#     print("go out and have fun")

#loops

# for i in range(1,16,2):
#     print(i)

# a=0
# while a<3:
#     print(a)
#     a+=1

# my_list = [1,2,5,"string",4.5]

# print(my_list)

# for i in my_list:
#     print(i)

#Dictionary

# a= {"sachin":99,"ergjfsv":766}

# print(a.values())

# a=(1,23,5)
# a=[1,2,3,2,4,5]
# print(set(a))

#funtion

# def sum(a,b):
#     return a+b 
    
# print(sum(4,5))

# create to print the sum of a list

# a=[1,2,3,4]

# s=0
# for i in a:
#     s+=i

# print(s)

#Dice dataset 

dice_roll = [1,5,6,3,4,5,2,1,6,2,3,4]

# mean = sum of all observation / total no of observation
def sum_list(dice):
    s=0
    for i in dice:
        s+=i
    return s
    

def cmean(dice_roll):
    return  sum_list(dice_roll)/ len(dice_roll)
    
print(cmean(dice_roll))

import statistics

print(statistics.mean(dice_roll))

print(statistics.median(dice_roll))

a=["male","female", "male", "male","female"]

print(statistics.mode(dice_roll))














