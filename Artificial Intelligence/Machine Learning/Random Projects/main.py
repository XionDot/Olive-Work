from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Seed the random Num gen, so it gens same Nums every time prog runs. #
        random.seed(1)

        # Model single neuron, 3 input connections & 1 output connection. #
        # Assign rand weights to a | 3 x 1 | matrix, with values in the 
        # range -1 to 1  and mean 0. #
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    # Sigmoid Func, describes S shaped curve (sigmoid). #
    # Pass weighted sum of inputs through this function
    # to normalize them between 0 & 1. #

    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid Func. #
    # < Gradient of the Sigmoid curve. > #
    # It indicates how confident the existing weight is. #
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Train the NN ( Neural Network ) through a process of trial and error. #
    # Adjusting the synaptic weights each time. #
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # Pass the training set through our neural network (singal neuron). #
            output = self.think(training_set_inputs)

            # Calculate error ( Difference between the desired output 
            # & predicted output ). #
            error = training_set_outputs - output

            # Multiply error by input and again by the gradient of Sigmoid curve. #
            # Meaning less confident weights are adjusted more. #
            # Meaning inputs, which = 0, do not cause changes to weights. #
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # Adjust weights. #
            self.synaptic_weights += adjustment

    # Neural Network thinks. #
    def think(self, inputs):
        # Pass inputs through our NN ( The single neuron ). #
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":
    # Intialise a single NNN ( Neuron Neural Network ). #
    neural_network = NeuralNetwork()
    print "Random Starting Synaptic Weights: "
    print "|#|#|#|*|#|#|#|"
    print neural_network.synaptic_weights
    print "|#|#|#|*|#|#|#|"
    
    # Training Set. #
    # There are 4 examples, each consisting of 3 input values 
    # & 1 output value. #
    training_set_inputs = array( [[0, 0, 1], 
                                  [1, 1, 1],
                                  [1, 0, 1],
                                  [0, 1, 1]] )

    training_set_outputs = array( [[0, 1, 1, 0]] ).T

    # Train NN using training set. #
    # Train 10,000 times & make small adjustments each time. #
    neural_network.train(training_set_inputs, training_set_outputs, 100000)
    print "New synaptic weights after training: "
    print "|#|#|#|*|#|#|#|"
    print neural_network.synaptic_weights
    print "|#|#|#|*|#|#|#|"

    # Test NN with new situation. #
    print "Considering new situation [1, 0, 0] -> ?: "
    print "|#|#|#|*|#|#|#|"
    print neural_network.think(array([1, 0, 0]))
    print "|#|#|#|*|#|#|#|"
