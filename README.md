# Invictus Capital
## Overview
The system will offer service that provides three functions:

1.	A function that squares each odd number in a given list of 
integers.
2.	A function that accepts a list of strings, and returns a 
dictionary of the strings - the key being the original string, and 
the value being a compressed version of that string Huffman  
3.	A function that decodes a given string previously encoded.  

### Service Names
``
nameko_service.square_list
``  
``
nameko_service.compress_string
``  
``
nameko_service.decode_string
``

The system is built using Python 3.7.4 with a Nameko framework for the
services. We are also using the dahuffman package for the compression.

### Nameko
Nameko is an easy-to-use solution for microservices in Python. It 
helps to develop scalable and distributed services as soon as you 
get to use it. This framework will manage all the communication, 
transport and concurrency, you only have to focus on your project 
specifications.

## Installation
### Initial Installation
Install Python 3.7 and follow commands. Allow Python to be added to 
the PATH.

Once Python is installed. Install virtualenv via pip so that all 
dependencies are stored inside the virtual enviroment. Open the 
command line and run the following.

```bash
pip install virtualenv
```

Create virtual enviroment using the following command:
```bash
virtualenv venv
```

Activate the virtual enviroment. On Windows use the following.
```bash
venv\Scripts\activate.bat
```

Install the required packages, using pip and the requirements file.
```bash
pip install -r requirements.txt
````

## Setup
After this, you need to launch an AMQP server (it will be your main
 backend for communication between services). We will use RabbitMQ
 for this example.
```bash
docker run -d -p 5672:5672 --name rabbitmq rabbitmq:3
````

Open up docker and navigate to the project. Then run the following
command:
```bash
docker-compose up
````

Once the rabbitmq is running, open up a terminal and navigate to the
project. Activate the virtual enviroment. On Windows OS use the following
command.
```bash
venv\Scripts\activate.bat
```

Then once in the virtual enviroment, run the service using the below command:
```bash
nameko run nameko_service --broker amqp://guest:guest@192.168.99.100
```

### Test
To test the services open up another terminal, after rabbitmq and the
service is running. Run the following command.

```bash
nameko shell --broker amqp://guest:guest@192.168.99.100
```

In the shell you can use the below to test the 3 services.  
Square List Numbers:
```bash
n.rpc.nameko_service.square_list([9, 8, 6, 7])
```
Compress String:
```bash
n.rpc.nameko_service.compress_string(['Blah', 'Hello', 'Bye'])
```
Decode String:
```bash
n.rpc.nameko_service.decode_string('<éIĎ')
```