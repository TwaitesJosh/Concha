# Concha
Opt1 represents the code used for the optional task 1, create an API

The API is created using flask in app.py. I am hosting it on an AWS ec2 server.

`ec2-18-118-160-157.us-east-2.compute.amazonaws.com`

This is an example curl request:

` curl -X POST ec2-18-118-160-157.us-east-2.compute.amazonaws.com:80/predict -H "Content-Type: application/json" -d "[5,30,5]" `

It is worth noting, that linux and windows get really ansty if you mix up ' and " in a curl request. I lost 6 hours of my life fixing that issue.


As mentioned in the report, I use eager memoisation and pre-compute all possible model inputs. This is saved as `csv_for_model_3_input.csv`, the model.py is just a method for loading this into memory and using it to make predictions.

The app.py simply takes the input and writes out the predictions. No error checking is done on the inputs, as I didn't have time to implement this.
