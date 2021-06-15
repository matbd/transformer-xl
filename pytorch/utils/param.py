import torch
import torch.nn as nn

class ParameterModule(nn.Module):
    def __init__(self, value):
        super(ParameterModule, self).__init__()
        self.parameter = nn.Parameter(value)
