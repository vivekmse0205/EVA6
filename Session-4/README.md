# Session 4 Assignment

## NN Architecture
WRITE IT AGAIN SUCH THAT IT ACHIEVES
 - 99.4% validation accuracy
 - Less than 20k Parameters
 - You can use anything from above you want. 
 - Less than 20 Epochs
 - Have used BN, Dropout, a Fully connected layer, have used GAP. 

## Model Summary:
        Layer (type)               Output Shape         Param 
            Conv2d-1           [-1, 16, 28, 28]             144
              ReLU-2           [-1, 16, 28, 28]               0
       BatchNorm2d-3           [-1, 16, 28, 28]              32
            Conv2d-4           [-1, 16, 28, 28]           2,304
              ReLU-5           [-1, 16, 28, 28]               0
       BatchNorm2d-6           [-1, 16, 28, 28]              32
            Conv2d-7           [-1, 32, 26, 26]           4,608
              ReLU-8           [-1, 32, 26, 26]               0
       BatchNorm2d-9           [-1, 32, 26, 26]              64
        MaxPool2d-10           [-1, 32, 13, 13]               0
           Conv2d-11            [-1, 8, 13, 13]             256
             ReLU-12            [-1, 8, 13, 13]               0
           Conv2d-13           [-1, 16, 11, 11]           1,152
             ReLU-14           [-1, 16, 11, 11]               0
      BatchNorm2d-15           [-1, 16, 11, 11]              32
        Dropout2d-16           [-1, 16, 11, 11]               0
           Conv2d-17             [-1, 16, 9, 9]           2,304
             ReLU-18             [-1, 16, 9, 9]               0
      BatchNorm2d-19             [-1, 16, 9, 9]              32
           Conv2d-20             [-1, 32, 7, 7]           4,608
             ReLU-21             [-1, 32, 7, 7]               0
      BatchNorm2d-22             [-1, 32, 7, 7]              64
        Dropout2d-23             [-1, 32, 7, 7]               0
           Conv2d-24              [-1, 8, 7, 7]             256
             ReLU-25              [-1, 8, 7, 7]               0
           Conv2d-26             [-1, 16, 5, 5]           1,152
             ReLU-27             [-1, 16, 5, 5]               0
      BatchNorm2d-28             [-1, 16, 5, 5]              32
        Dropout2d-29             [-1, 16, 5, 5]               0
        AvgPool2d-30             [-1, 16, 1, 1]               0
           Linear-31                   [-1, 10]             170
      Total params: 17,242
      Trainable params: 17,242
      Non-trainable params: 0
      Input size (MB): 0.00
      Forward/backward pass size (MB): 1.29
      Params size (MB): 0.07


## Optimizer:
 > SGD with learning rate of 0.01

## Loss Function:
 > negative log likelihood loss

## Optimal Epoch:

## Result:

## Team:             
•	Vivek 
•	Jenisha 
•	Chethan Kumar
•	Suman
