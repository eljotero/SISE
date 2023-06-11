import sys
import neural_network as nn
import os
import glob as gl


def main():
    args = sys.argv[1:]

    if len(args) != 1:

        # TODO: Add argument for type of neural network // Base: Multi-layer perceptron // But not obligatory

        ### Reading path to data file, that is folder with F8 and F10 folders from CMD.
        path_to_data = args[0]

        ### Reading number of hidden layers, specified by the user in CMD when running the program.
        number_of_hidden_layers = int(args[1])

        ### Limit of hidden layers is equal to 3 (TODO: Change this limit in the future (IF POSSIBLE))
        if number_of_hidden_layers > 3:
            number_of_hidden_layers = 3

        ### Reading number of neurons in each layer (specified by the user).
        list_of_neuron_numbers = []
        for i in range(0, number_of_hidden_layers):
            list_of_neuron_numbers.append(int(args[i + 2]))

        ### TODO: Add maximum number of neurons in each layer (for batch testing purposes).

        ### Printing entered data

        # print("Path to data: " + path_to_data)
        # print("Number of hidden layers: " + str(number_of_hidden_layers))
        # for i in range(0, number_of_hidden_layers):
        #     print("Number of neurons in " + str(i + 1) + " hidden layer: " + str(list_of_neuron_numbers[i]))

        ### Creating network

        # neural_network = nn.NeuralNetwork(number_of_hidden_layers, list_of_neuron_numbers, 2)
        # print(neural_network)

        data_f8 = path_to_data + "\F8"
        data_f10 = path_to_data + "\F10"

        list_of_files_f8 = gl.glob(data_f8 + "\*stat*")
        list_of_files_f10 = gl.glob(data_f10 + "\*stat*")

        # Learning loop

        for file in list_of_files_f8:
            print("")

    else:
        neural_network_file = args[0]
        print("Path to selected neural network file: " + neural_network_file)


if __name__ == "__main__":
    main()