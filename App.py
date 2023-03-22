fait les tests d'intégration 4 tests d'acceptations (format BDD de se code) de cette application : "import toga
import tensorflow as tf
from sklearn.preprocessing import  StandardScaler
import numpy as np
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

"""
import os

print(os.getcwd())
"""


class App(toga.App):
    def startup(self):
        # Define the models
        self.models = {
            'model1': {
                'path': 'model1',
                'input_cols': ['a','b','c'],
                'num_inputs': 3,
                'info': "model1"
            },
            'model2': {
                'path': 'model1',
                'input_cols': ['a','b','c','d'],
                'num_inputs': 4,
                'info': "model2"
            },            
            'model3': {
                'path': 'model3',
                'input_cols': ['a','b','c','d','e'],
                'num_inputs': 5,
                'info': "model3"
            },            
            'model4': {
                'path': 'model4',
                'input_cols': ['a','b','c','d','e','f'],
                'num_inputs': 6,
                'info': "model4"
            }, 
            'model5': {
                'path': 'model3',
                'input_cols': ['a','b','c','d','e','f','g'],
                'num_inputs': 7,
                'info': "model5"
            }, 
        }

        # Create the main window
        self.main_window = toga.MainWindow(title=self.name)

        # Create the model selection dropdown
        model_names = list(self.models.keys())
        self.model_selection = toga.Selection(items=model_names, on_select=self.on_select_model)
        model_box = toga.Box(children=[toga.Label('Select a database :'), self.model_selection])

        # Add the components to the main window
        self.main_window.content = toga.Box(children=[model_box])
        self.main_window.show()

    def on_select_model(self, widget):
        # Get the selected model
        selected_model_name = self.model_selection.value
        selected_model = self.models[selected_model_name]

        # Load the selected model
        self.model = tf.keras.models.load_model(selected_model['path'], compile=False)

        # Create the input fields
        self.input_fields = []
        for i in range(selected_model['num_inputs']):
            input_field = toga.TextInput(placeholder=selected_model['input_cols'][i], style=Pack(padding=5, flex=1))
            self.input_fields.append(input_field)
            
        #Create the info label
        self.info_label = toga.Label(selected_model["info"])

        # Create the prediction button
        predict_button = toga.Button('Predict', on_press=self.on_predict)

        # Create the result label
        self.result_label = toga.Label('Result: ', style=Pack(color="red"))

        # Create the return button
        return_button = toga.Button('Return', on_press=self.on_return)

        # Add the components to the main window
        input_box = toga.Box(children=self.input_fields)
        buttons_box = toga.Box(children=[predict_button, return_button])
        box = toga.Box(children=[self.info_label, input_box, buttons_box, self.result_label], style=Pack(direction=COLUMN))
        self.main_window.content = box

    def on_predict(self, widget):
            # Get the input values
        input_values = []
        for input_field in self.input_fields:
            input_values.append(float(input_field.value))

        # Reshape the input values to match the model's input shape
        input_values = tf.reshape(input_values, [1, len(self.input_fields)])

        # Make the prediction
        prediction = self.model.predict(input_values)[0][0]

        # Update the result label
        self.result_label.text = f"Result: {str(prediction)}"
        self.result_label.refresh()
        
        # Reshape the input values to match the model's input shape
        input_values = tf.reshape(input_values, [1, len(self.input_fields)])

        # Make the prediction
        prediction = self.model.predict(input_values)[0][0]

        # Update the result label
        self.result_label.text = f"Result: {str(prediction)}"
        self.result_label.refresh()
    def on_return(self, widget):
        # Reset the main window to the initial state
        model_names = list(self.models.keys())
        self.model_selection = toga.Selection(items=model_names, on_select=self.on_select_model)
        model_box = toga.Box(children=[toga.Label('Select a database :'), self.model_selection])
        self.main_window.content = toga.Box(children=[model_box])
        self.result_label.text = 'Result: '

    def main(self):
        return self.main_window


def main():
    return App('Model Predictor', 'org.example.modelpredictor').main_loop()


if __name__ == '__main__':
    main()
"
