"""
Dante Vanderpool
feb 19 2026
Lab 7, working with data in python
"""
 

print("\n ---- Example 2: readline file ----")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readline(30)
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)

print("\n ---- Example 3: readlines file ----")
# readlines makes a list of all the lines in the text file.
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines(30)
    print(filecontent)
    filecontent = file1.readlines(5)
    print(filecontent)

print("\n ---- Example 4: loop through each line in a file ----")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip()) #strip() method removes \n in each line

  
print("\n ---- Example 5: create file ----")    
#w mode creates a file if the file doeant exist. on the other hand, if thr file exists, w mode will overwrite the data in the file.
with open("Vanderpool.txt", "w")as file:
    file.write("Python basics for data science\n")
    file.write("Dante Vanderpool")

print("\n ---- Example 6: append data into an existing file ----")
#append the date and time into 'lastname.txt" file
from datetime import datetime

with open("lastname.txt", "a") as file:
    file.write(f"\nLast update: {datetime.now()}")

print("\n ---- Example 7: copy a file ----")
#copy file "lastname.txt" into a new file
with open("lastname.txt", "r") as readfile:
    with open("newfile.txt", "w") as writefile:
        for eachline in readfile:
            writefile.write(eachline)

print("\n ---- Example 8: pandas a file ----")
import pandas as pd

data ={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25,30,35]
}

df = pd.DataFrame(data)
print(df)

print("\n ---- Example 9: Creating df with pandas from an excel file ----")
df = pd.read_excel("classdata.xlsx")
print(df)
print(df.head())

print("\n----EXERCISE-----")

def email_read():

    gmail_count = 0
    yahoo_count = 0
    hotmail_count = 0


    with open("user_email.txt", "r") as file:

        for eachline in file:
            eachline = eachline.strip()

            if "@gmail" in eachline:
                gmail_count += 1

            elif "@yahoo" in eachline:
                yahoo_count += 1

            elif "@hotmail" in eachline:
                hotmail_count += 1


    with open("reportemail.txt", "w") as report:
        report.write("gmail = " + str(gmail_count) + "\n")
        report.write("yahoo = " + str(yahoo_count) + "\n")
        report.write("hotmail = " + str(hotmail_count) + "\n")

    return gmail_count, yahoo_count, hotmail_count

result = email_read()
print("Email counts:", result)