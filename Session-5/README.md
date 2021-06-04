Session -5 Experiments

Step - 1
```
Target:
    > Design the base model along with LR scheduler
    > Less than or equal to 15 Epochs
    > Less than 10000 Parameters
Results:
    > Parameters: 7.68k
    > Best Train Accuracy: 98.84
    > Best Test Accuracy: 99.07 (15th Epoch)
Analysis:
    The base model test accuracy reached upto 99.07% while train accuracy was 98.84 which indicates minor underfitting

```

Step - 2
```
Target:
    > Using the same base mode,add image augmentations

Results:
    > Parameters: 7.68k
    > Best Train Accuracy: 98.72
    > Best Test Accuracy: 99.18 (12th Epoch),99.15(14th Epoch)
Analysis:
    The base model test accuracy was stuck at 99.1% while train accuracy was not improving above 98.72
```
Step -3
```
Target:
    > Modify model architecture by adding depth to channels,1X1 filters,reduce dropout

Results:
    > Parameters: 7.83k
    > Best Train Accuracy: 99.04 (10th Epoch)
    > Best Test Accuracy: 99.28 (11th Epoch),99.27(9th Epoch)
Analysis:
    The modified model test accuracy was ~99.2% while train accuracy was not improving above 99.04
```




Final Model Summary
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


## Result:
![Accuracy](https://raw.githubusercontent.com/vivekmse0205/EVA6/main/Session-5/acc.png)
![Loss](https://raw.githubusercontent.com/vivekmse0205/EVA6/main/Session-5/loss.png)


## Logs:

EPOCH: 11
Loss=0.010718464851379395 Batch_id=468 Accuracy=98.99: 100%|██████████| 469/469 [00:26<00:00, 17.74it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0235, Accuracy: 9928/10000 (99.28%)
EPOCH: 12
Loss=0.02246980555355549 Batch_id=468 Accuracy=99.01: 100%|██████████| 469/469 [00:26<00:00, 17.74it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0239, Accuracy: 9922/10000 (99.22%)
EPOCH: 13
Loss=0.07661829888820648 Batch_id=468 Accuracy=99.04: 100%|██████████| 469/469 [00:26<00:00, 17.70it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0240, Accuracy: 9925/10000 (99.25%)
EPOCH: 14
Loss=0.03172140195965767 Batch_id=468 Accuracy=99.00: 100%|██████████| 469/469 [00:26<00:00, 17.80it/s]
Test set: Average loss: 0.0235, Accuracy: 9927/10000 (99.27%)


## Team:             
•	Vivek 
•	Jenisha 
•	Chethan Kumar
•	Suman
