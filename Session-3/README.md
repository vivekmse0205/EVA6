# EVA Session-3 Assignment - Pytorch

## Problem Statement
Write a neural network that can:
take 2 inputs:
    an image from MNIST dataset, and
    a random number between 0 and 9
and gives two outputs:
    the "number" that was represented by the MNIST image, and
    the "sum" of this number with the random number that was generated and sent as the input to the network

## Data 
Train set - MNIST Images(28X28) - 6000
Random Integer - 0-9
Images are flatten into 1D Tensor of [1X784]
Random number is added to image tensor [1X785]

## Loss
MSE Loss. MSE loss is picked because we are trying to model the problem as regression problem. 
Given a input, the model have to predict 2 output, 1 corresponds to the MNIST image and other to the addition value

## Logs
Epoch 0 Train loss = 0.15493248595080988
Epoch 0 Validation loss = 0.1533671794814644
Epoch 1 Train loss = 0.15431905445510927
Epoch 1 Validation loss = 0.155286526114482
Epoch 2 Train loss = 0.1545496146815351
Epoch 2 Validation loss = 0.15384361760989954
Epoch 3 Train loss = 0.1538175434231588
Epoch 3 Validation loss = 0.15717387299719116
Epoch 4 Train loss = 0.15437669115458988
Epoch 4 Validation loss = 0.15437911006373004
Epoch 5 Train loss = 0.15436437831361088
Epoch 5 Validation loss = 0.15457072071320255
Epoch 6 Train loss = 0.154279105937023
Epoch 6 Validation loss = 0.1540331918396803
Epoch 7 Train loss = 0.1543220037032597
Epoch 7 Validation loss = 0.1549082297192077

