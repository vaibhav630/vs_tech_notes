
#1. Create a list of 5 integers and print it.
my_list = [1,2,3,4,5]
print(my_list)

#2. Given a list `numbers = [10, 20, 30, 40, 50]`, print the first & last element
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])

# 3. Create an empty list and add 5 numbers using `append()`.
my_list2 = []
for i in range(1,6):
    my_list2.append(i)
print(my_list2)

mylist2 = [i for i in range(1,6)]
print(mylist2)


# 4. Insert the number `25` at index `2` in the list `[10, 20, 30, 40]`.
numbers2 = [10, 20, 30, 40]
numbers2[2] = 25
print(numbers2)

# 5. Remove `30` from `[10, 20, 30, 40, 50]`.
numbers3 = [10, 20, 30, 40, 50]
numbers3.pop(2)
print(numbers3)

# 6. Write a program to find the length of a list '[10, 20, 30, 40, 50]' without using `len()`.
count=0
for number in numbers3:
    count+=1
print(count)

# 7. Find the sum of elements in '[10, 20, 30, 40, 50]`.
sum=0
for number in numbers3:
    sum+=number
print(sum)

#8. Write a program to find the maximum number in a list '[2,5,9,7,6,8]' without using `max()`
numbers4 = [2,5,9,7,6,8]
maximum = 0
for number in numbers4:
    if number>maximum:
        maximum=number
print(maximum)

max(numbers4)

#9. Count how many times `5` appears in `[5, 2, 5, 3, 5, 4]`.
numbers5 = [5, 2, 5, 3, 5, 4]
count_5 = 0
for number in numbers5:
    if number == 5:
        count_5+=1
print(count_5)

print(numbers5.count(5))

#10. Reverse `[1,2,3,4,5]` without using `reverse()`.
numbers6 = [1,2,3,4,5]
print(numbers6[::-1])

#11. Remove duplicates from `[1,2,2,3,4,4,5]`.
numbers7 = [1,2,2,3,4,4,5]
#print(numbers7.index(2))
unique = []
for number in numbers7:
    if number in unique:
        continue
    else:
        unique.append(number)
print(unique)

print(set(numbers7))

#12. From `[10,15,20,25,30,35]`, create a new list containing only even numbers.
numbers8 = [10,15,20,25,30,35]
even = []
for number in numbers8:
    if number % 2 == 0:
        even.append(number)
print(even)

#13. Find the second-largest number in a list.
numbers9 = [2,5,9,7,6,8]
numbers9.sort()
print(numbers9[-2])

#14. Rotate `[1,2,3,4,5]` to the left by 1 position.
# Example result:
# Input:  [1,2,3,4,5]
# Output: [2,3,4,5,1]
