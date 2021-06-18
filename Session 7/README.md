#### CIFAR10

Achieve 85% accuracy. Total Params to be less than 200k

#### 1. Architecture
#### Model 1

[1] Block1, Block2, Block3, Block4 \\ 

[2] Used dilated kernels instead of stride \\

[3] No maxpooling layer


#### 2. Receptive Field Calculation > 52

#### 3. Add two Depthwise Seperable Convolution


#### 4. Add Dilated Kernel

#### 5. Add Global Average Pooling


#### 6. Add augumentation using Albumentation library and apply:
[1] horizontal flip

[2]  shiftScaleRotate

[3] coarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of your dataset), mask_fill_value = None)


