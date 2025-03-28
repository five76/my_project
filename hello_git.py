import os
print('Hello, Git')
print("Indexing it's important")

ind = 0
sum = 0

while ind <= 9:
        sum += ind
        print(sum)
        ind += 1

print(f'\nYour current directory: {os.getcwd()}')

