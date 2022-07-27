import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Bidirectional, Dropout
from tensorflow.keras.utils import to_categorical
import numpy as np
import pickle
from sklearn import preprocessing
from sklearn.utils import shuffle


def augment(image_label):
    image = image_label
    thr = tf.random.uniform([1])/4
    sign = tf.random.uniform([1], maxval = 2, dtype=tf.dtypes.int32)*2-1
    image = image + tf.cast(sign, dtype=tf.dtypes.float32, name=None)*thr

    shift = tf.random.uniform(shape=[1], minval=-5, maxval=5, dtype=tf.int32)
    image = tf.roll(image, shift=shift, axis=[0])

    return image

def train_process(new_label:str, new_keypoints:list):

    le = preprocessing.LabelEncoder()

    with open('mediapipe/keypoints.pkl', 'rb') as f:
        keypoints = pickle.load(f)

    with open('mediapipe/labels.pkl', 'rb') as f:
        labels = pickle.load(f)

    keypoints.append(new_keypoints)
    labels.append(new_label)

    le.fit(labels)
    labels_num = le.transform(labels)
    y = to_categorical(labels_num).astype(int)

    keypoints_pad = tf.keras.preprocessing.sequence.pad_sequences(keypoints, maxlen=30, dtype='float32',)

    X_train, y_train = shuffle(keypoints_pad, y, random_state=0)

    batch_size = 128

    tf_train_data = tf.data.Dataset.from_tensor_slices((np.array([X_train]) ,
                                                        np.array([y_train]))).shuffle(batch_size, 
                                                                                    reshuffle_each_iteration=True)

    tf_train_data = (tf_train_data.shuffle(batch_size * 100)
        .map(lambda x, y: (augment(x), y),
        num_parallel_calls=tf.data.AUTOTUNE)
        .prefetch(tf.data.AUTOTUNE))

    model = Sequential()
    model.add(Bidirectional(LSTM(30, return_sequences=True, activation='relu', input_shape=(None,126))))
    model.add(LSTM(30, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(le.classes_.shape[0], activation='softmax'))

    model.fit(tf_train_data, epochs=400, batch_size=batch_size)
    model.save("mediapipe/train_tl")

    with open('mediapipe/labels.pkl', 'wb') as f:
        pickle.dump(labels, f)

    with open('mediapipe/keypoints.pkl', 'wb') as f:
        pickle.dump(keypoints, f)