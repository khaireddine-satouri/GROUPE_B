import tensorflow as tf

# Define model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(loss='mse', optimizer='adam')

# Train model (example)
x_train = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y_train = [5, 7, 9, 11, 13]
model.fit(x_train, y_train, epochs=100)

# Predict using trained model
x_test = [[11, 12], [13, 14], [15, 16]]
y_pred = model.predict(x_test)
print("Predictions: \n", y_pred)

# Save model to file
model.save('model1')
