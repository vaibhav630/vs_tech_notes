# 1. Create a list of 5 integers and print it

```python
my_list = [1,2,3,4,5]
print(my_list)
````

Output

```
[1, 2, 3, 4, 5]
```

---

# 2. Print the first and last element

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
```

Output

```
10
50
```

---

# 3. Create an empty list and add 5 numbers using `append()`

### Using loop

```python
my_list2 = []
for i in range(1,6):
    my_list2.append(i)

print(my_list2)
```

Output

```
[1, 2, 3, 4, 5]
```

### Using List Comprehension (Better Pythonic way)

```python
mylist2 = [i for i in range(1,6)]
print(mylist2)
```

Output

```
[1, 2, 3, 4, 5]
```

---

# 4. Insert `25` at index `2`

Your current code **replaces** the element instead of inserting.

```python
numbers2 = [10, 20, 30, 40]

numbers2[2] = 25
print(numbers2)
```

Output

```
[10, 20, 25, 40]
```

Correct insertion would be:

```python
numbers2.insert(2,25)
```

Result

```
[10, 20, 25, 30, 40]
```

---

# 5. Remove `30` from list

```python
numbers3 = [10, 20, 30, 40, 50]

numbers3.pop(2)
print(numbers3)
```

Output

```
[10, 20, 40, 50]
```

Alternative:

```python
numbers3.remove(30)
```

---

# 6. Find length without using `len()`

```python
count=0

for number in numbers3:
    count+=1

print(count)
```

Output

```
4
```

---

# 7. Find the sum of elements

```python
sum=0

for number in numbers3:
    sum+=number

print(sum)
```

Output

```
120
```

⚠️ Note: Avoid naming variables `sum` because it overrides Python's built-in `sum()` function.

---

# 8. Find maximum without using `max()`

```python
numbers4 = [2,5,9,7,6,8]

maximum = 0

for number in numbers4:
    if number>maximum:
        maximum=number

print(maximum)
```

Output

```
9
```

Built-in method:

```python
max(numbers4)
```

Output

```
9
```

---

# 9. Count how many times `5` appears

```python
numbers5 = [5, 2, 5, 3, 5, 4]

count_5 = 0

for number in numbers5:
    if number == 5:
        count_5+=1

print(count_5)
```

Output

```
3
```

Built-in method:

```python
print(numbers5.count(5))
```

Output

```
3
```

---

# 10. Reverse list without using `reverse()`

```python
numbers6 = [1,2,3,4,5]

print(numbers6[::-1])
```

Output

```
[5, 4, 3, 2, 1]
```

---

# 11. Remove duplicates

```python
numbers7 = [1,2,2,3,4,4,5]

unique = []

for number in numbers7:
    if number in unique:
        continue
    else:
        unique.append(number)

print(unique)
```

Output

```
[1, 2, 3, 4, 5]
```

Alternative using set

```python
print(set(numbers7))
```

Output

```
{1, 2, 3, 4, 5}
```

⚠️ Note: Using `set` does **not preserve order**.

---

# 12. Extract even numbers

### using loop

```python
numbers8 = [10,15,20,25,30,35]

even = []

for number in numbers8:
    if number % 2 == 0:
        even.append(number)

print(even)
```

### Using List Comprehension (Better Pythonic way)

```python
numbers8 = [10,15,20,25,30,35]
mylist2 = [number for number in numbers8 if number% 2 == 0]
print(mylist2)
```

Output

```
[10, 20, 30]
```

---

# 13. Find second largest number

```python
numbers9 = [2,5,9,7,6,8]

numbers9.sort()

print(numbers9[-2])
```

Output

```
8
```

---

# 14. Rotate list left by 1

```python
numbers10 = [1,2,3,4,5]

rotated = numbers10[1:] + numbers10[:1]

print(rotated)
```

Output

```
[2, 3, 4, 5, 1]
```

---

# Key Concepts Practiced

* List creation
* Indexing
* Slicing
* Append
* Insert
* Remove vs Pop
* List comprehension
* Counting elements
* Removing duplicates
* Finding max / second largest
* List rotation

--- 

# Key Learning Points

* Avoid overriding built-in names like max, sum, list.

* Use insert() instead of assignment when inserting elements.

* remove(value) removes by value.

* pop(index) removes by index.

* List slicing is powerful for reversing and rotating lists.

---

