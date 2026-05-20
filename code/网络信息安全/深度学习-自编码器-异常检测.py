import numpy as np  
import tensorflow as tf  
from tensorflow.keras.layers import Input, Dense  
from tensorflow.keras.models import Model  
import matplotlib.pyplot as plt  
  
# 假设我们有一些二维数据，其中一些是异常的  
np.random.seed(0)  
X_normal = np.random.normal(size=(1000, 2))  
X_outliers = np.random.uniform(low=-5, high=5, size=(100, 2))  # 异常点  
X = np.r_[X_normal + 2 * np.random.normal(size=(1000, 2)), X_outliers]  # 添加一些噪声到正常数据  
  
# 定义自编码器模型  
input_img = Input(shape=(2,))  
encoded = Dense(1, activation='relu')(input_img)  
decoded = Dense(2, activation='linear')(encoded)  
autoencoder = Model(input_img, decoded)  
  
# 编译模型  
autoencoder.compile(optimizer='adam', loss='mean_squared_error')  
  
# 训练模型  
autoencoder.fit(X, X, epochs=50, batch_size=256, shuffle=True, validation_data=(X, X))  
  
# 使用模型进行预测并计算重建误差  
X_pred = autoencoder.predict(X)  
mse = np.mean(np.power(X - X_pred, 2), axis=1)  
error_df = pd.DataFrame({'reconstruction_error': mse, 'is_outlier': [0 if x < 0.05 else 1 for x in mse]})  
  
# 绘制结果  
plt.figure(figsize=(10, 5))  
plt.scatter(X[:, 0], X[:, 1], c=error_df['is_outlier'], cmap='viridis', alpha=0.7,  
            label='data points (color: outlier status)')  
plt.title("Anomaly Detection with Autoencoder")  
plt.xlabel("feature 1")  
plt.ylabel("feature 2")  
plt.legend()  
plt.show()
