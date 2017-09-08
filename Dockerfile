FROM keyi/python2-mcr2017a-rpi-isl

COPY JMI_O196/ ./JMI_O196
COPY setup.py ./
COPY O196_JMI_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
