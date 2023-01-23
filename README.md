# Coupled_Signals_Classification

# Data
Each sample consists of two signals coupled together (each sample has two signals), like the below image:

![Picture1](https://user-images.githubusercontent.com/44122487/213175445-412be718-4b86-4d10-a4f9-70a6deddf3d6.png)

# Feature extraction
In signal processing/classification feature extraction is an extremely important stage, as a proper feature extraction will lead to highly accurate classification. On the contrary, poor/blind feature extraction is useless and won't be effective for classification.

I considered the phase shift and/or signal similarity between two signals, as the appropriate feature, for classification. As you can see from the below image, the extracted feature are completely separate, therefore the classification can be done even with a simple threshold (i.e. there is no need for a machine/deep learning model).

![Picture2](https://user-images.githubusercontent.com/44122487/213178967-37a32288-32a0-4189-8365-be2a817921d3.png)


I think it is so wise to extract features somehow they are separated maximally. As you can see in this project, with maximal separated features there is no need for training a classifier, like a deep neural network. 

