import numpy as np


class NeuralNetwork:
    number_of_layers = 0
    number_of_neurons_in_each_layer = []

    def __init__(self, number_of_hidden_layers, list_of_number_of_neurons, number_of_entry_neurons):
        self.number_of_layers = number_of_hidden_layers + 2
        self.number_of_neurons_in_each_layer.append(number_of_entry_neurons)
        for i in range(1, number_of_hidden_layers + 1):
            self.number_of_neurons_in_each_layer.append(list_of_number_of_neurons[i - 1])
        self.number_of_neurons_in_each_layer.append(2)

    def __str__(self):
        string_to_print = "Number of layers: " + str(self.number_of_layers) + '\n'
        for i in range(0, self.number_of_layers):
            string_to_print += "Number of neurons in " + str(i + 1) + ". layer: " + str(self.number_of_neurons_in_each_layer[i]) + '\n'
        return string_to_print