import io

# with open('burgers.txt', 'w') as file:
#     file.write('burger\n')
#     file.write('great burgers\n')
#
# file.close()

##### read whole file

with open('burgers.txt', "r", encoding="utf-8") as file:
    while True:
        line = file.read()
        print(line)
        if not line:
            break
