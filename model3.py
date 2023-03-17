import tensorflow as tf

# Define model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(loss='mse', optimizer='adam')

# Train model (example)
x_train = [[1, 2, 5 ,4], [3, 4, 1, 8], [5, 6, 2, 4], [7, 8, 7, 2]]
y_train = [5, 7, 9, 11]
model.fit(x_train, y_train, epochs=100)

# Predict using trained model
x_test = [[11, 12, 15, 14], [13, 14, 10, 12], [15, 16, 11, 10], [14, 21, 17, 12]]
y_pred = model.predict(x_test)
print("Predictions: \n", y_pred)

# Save model to file
model.save('model3')
