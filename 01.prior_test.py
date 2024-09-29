input = "apple cherry kiwi melon banana";
target = 'cherry';

fruits = input.split();

for i in range(len(fruits)):
    if fruits[i] != target:
        continue;
    else:
        print(f'{fruits[i]} : 발견!');
        print(f'{fruits[i]}의 index는 {i}');
  
for fruit in fruits:
  if fruit != target:
    continue;
  else:
    print(f'{fruit} : 발견!');
    print(f'{fruit}의 index는 {fruits.index(fruit)}')
    break;

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5

# print(len(matrix));

found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f'position: {i} {j}, element: {matrix[i][j]}')
        if matrix[i][j] == target:
            found = True
            break
    if found == True:
        break

print(f'target이 matrix안에 있나요? {found}');
