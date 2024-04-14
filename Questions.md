## Question 1: 

Explain the difference between a stack and a queue. 
Provide real life examples of real-life scenarios where each of them are used appropriately.

Answer: 
- The stack is a linear data structure in which the last inserted element is the first to come out, 
thus is known as a **LIFO (Last In , First Out)** structure. 
- On the other hand, a queue is also linear but the first element added is the first one to be removed, 
so it is a **FIFO (First In, First Out)** structure.

When thinking of them:
- I imagine the stack as a stack of plates, thus , in order to use a certain plate I have to remove all the plates above it otherwise the plates above risk being shattered.
You can also imagine the clothes that you wear, because the last item you added when dressing up in the morning is the first you take down when undressing in the evening.
- For the queue , I like to imagine the queue at a restaurant, because the customer who arrives first, is the one served first, thus the one who exists the restaurant first.

## Question 2: 
What is the difference between an array and a linked list? Provide advantages and disadvantages of each data structure.

Answer:

- The array is a data structure that stores its elements next to each other memory wise. 
So their addresses are easy to calculate, and the access to an element at a specific index is very fast.
Some advantages would be : it uses less memory than linked list, elements can be easily accessed, 
but it comes at the cost of having a fixed size and taking a lot of time to delete and insert elements at a specific index.

- The Linked list is a data structure that stores its elements in different parts of the memory, so, every element need a pointer to the next element.
The big advantage is that it is easy to add elements because of its dynamic size, and also it has a very fast insertion and deletion time.
A disadvantage would be that if you want to access a specific element you need to traverse the whole linked list, and also you use more memory because each element requires the pointer tot the next element.

## Question 3: 
What is HTTP? How is it different from HTTPS?

Answer:

- HTTP = HyperText Transfer Protocol, is a protocol that helps us distribute hypertext documents across World Wide Web.
The application layer called HTTP lies above the TCP layer. This protocol is the foundation of the web as we know it since it has given web browsers and servers a way to communicate with each other.
HTTP is also a stateless protocol.
- HTTPS = HyperText Transfer Protocol Secured, is just HTTP that has an encryption layer since it uses TLS = Transport Layer Security (SSL = Secure Socket Layer)
So it is used for secure communication as when you need to provide login credentials or bank account information.

## Question 4: 
Can you give some examples of common HTTP response codes?

Answer: I know just a few of them like:
- 200 which is for Success
- 404 for Not found
- 400 for Bad request
- 500 for Internal Server Error
- 201 for Created
- 502 for Bad Gateway

## Question 5: 
What is the difference between authorization and authentication?

Answer:

- When we do authentication we check the identity of the user and provide them access to our application based on their login information.
- When we do authorization, the user is already authenticated in our application, and now we want to give them rights to access the resources based on their permissions they have (like admin or just regular user).

## Question 6: 
How would you explain to a 5-year-old how the WWW works?

Answer:

I would try to make an analogy with a city or a library, something like "The WWW , which means World Wide Web , is like a big city filled with a lot of buildings.
Imagine that each building is a different website, where there are interesting things to do and see. But in order to go any building you have to know its address.
Well, when you type in a browser a website name like www.YouTube.com where you go to watch all those cool videos, it is like typing the address in a GPS or telling 
it to a tour guide/taxi driver that knows all the addresses. The GPS for example talks to other big computers called servers, which are like the city's information centers.
So, these servers know where all the buildings are and help bring the website to your screen. 
So, just like exploring a city, the World Wide Web lets you visit different buildings (websites) and discover all sorts of nice things inside them."

I actually used a similar strategy to get my grandparents to understand the internet, and social media, but I just used their home village instead of a city. It worked pretty well :))