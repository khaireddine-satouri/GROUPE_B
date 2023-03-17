import tensorflow as tf
import pytest

@pytest.mark.slow
def test_my_model():
    # Votre code de test ici

    loaded_model = tf.keras.models.load_model('model3')

    # Charger les données de test
    x_test = [[1, 2, 5 ,4], [3, 4, 1, 8], [5, 6, 2, 4], [7, 8, 7, 2]]
    y_test = [5, 7, 9, 11]

    # Faire des prédictions sur les données de test
    y_pred = loaded_model.predict(x_test)

    # Afficher les résultats
    print('Predictions:', y_pred)
test_my_model()
#test_model5.py 