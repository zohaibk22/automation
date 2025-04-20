from pathlib import Path
p1 = 'files/text1.txt'


p2 = Path('files/text1.txt')
# print(p2)

# if p2.exists:
#     with open(p1, 'r', ) as file:
#         print(file.read())

p3 = Path('files/zohaib.txt')

if p3.exists():
    with open(p3, 'w') as file:
        file.write("Content 3")
    with open(p3, 'r') as file:
       print(file.read())
 
print(p3.name)
print(p3.stem)
print(p3.suffix )

dir_val = Path('files')

print(dir_val.iterdir())
        

for val in list(dir_val.iterdir()):
    print(type(val))
    

