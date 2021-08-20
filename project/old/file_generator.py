#!/usr/bin/env python3
"""
1. Prompts user to provide a title (will convert to standard filename)
2. finds and replaces spaces with underscores
3. places "lab{number}" at the beginning
4. places ".py" at the end
5. then moves on to take a body of info
6. pushs info inside of generated file name
7. creates new file
8. sends file to specified directory path
"""
import os

# move into the working directory
#my_path = "/Users/danielwilmer/python_projects/example_code"
my_path = "/home/student/python_projects/example_code"
os.chdir(my_path)

# fixing the file name (replace spaces w/ "_", add lab + number)


# generating a standard file name from a title provided by the user
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
while True:
    cond = input("Continue? Y/n: ")
    if cond == "n":
        break
    title = input("\nProvide TITLE: ").lower()
    underscores = title.replace(" ","_")
    py = underscores +".py"
    # create a text file for writing
    print("\nFilename generated:\n", py)
 
    #os.path.join()
    new_path = my_path + "/" + py
    contents = []
    # getting the body of information
    print("\nProvide CODE: ")
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    with open(new_path, 'w') as fp:
        fp.write("\n".join(contents))

