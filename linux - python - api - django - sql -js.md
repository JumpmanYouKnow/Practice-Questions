**Linux**

How do I reconnect to an existing screen or tmux session named 'leaflink'?

screen -r leaflink

How would I "follow" the output of a server log named 'access.log'?

tail -f access.log

How would I remove all files in a directory that start with an 'a' and have a '.jpg' extension?

rm a*.jpg

How would I see all running processes and memory they consume?

ps aux

How would I combine the following files: '1.log', '2.log', '3.log' into a single file named 'master.log'?

cat 1.log 2.log 3.log > master.log

**Database**

What is a database index and when is it wise to build an index?

Database index is a data structure that contains the values for a specific column in a table. (Mostly B-tree)
It's like the table of contents for tables, although it often greatly improve time complexity for retrieving data, it took lots of extra space. 
It's usually wise to build an index when:
1. The column would usually be used as a foreign key(frequently retrieved).
2. The column is clustering, narrow, unique(low-cardinality), stable(rarely update or delete)

Table Name: 'pets'

| owner |      pet      | age |
|-------|:-------------:|----:|
| bob   |      dog      |  3  |
| cindy |      cat      |  5  |
| lisa  |      cat      |  7  |
| tony  |      fish     |  1  |


Write a query to return all unique pets in the 'pets' table.

SELECT DISTINCT pet FROM pets;

Write a query to return the oldest cat owner in the 'pets' table.

SELECT TOP  owner  FROM (SELECT * FROM pets ORDER BY age DESC) AS oldest_owner LIMIT 1; 

Write a query to return the average age of all cats and dogs in the 'pets' table.

SELECT AVG(age) as Ageaverage FROM pets WHERE pet = 'dog' OR pet = 'cat'; 

**Python**

What is your favorite python module and why?

NumPy. NumPy is a very powerful libray, it provides me a lot of convenience when I need linear algebra or other
mathematic operations and calculations. Recently I am interested in learning Machine Learning and learning TensorFlow, 
I found Numpy more important because I need it everywhere. It greatly helps me simplify my code and saves my time.


Write python code to return an iterable which contains all unique numbers in the list [1, 3, 4, 5, 2, 2, 1, 4].

myD1 = {} #dictionary 
for item in a:
    myD1[item] = item
myIterable = [k for k in myD1]

Write python code to find the largest number in [1, 3, 4, 5, 2, 2, 1, 4].

max([1, 3, 4, 5, 2, 2, 1, 4])

Write python code to return common elements between l = [1, 'A', 3, 5] and p = [8, 3, 5, 'A'].

#dictionary built on hash table in Python, therefore each search 
#for the each takes O(1) time, overall find common takes O(n)time
l = [1, 'A', 3, 5]
p = [8, 3, 5, 'A']

myD = {} #dictionary 
for item in l:
    myD[item] = item
for item in p:
    value = myD.get(item)
    if value != None: # if can't find in dict
        print value

Write python code to sort the following from highest to lowest [1, 3, 4, 5, 2, 2, 1, 4].

[1, 3, 4, 5, 2, 2, 1, 4].sort(reverse = True)

**Django**

Write a formal Django model for a typical 'Blog' entry.

class Post(models.Model):
	author = models.ForeignKey(required = True)
	title = models.CharField(required = True)
	body = models.TextField(required = True)
	category = models.ForeignKey()
	created_date = models.DateTimeField(
				default =timezone.now)
	published_date = models.DateTimeField(
    	        blank=True, null=True)

Using the Django ORM how would you find all owners in the 'pets' table above who have a cat older than 1? Assume the Model name is "Pet".

Pet.objects.fliter.(pet = 'cat', age__gt= 1).values_list('owner', flat = True)


Render your query set above using Django template syntax as an HTML Table.

<table>
    <th> owner </th>
    <th> pet</th>
    <th> age</th>
    <tr>
    {% for record in ojbect_list %}
    {% if record.pet = 'cat' %}
    {% elif record.age > 1 %} 
    <td>{{ record.owner }}</td>
    {% end if%}
    {% endfor %}
    </tr>
</table>


**API**

Write python code to print all pet owner names for the following 'JSON web service'.
<http://dpaste.com/3NX4EXA.txt>

import json
import urllib2

#open the url
url = 'http://dpaste.com/3NX4EXA.txt'

#trans json string to python object
pets_data = json.load(urllib2.urlopen(url))

for pet in pets_data:
    for owner in pets_data[pet]:
        print owner


**Javascript**

What is the DOM?

The Document Object Model (DOM) is a programming API for HTML and XML documents

Write a jQuery selector to select all list items that have 'cat' as a class.


```<ul>
    <li class="dog">dog</li>
    <li class="cat">cat</li>
    <li class="fish">fish</li>
    <li class="cat">cat</li>
</ul>
```


$('ul li.cat')
