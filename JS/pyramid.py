character = "#"
count = 8
rows = []

print("-" * 100)
print("THIS IS THE FIRST LOOP")

for i in range(10):
    # print(f"with python: {i}")
    rows.append(character)
    print(f'[{i}] {rows}')

print("-" * 100)
print("THIS IS THE SECOND LOOP")
result = ""

for i in rows:
    print(i)
    result = result + str(i) + "\n" 

print("-" * 100)
print("THIS IS THE RESULT")
print(result)
print(type(result))
