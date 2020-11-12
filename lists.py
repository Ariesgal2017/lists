#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: Lists!
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Jennifer Schneider"

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.


def match_ends(words):
    #assigning a value of 0 to the count for words
    
    amt = 0
    #indicating if any word in words is more than or equal to 2 | the last 2 indexes(0, -1) are the same 
    if match_ends(word) > 1 and word[0] == word[-1]
      #add 1 to amt
    amt += 1

      return amt






# B. front_x
# Given a list of strings, return a list with the strings in
# sorted order, except group all the strings that begin with
# 'x' first.
# Example:
#   ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
#   ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each
# of them before combining them.


def front_x(words):
#assigning a value for words starting with x and another for words starting with any other letter
    xlist = []
    avglist = []

    for word in words:
        #if any word ends with the letter x
        if word.startswith('x'):
        # add it to xlist 
            xlist.append(word)
        else:
            #every other letter goes in avglist
            avglist.append(word)
    
    return sorted(xlist) + sorted(avglist)


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in
# increasing order by the last element in each tuple.
# Example
#   [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
#   [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element from each tuple.


def sort_last(tuples):
    #defining a variable to hold the current tuples to get the value at index -1
    def last(tuples): return tuples[-1]
    #sorts the lists in order with the key from above
    return sorted(tuples, key=last)


# D. remove_adjacent
# Given a list of numbers, return a list where all adjacent
# equal elements have been reduced to a single element.
# Example:
#   [1, 2, 2, 3] -> [1, 2, 3]
# You may create a new list or modify the passed in list.
# Hint: Don't use set()


def remove_adjacent(nums):
    #assigning nums to list1
    list1 = nums
    #for index of i in nums
    for i in nums:
        #for index of n in list1
        for n in list1:
            #if I is equal to n
            if i == n:
                #create a second list(list2) and add i to it
                list2 = i
                #print list 2
                print(list2)
        


# E. zip_merge
# Given two lists, combine the values from their corresponding
# indices into a single list.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# result = ['My', 'name', 'is', 'Kelly']
# Hint: Think of it as "zipping" two lists together.  Is there
# a built-in function in python that will do this?


def zip_merge(list1, list2):
    #created an empty list
    temp = []
    #take i from zip_merge
for i in zip_merge(list1, list2):
    #for n in i
    for n in i:
        #append n into the list temp
        temp.append(n)

# F. empty_filter
# Given a single list containing strings, empty strings, and
# None values:  Return a new list with the same elements, but
# strip out (filter) the empty strings and None values away.
# example: list1 = ["Mike", "", "Emma", None, "Kelly", "", "Brad", None]
# result:  ["Mike", "Emma", "Kelly", "Brad"]
# Hint: There is a Python idiom for doing this.  Can you find it?


def empty_filter(list1):
    list2 = filter(None, list1)
    list2 = filter(bool, list1)
    list2 = (len, list1)
    #if x is not equal to an empty string
    [x for x in list1 if x != '']
    
        return list2(x)


# G. linear_merge
# Given two lists sorted in increasing order, create and
# return a merged list of all the elements in sorted order.
# You may modify the passed in lists.
# The solution should work in "linear" time, making a single
# pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not O(n)
# linear time and the two lists are already provided in
# ascending sorted order.


def linear_merge(list1, list2):
result = []
while len(list1) and len(list2):
    if list1(0) < list2(0):
        result.append(list1.pop(0))
    else:
        result.append(list2.pop(0))

        result.extend(list1)
        result.extend(list2)
        
    return result
    #made this comment so i could create a pull request
