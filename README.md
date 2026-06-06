**Problem Statement :-**
To implemement a given Neural network model and train it on the Fashion-MNIST dataset using PyTorch. 

**Files included in Repo :-**
1. Python notebook(Colab) - Containing the Neural network alongwith its training pipeline and complete workflow. Plots of Loss vs EPOCHS and  Accuracy vs EPOCHS are present inside the notebook itself. 

2. Saved Model - A pickle file containings the final model and its saved weights and biases.

3. Submission csv - A CSV file containing the predicted results on the testing dataset of Fashion MNIST. It also contains the true labels of the images. 

4. Requirements - Contains list of all necessary requirements and libraries required to run the project.

*Training Setup*
For this project, I used 2 datasets :-
Fashion MNIST training dataset (size = 60000)
Fashion MNIST testing dataset (size = 10000)

The training dataset was split into 2 parts :
**Train set(Size =50000)** :This was for training the model weights and biases, calculating gradient, reducing loss and implementing backpropagation.

**Validation set (size = 10000)** : This was for evaluating the model performance in each EPOCH, during the training. No gradient calculation or backpropagation is during validation, just the loss and accuracy is calculated.

No. of EPOCHS  = 15

Final Training accuracy :- 87.95%
Final Validation accuracy :- 86.39%

Final Training loss :- 0.3326
Final Validation loss :-0.3711

_Testing_
For testing, I used the model on the testing dataset and saved the predictions labels, alongwith the true labels in the submission csv file for each image in the testing dataset




