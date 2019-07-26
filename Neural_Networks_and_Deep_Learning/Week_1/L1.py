

def L1(y_output, y_input):
    """ L1 Loss Function calculates the sum of the absolute difference between the predicted and the input"""
    return sum(abs(y_input - y_output))