import torch
import numpy as np

from torch import nn

class NN(nn.Module):
    
    def __init__(self):
        super(NN, self).__init__()

        # 2 fully connected layer
        self.fc1 = nn.Linear(784, 5)
        self.fc2 = nn.Linear(5, 10)
        
        # 2 activation function
        self.sigmoid = nn.Sigmoid()
        self.softmax = nn.Softmax(dim=1)

    # define the forward pass
    def forward(self, x):
        
        # feed into first layer
        x1 = self.fc1(x)
        x1 = self.sigmoid(x1)

        # feed into output layer
        x2 = self.fc2(x1)
        x2 = self.softmax(x2)
        
        return x2

def predict_model(x, model):
    
    # convert into tensor
    x_tensor = torch.tensor([x]).float()

    with torch.no_grad():

        # predict
        preds = model(x_tensor)
        preds = preds.detach().cpu()

        # get max index from predict
        return torch.argmax(preds).item()

def preprocess(x):

    # get rgb channel
    r, g, b = [], [], []
    for i in range(0, len(x), 4):
        r.append(x[i])
        g.append(x[i+1])
        b.append(x[i+2])
    rgb = np.array([r, g, b])

    # convert rgb to grayscale
    rgb_weights = [0.2989, 0.5870, 0.1140]
    grayscale = np.dot(rgb_weights, rgb).reshape(140, 140)

    # rescale image to 28 x 28
    rescale = []
    for i in range(0, len(grayscale), 5):
        for j in range(0, len(grayscale), 5):
            res = sum([grayscale[p, q] for p in range(i, i+5) for q in range(j, j+5)])
            rescale.append(res / 255)
    rescale = np.array(rescale)

    return rescale