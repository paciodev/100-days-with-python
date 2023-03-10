# with open('test_file.txt') as file:
#     content = file.read()
#     print(content)

# mode='a' = append (add to file)
# mode='w' = write (replace content)
# IMPORTANT! When mode is 'w' and file does not exist, file will be created.
with open('test_file.txt', mode='a') as file:
    file.write(f"\nHello!")