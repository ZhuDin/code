import numpy as np
import tensorflow as tf

import tensorflow_hub as hub
import tensorflow_datasets as tfds

print('Version: ', tf.__version__)
print('Eager mode: ', tf.executing_eagerly())
print('Hub version: ', hub.__version__)
print('GPU is', 'available' if tf.config.experimental.list_physical_devices('GPU') else 'Not Available')

train_data, validation_data, test_data = tfds.load(
    name='imdb_reviews',
    split=('train[:60%]', 'train[60:]', 'test'),
    as_supervised=True
)

train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
print(train_examples_batch)

