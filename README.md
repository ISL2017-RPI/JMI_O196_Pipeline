# JMI_O196_Pipeline

This is the source code for our JMI primitive on the seed data O196.

Once you clone this folder into your local repo, you can directly build the Docker image by:

docker build -t jmi196 ./

Then, you can run the pipeline script in the following way:

docker run jmi196 python O196_JMI_wrapper.py

The output is the selected features stored in a csv file
