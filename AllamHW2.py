#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:17:20 2022

@author: ibrahim
"""
#First List Loop
pets=['Cat','Dog','Bird','Pig']
for x in range(len(pets)):
    print(pets[x])


#First Neat List Loop
pets=['Cat','Dog','Bird','Pig']
owner=['Abe','Sam','Ben','Rob']
for x in range(len(owner)):
    print(owner[x],'owns a',pets[x])

#Your First List Loop
pets=['Cat','Dog','Bird','Pig']
owner=['Abe','Sam','Ben','Rob']
for pets, owner in zip(pets,owner):
    print(owner,"owns a",pets)

#Working List
careers=['Accountant','Teacher','Doctor','Lawyer']
print(careers.index('Teacher'))
print('Teacher' in careers)
careers.append('Nurse')
careers.insert(0,'Chef')
print(careers)
for x in range(len(careers)):
    print(careers[x])
    
#Starting From Empty
empty_list=[]
empty_list.append('Chef')
empty_list.append('Accountant')
empty_list.append('Teacher')
empty_list.append('Doctor')
empty_list.append('Lawyer')
empty_list.append('Nurse')
print(empty_list)
print('The first career I thought of was a', empty_list[0])
print('The last career I thought of was a', empty_list[5])

#Ordered Working List
careers=['Accountant','Teacher','Doctor','Lawyer']
for x in careers:
    print("Original Order- ",careers)
    print("Alphabetical Order- ",sorted(careers))
    print("Original Order- ",careers)
    print("Reverse Alphabetical Order- ",sorted(careers,reverse=True))
    print("Original Order- ",careers)
    careers.reverse()
    print("Reverse Order- ",careers)
    careers.reverse()
    print("Original Order- ",careers)
    careers.clear()
    careers.append("Accountant")
    careers.append("Doctor")
    careers.append("Lawyer")
    careers.append("Teacher")
    print("Alphabetical Order- ",careers)
    careers.clear()
    careers.append("Teacher")
    careers.append("Lawyer")
    careers.append("Doctor")
    careers.append("Accountant")
    print("Original Order- ", careers)
    break

#Ordered Numbers
numbers=[17,9,25,32,6]
for x in numbers:
    print("Original Order- ",numbers)
    print("Increasing Order- ",sorted(numbers))
    print("Original Order- ",numbers)
    print("Decreasing Order- ",sorted(numbers,reverse=True))
    print("Original Order- ",numbers)
    numbers.reverse()
    print("Reverse Order- ",numbers)
    numbers.reverse()
    print("Original Order- ",numbers)
    numbers.clear()
    numbers.append(6)
    numbers.append(9)
    numbers.append(17)
    numbers.append(25)
    numbers.append(32)
    print("Increasing Order- ",numbers)
    numbers.clear()
    numbers.append(32)
    numbers.append(25)
    numbers.append(17)
    numbers.append(9)
    numbers.append(6)
    print("Decreasing Order- ",numbers)
    break
    
#List Length
pets=['Cat','Dog','Bird','Pig']
print("The list of pets is",len(pets),"units long")
careers=['Accountant','Teacher','Doctor','Lawyer']
print("The list of careers is",len(careers),"units long")
colors=["Red","Yellow","Blue","Green"]
print("The list of colors is",len(colors),"units long")
