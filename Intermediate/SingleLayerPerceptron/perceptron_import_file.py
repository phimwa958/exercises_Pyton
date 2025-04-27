import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

class Perceptron(object):
    def __init__(self, input_dimensions=4, number_of_classes=3, seed=None):
        if seed is not None:
            np.random.seed(seed)
        self.input_dimensions = input_dimensions
        self.number_of_classes = number_of_classes
        self._initialize_weights()

    def _initialize_weights(self):
        self.weights = np.random.randn(self.number_of_classes, self.input_dimensions + 1)

    def initialize_all_weights_to_zeros(self):
        self.weights = np.zeros((self.number_of_classes, self.input_dimensions + 1))

    def predict(self, X):
        temp = np.ones((1, X.shape[1]))  # Add bias term
        X = np.r_[temp, X]
        activation = np.dot(self.weights, X)
        activation = 1 / (1 + np.exp(-activation))  # Sigmoid activation function
        return (activation > 0.5).astype(int)  # Threshold to binary 0/1

    def print_weights(self):
        return self.weights

    def train(self, X, Y, num_epochs=50, alpha=0.001):
        temp = np.ones((1, X.shape[1]))
        X = np.r_[temp, X]
        
        for epoch in range(num_epochs):
            predictions = self.predict(X[1:, :])  # Predict based on current weights
            errors = Y - predictions  # Calculate error
            
            for i in range(X.shape[1]):
                self.weights += alpha * np.outer(errors[:, i], X[:, i])

    def calculate_percent_error(self, X, Y):
        predictions = self.predict(X)
        number_of_errors = np.sum(np.any(predictions != Y, axis=0))
        percent_error = (number_of_errors / X.shape[1]) * 100
        return percent_error

# Load data
def load_iris_data(file_path):
    data = np.genfromtxt(file_path, delimiter=',', dtype=str)
    X = data[:, :-1].astype(float)  # Features
    y = data[:, -1]  # Labels

    # Convert labels to numeric values
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    # Convert labels to one-hot encoding for multi-class Perceptron
    Y = np.zeros((len(y), len(set(y))))
    Y[np.arange(len(y)), y] = 1
    
    return X.T, Y.T  # Transpose for easier handling in Perceptron

# Main program
if __name__ == "__main__":
    # Load the dataset
    X, Y = load_iris_data('iris.data.txt')
    
    # Split the dataset into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X.T, Y.T, test_size=0.3, random_state=42)
    X_train, X_test, Y_train, Y_test = X_train.T, X_test.T, Y_train.T, Y_test.T

    # Initialize Perceptron model
    model = Perceptron(input_dimensions=4, number_of_classes=3, seed=1)
    model.initialize_all_weights_to_zeros()
    print("Initial weights:\n", model.print_weights())

    # Train the model and display percent error over epochs
    percent_error = []
    for epoch in range(50):  # Increased epochs
        model.train(X_train, Y_train, num_epochs=1, alpha=0.001)  # Reduced alpha
        percent_error.append(model.calculate_percent_error(X_test, Y_test))

    # Display percent error and final weights
    print("Percent error over epochs:", percent_error)
    print("Final weights:\n", model.print_weights())
