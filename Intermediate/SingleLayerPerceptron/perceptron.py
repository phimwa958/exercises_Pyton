import numpy as np

class Perceptron(object):
    def __init__(self, input_dimensions=2, number_of_classes=4, seed=None):
        """
        Initialize Perceptron model
        :param input_dimensions: The number of features of the input data
        :param number_of_classes: The number of classes
        :param seed: Random number generator seed
        """
        if seed is not None:
            np.random.seed(seed)
        self.input_dimensions = input_dimensions
        self.number_of_classes = number_of_classes
        self._initialize_weights()

    def _initialize_weights(self):
        """
        Initialize the weights randomly
        """
        self.weights = np.random.randn(self.number_of_classes, self.input_dimensions + 1)

    def initialize_all_weights_to_zeros(self):
        """
        Initialize all weights to zeros
        """
        self.weights = np.zeros((self.number_of_classes, self.input_dimensions + 1))

    def predict(self, X):
        """
        Make a prediction on an array of inputs
        :param X: Array of input [input_dimensions, n_samples]
        :return: Array of model outputs [number_of_classes, n_samples]
        """
        temp = np.ones((1, X.shape[1]))  # Add a row of 1s for the bias term
        X = np.r_[temp, X]  # Concatenate bias with input
        activation = np.dot(self.weights, X)
        activation[activation < 0] = 0  # Binary step function
        activation[activation > 0] = 1
        return activation

    def print_weights(self):
        """
        Print the weight matrix (Bias included)
        """
        return self.weights

    def train(self, X, Y, num_epochs=10, alpha=0.001):
        """
        Adjust weights using Perceptron learning rule
        :param X: Array of input [input_dimensions, n_samples]
        :param Y: Array of desired (target) outputs [number_of_classes, n_samples]
        :param num_epochs: Number of training epochs
        :param alpha: Learning rate
        """
        # Add row of 1s to X for the bias term
        temp = np.ones((1, X.shape[1]))
        X = np.r_[temp, X]
        
        for epoch in range(num_epochs):
            predictions = self.predict(X[1:, :])  # Predict based on current weights
            errors = Y - predictions  # Calculate error
            
            # Update weights based on the error and learning rate
            for i in range(X.shape[1]):
                self.weights += alpha * np.outer(errors[:, i], X[:, i])

    def calculate_percent_error(self, X, Y):
        """
        Calculate percent error of predictions
        :param X: Array of input [input_dimensions, n_samples]
        :param Y: Array of desired (target) outputs [number_of_classes, n_samples]
        :return: Percent error
        """
        predictions = self.predict(X)
        number_of_errors = np.sum(np.any(predictions != Y, axis=0))
        percent_error = (number_of_errors / X.shape[1]) * 100
        return percent_error

# Main program
if __name__ == "__main__":
    input_dimensions = 2
    number_of_classes = 2

    model = Perceptron(input_dimensions=input_dimensions, number_of_classes=number_of_classes, seed=1)
    
    # Training data
    X_train = np.array([[-1.43815556, 0.10089809, -1.25432937, 1.48410426],
                        [-1.81784194, 0.42935033, -1.2806198, 0.06527391]])
    Y_train = np.array([[1, 0, 0, 1], [0, 1, 1, 0]])
    
    # Initial predictions
    print("Initial predictions:", model.predict(X_train))
    
    # Initialize weights to zero and display initial weights
    model.initialize_all_weights_to_zeros()
    print("Initial weights:\n", model.print_weights())
    
    # Train the model and display percent error over epochs
    percent_error = []
    for k in range(20):
        model.train(X_train, Y_train, num_epochs=1, alpha=0.0001)
        percent_error.append(model.calculate_percent_error(X_train, Y_train))
    
    # Display percent error and final weights
    print("Percent error over epochs:", percent_error)
    print("Final weights:\n", model.print_weights())
