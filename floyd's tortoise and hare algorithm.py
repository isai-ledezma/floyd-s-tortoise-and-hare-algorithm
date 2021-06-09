n = 0
numbers = []
end_loop = False
while not end_loop:
    n += 1
    numbers.append(input(f'posicion {n}, give me the number:'))
    if input('do you want continue?') in ['n', 'N']:
        end_loop = True

print('this are the numbers:')
n = 0
for number in numbers:
    print(f'{number}', end=' ')

#finding the first duplicated number
posision = 1
hare_posision = 0
tortoise_posision = 0
while posision <= ((len(numbers) * 2 + (len(numbers)/2) )):
    posision += 1
    tortoise_posision = (tortoise_posision + 1 ) % len(numbers)
    hare_posision = (hare_posision + 2 ) % len(numbers)
    if numbers[tortoise_posision] == numbers[hare_posision]:
        break
print(f'the first duplicated number is {numbers[tortoise_posision]}')
