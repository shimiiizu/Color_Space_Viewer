import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# データフレームを読み込む
df = pd.read_csv('./csv/RGBCMYK.csv')

# RGB値を0-1の範囲に正規化（色として使用）
colors = df[['R', 'G', 'B']].values / 255.0

# 3Dグラフを作成
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# CMYの3次元散布図（RGB値で色付け）
ax.scatter(df['C'], df['M'], df['Y'], c=colors, marker='o', s=100, edgecolors='black')

# 軸ラベル
ax.set_xlabel('C (Cyan)', fontsize=12)
ax.set_ylabel('M (Magenta)', fontsize=12)
ax.set_zlabel('Y (Yellow)', fontsize=12)
ax.set_title('CMY Color Space', fontsize=14)

# 軸の範囲を設定
ax.set_xlim(0, 255)
ax.set_ylim(0, 255)
ax.set_zlim(0, 255)

plt.show()