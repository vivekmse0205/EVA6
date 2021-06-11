
Session -6 Experiments

Step - 1
```
Train a model with Group Norm
```

Step - 2
```
Train a model with Layer Norm
```
Step -3
```
Train a model with Batch Norm+L1 Loss
```
## Description:
model.py - File which contains model that take a type of normalization as parameter and creates dynamically
Session_6_Assignment.ipynb contains all the 3 experiments on LN,BN,GN together with their acc and loss grapth
```python
python model.py --norm_type LN
```

Model Summary with BN
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
            Conv2d-1            [-1, 8, 26, 26]              72
              ReLU-2            [-1, 8, 26, 26]               0
       BatchNorm2d-3            [-1, 8, 26, 26]              16
            Conv2d-4           [-1, 16, 26, 26]           1,152
              ReLU-5           [-1, 16, 26, 26]               0
       BatchNorm2d-6           [-1, 16, 26, 26]              32
         MaxPool2d-7           [-1, 16, 13, 13]               0
            Conv2d-8            [-1, 8, 13, 13]             128
              ReLU-9            [-1, 8, 13, 13]               0
           Conv2d-10            [-1, 8, 11, 11]             576
             ReLU-11            [-1, 8, 11, 11]               0
      BatchNorm2d-12            [-1, 8, 11, 11]              16
        Dropout2d-13            [-1, 8, 11, 11]               0
           Conv2d-14             [-1, 16, 9, 9]           1,152
             ReLU-15             [-1, 16, 9, 9]               0
      BatchNorm2d-16             [-1, 16, 9, 9]              32
        Dropout2d-17             [-1, 16, 9, 9]               0
           Conv2d-18             [-1, 24, 7, 7]           3,456
             ReLU-19             [-1, 24, 7, 7]               0
      BatchNorm2d-20             [-1, 24, 7, 7]              48
        Dropout2d-21             [-1, 24, 7, 7]               0
           Conv2d-22             [-1, 24, 7, 7]             576
             ReLU-23             [-1, 24, 7, 7]               0
        AvgPool2d-24             [-1, 24, 1, 1]               0
           Conv2d-25             [-1, 16, 1, 1]             384
             ReLU-26             [-1, 16, 1, 1]               0
      BatchNorm2d-27             [-1, 16, 1, 1]              32
           Conv2d-28             [-1, 10, 1, 1]             160

    Total params: 7,832
    Trainable params: 7,832
    Non-trainable params: 0

![Different Normalization](https://machinelearningknowledge.ai/wp-content/uploads/2020/12/Batch-Normalization-vs-Layer-Normalization-in-Keras.png)

## Result:
![Accuracy 3 models](https://raw.githubusercontent.com/vivekmse0205/EVA6/main/Session-6/acc.png)
![Loss 3 models](https://raw.githubusercontent.com/vivekmse0205/EVA6/main/Session-6/loss.png)


## Team:             
•	Vivek 
•	Jenisha 
•	Chethan Kumar
