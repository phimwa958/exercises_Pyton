# **Single Layer Perceptron Network using Python**

### **Perceptron:**
![Perceptron Network](https://www.mathworks.com/help/deeplearning/ug/percept_perneur.gif)

---

### **How the Perceptron Model Works**
The Perceptron is a simple artificial neuron model used as a **binary classifier**. It classifies input data into binary classes (e.g., 0 or 1) through training, where it learns from inputs with known outputs.

During training, the model's predicted outputs are compared with actual labels, and weights are adjusted using the **Perceptron Learning Rule** to minimize errors. This improves the model's classification accuracy over time.

### **Components of the Perceptron Model**

The Perceptron model includes:
1. **Summation Function**: Takes a weighted sum of the inputs.
2. **Transfer (Activation) Function**: Applies a hard-limit function ("hardlim") to produce a binary output (0 or 1) based on the weighted sum.

The model equation is:

**a = hardlim(WX + b)**

Where:
- **a**: Output from the activation function, representing the class of the input
- **W**: Weight matrix
- **X**: Input data
- **b**: Bias term

The Perceptron operates as a dense layer, meaning every input is connected to each neuron, and each neuron produces an output after passing through the activation function.

---

### **Code Overview**

The implementation includes the following key methods:

1. **_initialize_weights(self)**  
   Initializes the weights randomly for each neuron in the network.

2. **initialize_all_weights_to_zeros(self)**  
   Sets all weights to zero, useful for observing the effect of training with zero-initialized weights.

3. **predict(self, X)**  
   Uses the current weights to predict the output for given input data \( X \). 

4. **print_weights(self)**  
   Prints the current weight matrix, including bias.

5. **train(self, X, Y, num_epochs, alpha)**  
   Trains the model by updating weights according to the **Perceptron Learning Rule** over a specified number of epochs and learning rate (\( \alpha \)).

6. **calculate_percent_error(self, X, Y)**  
   Calculates the percentage of incorrect predictions, allowing evaluation of the model's performance over training epochs.

7. **Main Program**  
   Contains the driver code to initialize and train the model on sample data, providing a complete example of how to use the Perceptron class.

---

### **Usage Example**

Below is a sample usage example of running the Perceptron model on a dataset.

```python
import numpy as np
from sklearn.model_selection import train_test_split
from perceptron_import_file import Perceptron, load_iris_data

# Load the dataset
X, Y = load_iris_data('iris.data.txt')

# Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(X.T, Y.T, test_size=0.3, random_state=42)
X_train, X_test, Y_train, Y_test = X_train.T, X_test.T, Y_train.T, Y_test.T

# Initialize the model
model = Perceptron(input_dimensions=4, number_of_classes=3, seed=1)
model.initialize_all_weights_to_zeros()

# Train the model and calculate percent error
percent_error = []
for epoch in range(50):
    model.train(X_train, Y_train, num_epochs=1, alpha=0.001)
    percent_error.append(model.calculate_percent_error(X_test, Y_test))

# Print results
print("Percent error over epochs:", percent_error)
print("Final weights:\n", model.print_weights())

### **Explanation of the Code**
1. Data Loading: The load_iris_data function loads the Iris dataset, converts labels to numeric values, and applies one-hot encoding.
2. Model Initialization: The Perceptron model is created with specific input dimensions and number of classes.
3. Training: The model is trained for 50 epochs. Each epoch updates the model's weights based on the current error.
4. Evaluation: The percent error over epochs is calculated, and the final weight matrix is printed.