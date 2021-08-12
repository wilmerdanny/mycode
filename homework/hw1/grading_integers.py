#!/usr/bin/env python3




def grading_integers(list):
    list = []
    i = 0
    while i <= len(list):
        if list[i] >= 90:
            print("Thats an A")
        elif list[i] >= 80:
            print("Thats a B")
        elif list[i] >= 70:
            print("Thats a C")
        elif list[i] >= 60:
            print("Thats a D")
        else:
            print("Thats an F")


print(grading_integers(
    list = float(input("Please enter a list of grade numbers:"))
    )






