# -*- coding: utf-8 -*-
"""Mantap-Mantap Arif.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oftA1LgRhx0nWBOYd5rbUwDnkOkonZXf
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

model2 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1500, activation='relu', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model3 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(150, activation='relu', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model1.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model2.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model3.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model1.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2)
model1.evaluate(X_train, y_train, verbose=2)
model1.evaluate(X_test, y_test, verbose=2)
model1.evaluate(scaler.transform(X), y, verbose=2)

model2.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2)
model2.evaluate(X_train, y_train, verbose=2)
model2.evaluate(X_test, y_test, verbose=2)
model2.evaluate(scaler.transform(X), y, verbose=2)

model3.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2)
model3.evaluate(X_train, y_train, verbose=2)
model3.evaluate(X_test, y_test, verbose=2)
model3.evaluate(scaler.transform(X), y, verbose=2)

print(model1.history.history.keys())
print(model2.history.history.keys())
print(model3.history.history.keys())

plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.plot(model1.history.history['acc'], label='SLP accuracy')
#plt.plot(model1.history.history['val_acc'], label='SLP val_accuracy', ls="--")
plt.plot(model2.history.history['acc'], label='MLP accuracy')
#plt.plot(model2.history.history['val_acc'], label='MLP val_accuracy', ls="--")
plt.plot(model3.history.history['acc'], label='MLP* accuracy')
#plt.plot(model3.history.history['val_acc'], label='MLP* val_accuracy', ls="--")
plt.legend()
plt.show()

plt.ylabel("Val Accuracy")
plt.xlabel("Epoch")
#plt.plot(model1.history.history['acc'], label='SLP accuracy')
plt.plot(model1.history.history['val_acc'], label='SLP val_accuracy')
#plt.plot(model2.history.history['acc'], label='MLP accuracy')
plt.plot(model2.history.history['val_acc'], label='MLP val_accuracy')
#plt.plot(model3.history.history['acc'], label='MLP* accuracy')
plt.plot(model3.history.history['val_acc'], label='MLP* val_accuracy')
plt.legend()
plt.show()




plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.plot(model1.history.history['loss'], label='SLP loss')
#plt.plot(model1.history.history['val_loss'], label='SLP val_loss')
plt.plot(model2.history.history['loss'], label='MLP loss')
#plt.plot(model2.history.history['val_loss'], label='MLP val_loss')
plt.plot(model3.history.history['loss'], label='MLP* loss')
#plt.plot(model3.history.history['val_loss'], label='MLP* val_loss',)
plt.legend()
plt.show()

plt.ylabel("Val Loss")
plt.xlabel("Epoch")
#plt.plot(model1.history.history['loss'], label='SLP loss')
plt.plot(model1.history.history['val_loss'], label='SLP val_loss')
#plt.plot(model2.history.history['loss'], label='MLP loss')
plt.plot(model2.history.history['val_loss'], label='MLP val_loss')
#plt.plot(model3.history.history['loss'], label='MLP* loss')
plt.plot(model3.history.history['val_loss'], label='MLP* val_loss',)
plt.legend()
plt.show()

model4 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1500, activation='tanh', input_shape=(16,)),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model5 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1500, activation='tanh', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model6 = tf.keras.models.Sequential([
    tf.keras.layers.Dense(150, activation='tanh', input_shape=(16,)),
    tf.keras.layers.Dense(1500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(500, kernel_regularizer=tf.keras.regularizers.l2(0.001), activation='tanh'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation='softmax'),
])

model4.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model5.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model6.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model4.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2)
model4.evaluate(X_train, y_train, verbose=2)
model4.evaluate(X_test, y_test, verbose=2)
model4.evaluate(scaler.transform(X), y, verbose=2)

model5.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2)
model5.evaluate(X_train, y_train, verbose=2)
model5.evaluate(X_test, y_test, verbose=2)
model5.evaluate(scaler.transform(X), y, verbose=2)

model6.fit(X_train, y_train, epochs=100, batch_size=25, verbose=1, validation_split=0.2)
model6.evaluate(X_train, y_train, verbose=2)
model6.evaluate(X_test, y_test, verbose=2)
model6.evaluate(scaler.transform(X), y, verbose=2)

print(model1.history.history.keys())
print(model2.history.history.keys())
print(model3.history.history.keys())

plt.ylabel("Accuracy")
plt.xlabel("Epoch")
plt.plot(model4.history.history['acc'], label='SLP accuracy')
#plt.plot(model4.history.history['val_acc'], label='SLP val_accuracy', ls="--")
plt.plot(model5.history.history['acc'], label='MLP accuracy')
#plt.plot(model5.history.history['val_acc'], label='MLP val_accuracy', ls="--")
plt.plot(model6.history.history['acc'], label='MLP* accuracy')
#plt.plot(model6.history.history['val_acc'], label='MLP* val_accuracy', ls="--")
plt.legend()
plt.show()

plt.ylabel("Val Accuracy")
plt.xlabel("Epoch")
#plt.plot(model4.history.history['acc'], label='SLP accuracy')
plt.plot(model4.history.history['val_acc'], label='SLP val_accuracy')
#plt.plot(model5.history.history['acc'], label='MLP accuracy')
plt.plot(model5.history.history['val_acc'], label='MLP val_accuracy')
#plt.plot(model6.history.history['acc'], label='MLP* accuracy')
plt.plot(model6.history.history['val_acc'], label='MLP* val_accuracy')
plt.legend()
plt.show()




plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.plot(model4.history.history['loss'], label='SLP loss')
#plt.plot(model4.history.history['val_loss'], label='SLP val_loss')
plt.plot(model5.history.history['loss'], label='MLP loss')
#plt.plot(model5.history.history['val_loss'], label='MLP val_loss')
plt.plot(model6.history.history['loss'], label='MLP* loss')
#plt.plot(model6.history.history['val_loss'], label='MLP* val_loss',)
plt.legend()
plt.show()

plt.ylabel("Val Loss")
plt.xlabel("Epoch")
#plt.plot(model4.history.history['loss'], label='SLP loss')
plt.plot(model4.history.history['val_loss'], label='SLP val_loss')
#plt.plot(model5.history.history['loss'], label='MLP loss')
plt.plot(model5.history.history['val_loss'], label='MLP val_loss')
#plt.plot(model6.history.history['loss'], label='MLP* loss')
plt.plot(model6.history.history['val_loss'], label='MLP* val_loss',)
plt.legend()
plt.show()

