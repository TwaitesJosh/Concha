# Concha
Main represents the code used for the main task. e.g. only 3 inputs and no API

Docker containers storing the code for main and opt-2 are located in my docker-hub account `twaitesjosh`


The commands:

` docker pull twaitesjosh/concha-main ` \ ` docker pull twaitesjosh/concha-opt2 ` 


` docker run -i twaitesjosh/concha-main `\ `docker run -i twaitesjosh/concha-opt2` 


will allow you access to the containers.


As mentioned in the report, I use eager memoisation and pre-compute all possible model inputs. This is saved as `csv_for_model_3_input.csv`, the model.py is just a method for loading this into memory and using it to make predictions.

The main.py simply takes the input and writes out the predictions. No error checking is done on the inputs, as I didn't have time to implement this.
