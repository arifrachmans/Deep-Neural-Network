# -*- coding: utf-8 -*-
"""Running 100x.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ndqr3UJ0dtQZ9Ki3EyQRSQLb69RaoVGt
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import time
import os
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mean-value-c2.csv')
dataset = df.values
X = dataset[:,0:16].astype(float)
y = dataset[:,16:19]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model1 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1500, activation='relu', input_shape=(16,)),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model1.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

acctrain, acctes, accsemua = [], [], []

for i in range(100):
  logmodel1 = tf.keras.callbacks.CSVLogger(f'model1{i}_log.csv', append=True, separator=',')
  model1.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2, callbacks=[logmodel1])
  A = model1.evaluate(X_train, y_train, verbose=2)[1]
  B = model1.evaluate(X_test, y_test, verbose=2)[1]
  C = model1.evaluate(scaler.transform(X), y, verbose=2)[1]
  model1.save(f'model1{i}.h5')
  acctrain.append(A)
  acctes.append(B)
  accsemua.append(C)

hasil = {
    'Train': acctrain,
    'Test': acctes,
    'Semua': accsemua,
}

hasil = pd.DataFrame(hasil)
hasil.to_csv('hasil_model_1.csv')



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import time
import os
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mean-value-c2.csv')
dataset = df.values
X = dataset[:,0:16].astype(float)
y = dataset[:,16:19]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model2 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1500, activation='relu', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model2.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

acctrain, acctes, accsemua = [], [], []

for i in range(100):
  logmodel2 = tf.keras.callbacks.CSVLogger(f'model2{i}_log.csv', append=True, separator=',')
  model2.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2, callbacks=[logmodel2])
  A = model2.evaluate(X_train, y_train, verbose=2)[1]
  B = model2.evaluate(X_test, y_test, verbose=2)[1]
  C = model2.evaluate(scaler.transform(X), y, verbose=2)[1]
  model2.save(f'model2{i}.h5')
  acctrain.append(A)
  acctes.append(B)
  accsemua.append(C)

hasil = {
    'Train': acctrain,
    'Test': acctes,
    'Semua': accsemua,
}

hasil = pd.DataFrame(hasil)
hasil.to_csv('hasil_model_2.csv')



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import time
import os
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mean-value-c2.csv')
dataset = df.values
X = dataset[:,0:16].astype(float)
y = dataset[:,16:19]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model3 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(150, activation='relu', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model3.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

acctrain, acctes, accsemua = [], [], []

for i in range(100):
  logmodel3 = tf.keras.callbacks.CSVLogger(f'model3{i}_log.csv', append=True, separator=',')
  model3.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2, callbacks=[logmodel3])
  A = model3.evaluate(X_train, y_train, verbose=2)[1]
  B = model3.evaluate(X_test, y_test, verbose=2)[1]
  C = model3.evaluate(scaler.transform(X), y, verbose=2)[1]
  model3.save(f'model3{i}.h5')
  acctrain.append(A)
  acctes.append(B)
  accsemua.append(C)

hasil = {
    'Train': acctrain,
    'Test': acctes,
    'Semua': accsemua,
}

hasil = pd.DataFrame(hasil)
hasil.to_csv('hasil_model_3.csv')



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import time
import os
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mean-value-c2.csv')
dataset = df.values
X = dataset[:,0:16].astype(float)
y = dataset[:,16:19]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model4 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1500, activation='tanh', input_shape=(16,)),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model4.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

acctrain, acctes, accsemua = [], [], []

for i in range(100):
  logmodel4 = tf.keras.callbacks.CSVLogger(f'model4{i}_log.csv', append=True, separator=',')
  model1.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2, callbacks=[logmodel4])
  A = model4.evaluate(X_train, y_train, verbose=2)[1]
  B = model4.evaluate(X_test, y_test, verbose=2)[1]
  C = model4.evaluate(scaler.transform(X), y, verbose=2)[1]
  model4.save(f'model4{i}.h5')
  acctrain.append(A)
  acctes.append(B)
  accsemua.append(C)

hasil = {
    'Train': acctrain,
    'Test': acctes,
    'Semua': accsemua,
}

hasil = pd.DataFrame(hasil)
hasil.to_csv('hasil_model_4.csv')



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import time
import os
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mean-value-c2.csv')
dataset = df.values
X = dataset[:,0:16].astype(float)
y = dataset[:,16:19]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model5 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1500, activation='tanh', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model5.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

acctrain, acctes, accsemua = [], [], []

for i in range(100):
  logmodel5 = tf.keras.callbacks.CSVLogger(f'model5{i}_log.csv', append=True, separator=',')
  model5.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2, callbacks=[logmodel5])
  A = model5.evaluate(X_train, y_train, verbose=2)[1]
  B = model5.evaluate(X_test, y_test, verbose=2)[1]
  C = model5.evaluate(scaler.transform(X), y, verbose=2)[1]
  model5.save(f'model5{i}.h5')
  acctrain.append(A)
  acctes.append(B)
  accsemua.append(C)

hasil = {
    'Train': acctrain,
    'Test': acctes,
    'Semua': accsemua,
}

hasil = pd.DataFrame(hasil)
hasil.to_csv('hasil_model_5.csv')



import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import time
import os
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('mean-value-c2.csv')
dataset = df.values
X = dataset[:,0:16].astype(float)
y = dataset[:,16:19]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.2, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model6 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(150, activation='tanh', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])
model6.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

acctrain, acctes, accsemua = [], [], []

for i in range(100):
  logmodel6 = tf.keras.callbacks.CSVLogger(f'model6{i}_log.csv', append=True, separator=',')
  model1.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2, callbacks=[logmodel6])
  A = model6.evaluate(X_train, y_train, verbose=2)[1]
  B = model6.evaluate(X_test, y_test, verbose=2)[1]
  C = model6.evaluate(scaler.transform(X), y, verbose=2)[1]
  model6.save(f'model6{i}.h5')
  acctrain.append(A)
  acctes.append(B)
  accsemua.append(C)

hasil = {
    'Train': acctrain,
    'Test': acctes,
    'Semua': accsemua,
}

hasil = pd.DataFrame(hasil)
hasil.to_csv('hasil_model_6.csv')