"""ASSIGNMENT-4"""

""" 1. What exactly is []? """
# it is used to make a list data structure in python

"""2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)"""
spam = [2, 4, 6, 8, 10]
spam.insert(2, "hello")
print(spam)
# output - [2, 4, 'hello', 6, 8, 10]

spam = ['a', 'b', 'c', 'd']
"""3. What is the value of spam[int(int(&#39;3&#39; * 2) / 11)]?"""
print(spam[int(int('3' * 2) / 11)])
# output - d

"""4. What is the value of spam[-1]?"""
# d

"""5. What is the value of spam[:2]?"""
# ['a', 'b']


bacon = [3.14, 'cat', 11, 'cat', True]
'''6. What is the value of bacon.index(&#39;cat&#39;)?'''
# 1

'''7. How does bacon.append(99) change the look of the list value in bacon?'''
# it will append 99 at the end of list

'''8. How does bacon.remove(&#39;cat&#39;) change the look of the list in bacon?'''
# [3.14,  11, 'cat', True]

'''9. What are the list concatenation and list replication operators?'''
'''extend keyword is used to concat a list
    list.extend(list2)
    copy method is used to replicate a list
    l2 = l1.copy()
'''

'''10. What is difference between the list methods append() and insert()?'''
# append method insert element at teh end of the list while insert inserts the element at the given index

'''11. What are the two methods for removing items from a list?'''
# pop() and remove() methods are used to remove elements from the list

'''12. Describe how list values and string values are identical.'''
# both are sequential but list is mutable whereas string are immutable

'''13. What&#39;s the difference between tuples and lists?'''
# list and tuples both can store value of different data types but list are mutable and tuple are immutable

'''14. How do you type a tuple value that only contains the integer 42?'''
t = (41,)
print(t)

'''15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?'''
l = [1, 2, 3, 4]
t = (5, 6, 7, 8)

print(tuple(t))
print(list(t))

'''16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they
contain?'''
# they contain the references to the list values

'''17. How do you distinguish between copy.copy() and copy.deepcopy()?'''
# copy() simply copies the element of the list into another list but when we have nested list it makes references of
# the list inside list . deepcopy() is helpful when we have nested list, and it also copies the list inside list .
