import pytest

@pytest.mark.slow
def test_my_model():
    #code de test

    loaded_model = tf.keras.models.load_model('model1')

        # Charger les données de test
    x_test = [[1, 2], [7,8], [11,12], [15,16], [19,20]]
    y_test = [5, 7, 9, 11, 13]

        # Faire des prédictions sur les données de test
    y_pred = loaded_model.predict(x_test)

    # Afficher les résultats
print('Predictions:', y_pred)
test_my_model()