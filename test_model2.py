import tensorflow as tf
import pytest

@pytest.mark.slow
def test_my_model():
    # Votre code de test ici

    loaded_model = tf.keras.models.load_model('model2')

    # Charger les données de test
    x_test = [[88, 17, 15], [13, 14, 1800], [1777, 178455 , 65], [7, 815,1], [7709, 4510, 456]]
    y_test = [5, 7, 9, 11, 13]

    # Faire des prédictions sur les données de test
    y_pred = loaded_model.predict(x_test)

    # Afficher les résultats
    print('Predictions:', y_pred)
test_my_model()