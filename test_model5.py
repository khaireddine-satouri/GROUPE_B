import tensorflow as tf
import pytest

@pytest.mark.slow
def test_my_model():
    # Votre code de test ici

    loaded_model = tf.keras.models.load_model('model5')

    # Charger les données de test
    x_test = [[11, 12 , 13 , 14 , 16 ,17], [11, 14 , 16 , 14 , 16 ,18], [19, 20 , 21 , 22 , 23 ,24]]

    # Faire des prédictions sur les données de test
    y_pred = loaded_model.predict(x_test)

    # Afficher les résultats
    print('Predictions:', y_pred)
test_my_model()