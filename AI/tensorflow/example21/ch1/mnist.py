import tensorflow as tf

input_data = open('.\AI\\tensorflow\\example21\\ch1\\t10k-images.idx3-ubyte', 'r')

mnist = input_data.read_data_sets("MNIST_data1/", one_hot=True)
