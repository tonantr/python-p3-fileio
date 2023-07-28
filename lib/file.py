text_file = open('file_name.txt', encoding='utf-8')
text_file.close()


with open('file_name.txt', encoding='utf-8') as text_file:
    text_file.read()


# append mode 
text_file = open('file_directory/file_name.txt', mode='a', encoding='utf-8')

# write mode
text_file = open('file_directory/file_name.txt', mode='w' encoding='utf-8')

# reading from a file
text_file = open('text_file.txt', encoding='utf-8')
print(text_file.read())

# we can process one line at a time instead of using the read() method which gives us the entire file content.
with open('big_file.txt', encoding='utf-8') as text_file:
    for line in text_file:
        # Process the individual line
        print(line)


#Writing to a file
with open('log_file.txt', mode='w', encoding='utf-8') as log_file:
    log_file.write('Log 1')

with open('log_file.txt', mode='a', encoding='utf-8') as log_file:
    log_file.write('Log 2')