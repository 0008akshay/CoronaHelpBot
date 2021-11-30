import torch
import torch.nn as nn


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        """ReLU(rectified linear unit) for short is a piecewise linear function that 
        will output the input directly if it is positive, otherwise, it will output zero"""
        self.relu = nn.ReLU()
    
    #The "forward pass" refers to calculation process, values of the output layers from the inputs data
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out # A loss function is calculated from the output values.