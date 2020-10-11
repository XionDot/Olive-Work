#import tensorflow as tf

#weights = tf.Variable([tf.random.normal()])

#while True: # loop forever
#    with tf.GradientTape() as g:
 #       loss = compute_loss(weights)
  #      gradient = g.gradient(loss, weights)

   # weights = weights - lr * gradient

###################################################################################################
#########################################Gradient Descent##########################################

import tensorflow as tf

model = tf.keras.Sequential([...])

# pick favourite optimizer
optimizer = tf.keras.optimizer.SGD()

while True: #loop forever

    # forward pass through the network
    prediction = model(x)

    with tf.GradientTape() as tape:
        # compute the loss
        loss = compute_loss(y, prediction)

    # update the weights using the gradient
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

