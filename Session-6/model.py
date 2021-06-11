from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import torch.nn.functional as F
dropout_value = 0.01

from enum import Enum
class Regulaization(Enum):
  BNORM = 'BN'
  LNORM = 'LN'
  GNORM = 'GN'

class Net(nn.Module):
  def __init__(self,regularization_type=Regulaization.BNORM,group_num=1):
      super(Net, self).__init__()
      self.regularizer = regularization_type
      self.group_num = group_num
      self.conv1 = nn.Sequential(
          nn.Conv2d(1, 8, 3,bias=False),  
          nn.ReLU(),
          self.add_regularizer(8),

          nn.Conv2d(8, 16, 3,padding=1,bias=False),
          nn.ReLU(),
          self.add_regularizer(16),
      )
      self.pool1 = nn.MaxPool2d(2,2)
      self.trans1 = nn.Sequential(
          nn.Conv2d(16, 8, 1,bias=False),
          nn.ReLU(),
      )
      self.conv2 =  nn.Sequential(
          nn.Conv2d(8, 8, 3,bias=False), 
          nn.ReLU(),
          self.add_regularizer(8),
          nn.Dropout2d(dropout_value),

          nn.Conv2d(8, 16, 3,bias=False),  
          nn.ReLU(),
          self.add_regularizer(16),
          nn.Dropout2d(dropout_value),

          nn.Conv2d(16, 24, 3,bias=False),
          nn.ReLU(),
          self.add_regularizer(24),
          nn.Dropout2d(dropout_value), 
      )
      
      self.trans2 = nn.Sequential(
          nn.Conv2d(24, 24, 1,bias=False),
          nn.ReLU(),
      )
      self.conv3 = nn.Sequential(
          nn.Conv2d(8, 24, 3,bias=False),
          nn.ReLU(),
          self.add_regularizer(24),
          nn.Dropout2d(dropout_value),    
      )
      self.gap = nn.Sequential(
          nn.AvgPool2d(6)
      )

      self.conv4 = nn.Sequential(
          nn.Conv2d(24, 16, 1,bias=False),
          nn.ReLU(),
          self.add_regularizer(16),)
          # nn.BatchNorm2d(16),)
      self.conv5 = nn.Sequential(nn.Conv2d(16,10,1,bias=False))

  def forward(self, x):
    x = self.conv1(x)
    x = self.pool1(x)
    x = self.trans1(x)
    x = self.conv2(x)
    x = self.trans2(x)
    x = self.gap(x)
    x = self.conv4(x)
    x = self.conv5(x)
    x = x.view(-1,10)
    return F.log_softmax(x,dim=-1)

  def add_regularizer(self,out_channel):
    """
    Returns regulaizer BN/LN/GN
    """
    if self.regularizer == Regulaization.BNORM:
      return nn.BatchNorm2d(out_channel)
    elif self.regularizer == Regulaization.LNORM:
      return nn.GroupNorm(1,out_channel)
    return nn.GroupNorm(self.group_num,out_channel)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Customize model at runtime with LN/BN/GN')
    parser.add_argument('norm_type', help='Type of Norm-LN,BN,GN')
    args = parser.parse_args()
    model = Net(Regulaization.GNORM,4)
    if args.norm_type == 'LN':
        model =  Net(Regulaization.LNORM)
    elif args.norm_type =='BN':
        model = Net(Regulaization.BNORM)