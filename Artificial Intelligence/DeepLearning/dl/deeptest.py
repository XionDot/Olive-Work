import tensorflow as tf

## Make dense layer from scratch ##

class myDenseLayer(tf.keras.layers.Layer):
    def __init__(self, input_dim, output_dim):
        super(myDenseLayer, self).__init__()
        
        input_dim = ([4, 5])

        # Initialize weights & bias
        self.W = self.add_weight([input_dim, output_dim])
        self.b = self.add_weight([1, output_dim])

    def call(self, inputs):
        # Forward propagate the inputs
        z = tf.matmul(inputs, self.W) + self.b

        # Feed through a non-linear activation
        output = tf.math.sigmoid(z)

        return output
        print(output)
## Dense Layer Generated using tensorflow ##
## import tensorflow as tf ##
## layer = tf.keras.layers.Dense( units = 2 ) ##

