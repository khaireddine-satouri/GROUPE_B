import tensorflow as tf

# Define model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(6,)),
    tf.keras.layers.Dense(1)
])

# Compile model
model.compile(loss='mse', optimizer='adam')

# Train model (example)
x_train = [[1, 2 , 3 , 4 , 6 ,7], [1, 2 , 3 , 4 , 6 ,7], [1, 2 , 3 , 4 , 6 ,7], [1, 2 , 3 , 4 , 6 ,7], [1, 2 , 3 , 4 , 6 ,7]]
y_train = [5, 7, 9, 11, 13]
model.fit(x_train, y_train, epochs=100)

# Predict using trained model
x_test = [[11, 12 , 13 , 14 , 16 ,17], [11, 14 , 16 , 14 , 16 ,18], [19, 20 , 21 , 22 , 23 ,24]]
y_pred = model.predict(x_test)
print("Predictions: \n", y_pred)

# Save model to file
model.save('model5')