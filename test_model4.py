import tensorflow as tf
import pytest

@pytest.mark.slow
def test_my_model():
    # Votre code de test ici

    loaded_model = tf.keras.models.load_model('model4')

    # Charger les données de test
    x_test = [[1, 2, 3, 4, 5], [3, 4, 5, 7, 9], [5, 6, 4, 1, 0], [7, 8, 9, 10, 11], [9, 10, 12, 4, 8]]
    
    # Faire des prédictions sur les données de test
    y_pred = loaded_model.predict(x_test)

    # Afficher les résultats
    print('Predictions:', y_pred)
test_my_model()