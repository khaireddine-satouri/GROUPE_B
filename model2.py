import tensorflow as tf

# Define model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(loss='mse', optimizer='adam')

# Train model (example)
x_train = [[88, 17, 15], [13, 14, 1800], [1777, 178455 , 65], [7, 815,1], [7709, 4510, 456]]
y_train = [5, 7, 9, 11, 13]
model.fit(x_train, y_train, epochs=100)

# Predict using trained model
x_test = [[11, 12, 487], [13, 14, 44], [15, 16, 1744]]
y_pred = model.predict(x_test)
print("Predictions: \n", y_pred)

# Save model to file
model.save('model2')