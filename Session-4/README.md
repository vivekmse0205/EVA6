# Session 4 Assignment

## NN Architecture
WRITE IT AGAIN SUCH THAT IT ACHIEVES
 - 99.4% validation accuracy
 - Less than 20k Parameters
 - You can use anything from above you want. 
 - Less than 20 Epochs
 - Have used BN, Dropout, a Fully connected layer, have used GAP. 

## Model Summary:
            Conv2d-1           [-1, 16, 28, 28]             144
              ReLU-2           [-1, 16, 28, 28]               0
       BatchNorm2d-3           [-1, 16, 28, 28]              32
            Conv2d-4           [-1, 16, 28, 28]           2,304
              ReLU-5           [-1, 16, 28, 28]               0
       BatchNorm2d-6           [-1, 16, 28, 28]              32
            Conv2d-7           [-1, 64, 28, 28]           9,216
              ReLU-8           [-1, 64, 28, 28]               0
       BatchNorm2d-9           [-1, 64, 28, 28]             128
        MaxPool2d-10           [-1, 64, 14, 14]               0
           Conv2d-11            [-1, 8, 14, 14]             512
             ReLU-12            [-1, 8, 14, 14]               0
           Conv2d-13           [-1, 16, 12, 12]           1,152
             ReLU-14           [-1, 16, 12, 12]               0
      BatchNorm2d-15           [-1, 16, 12, 12]              32
        Dropout2d-16           [-1, 16, 12, 12]               0
           Conv2d-17           [-1, 16, 10, 10]           2,304
             ReLU-18           [-1, 16, 10, 10]               0
      BatchNorm2d-19           [-1, 16, 10, 10]              32
           Conv2d-20           [-1, 16, 10, 10]             256
             ReLU-21           [-1, 16, 10, 10]               0
           Conv2d-22             [-1, 16, 8, 8]           2,304
             ReLU-23             [-1, 16, 8, 8]               0
      BatchNorm2d-24             [-1, 16, 8, 8]              32
        AvgPool2d-25             [-1, 16, 1, 1]               0
           Linear-26                   [-1, 10]             170
     Total params: 18,650
     Trainable params: 18,650
     Non-trainable params: 0


## Optimizer:
 > SGD with learning rate of 0.01

## Loss Function:
 > negative log likelihood loss

## Optimal Epoch:
19

## Result:


## Logs
loss=0.0581904835999012 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.67it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0305, Accuracy: 9902/10000 (99%)

loss=0.09158757328987122 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.55it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0338, Accuracy: 9904/10000 (99%)

loss=0.014537792652845383 batch_id=468: 100%|██████████| 469/469 [00:12<00:00, 38.83it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0289, Accuracy: 9915/10000 (99%)

loss=0.057427819818258286 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.70it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0271, Accuracy: 9916/10000 (99%)

loss=0.06304991245269775 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.23it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0369, Accuracy: 9882/10000 (99%)

loss=0.026372184976935387 batch_id=468: 100%|██████████| 469/469 [00:11<00:00, 39.59it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0267, Accuracy: 9921/10000 (99%)


## Team:             
•	Vivek 
•	Jenisha 
•	Chethan Kumar
•	Suman
