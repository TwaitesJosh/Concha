# Concha

The report covers more or less everything.

Main represents the code used for the main task. e.g. only 3 inputs and no API


opt-1 represents the code used for the API, 


opt-2 represents the code used for the 4 input task

The API is on a AWS ec2 server adress:`ec2-18-118-160-157.us-east-2.compute.amazonaws.com`

Docker containers storing the code for main and opt-2 are located in my docker-hub account `twaitesjosh`

The commands:

` docker pull twaitesjosh/concha-main ` \ ` docker pull twaitesjosh/concha-opt2 ` 

` docker run -i twaitesjosh/concha-main `\ `docker run -i twaitesjosh/concha-opt2` 

will allow you access to the containers. The `-i` tag is becuase they are interactive.

