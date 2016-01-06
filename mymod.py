import matplotlib.pyplot
import numpy

def plot_data(data):
    """Plot the mean, maximum and minimum values of data

    data is a numpy array taken from a temperature data set
    """
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
    axis1 = fig.add_subplot(1,3,1)
    axis2 = fig.add_subplot(1,3,2)
    axis3 = fig.add_subplot(1,3,3)
    
    axis1.set_ylabel("Mean")
    axis1.plot(data.mean(axis=0))
    
    axis2.set_ylabel("Max")
    axis2.plot(data.max(axis=0))
    
    axis3.set_ylabel("Min")
    axis3.plot(data.min(axis=0))
    
    fig.tight_layout()
    matplotlib.pyplot.show(fig)


def check_data(data):
    "More words"
    if (data.max(axis=0)[0]==0.0) and (data.max(axis=0)[20]==20.0):
        print("Odd max")
    elif (sum(data.min(axis=0)) == 0.0):
        print("Odd min")
    else:
        print("OK")
