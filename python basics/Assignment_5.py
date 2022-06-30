# ASSIGNMENT - 5

"""1. What does an empty dictionary&#39;s code look like?"""
d = {}
print(d)

"""2. What is the value of a dictionary value with the key &#39;foo&#39; and the value 42?"""
# 42

"""3. What is the most significant distinction between a dictionary and a list?"""
# list store values of different data types and dictionary store data in the form of key value pair

"""4. What happens if you try to access spam[&#39;foo&#39;] if spam is {&#39;bar&#39;: 100}?"""
# it will give KeyError

"""5. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
&#39;cat&#39; in spam.keys()?"""
# 'cat' in spam checks 'cat' key in dictionary and 'cat' in spam.keys()  will check if key with name 'cat' exist

"""6. If a dictionary is stored in spam, what is the difference between the expressions &#39;cat&#39; in spam and
&#39;cat&#39; in spam.values()?"""
# 'cat' in spam checks 'cat' key in dictionary and 'cat' in spam.values() will check for value with the key 'cat'

"""
7. What is a shortcut for the following code?
if &#39;color&#39; not in spam:
spam[&#39;color&#39;] = &#39;black&#39;
"""
# spam.setdefault('color', 'black')

"""8. How do you &quot;pretty print&quot; dictionary values using which module and function?"""
# import json
# json.dumps(dict)


