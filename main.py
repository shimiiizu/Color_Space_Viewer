import pandas as pd
import matplotlib.pyplot as plt

# データフレームを読み込む
df = pd.read_csv('./csv/RGBCMYK.csv')

# RGB値を0-1の範囲に正規化（色として使用）
colors = df[['R', 'G', 'B']].values / 255.0

# CMYK値をパーセント表示に変換
df['C_percent'] = (df['C'] / 255.0) * 100
df['M_percent'] = (df['M'] / 255.0) * 100
df['Y_percent'] = (df['Y'] / 255.0) * 100

# 3つのサブプロットを作成
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# YM グラフ
axes[0].scatter(df['Y_percent'], df['M_percent'], c=colors, s=100, edgecolors='black')
axes[0].set_xlabel('Y (Yellow) [%]', fontsize=12)
axes[0].set_ylabel('M (Magenta) [%]', fontsize=12)
axes[0].set_title('Y-M Plane', fontsize=14)
axes[0].set_xlim(0, 100)
axes[0].set_ylim(0, 100)
axes[0].grid(True, alpha=0.3)

# MC グラフ
axes[1].scatter(df['M_percent'], df['C_percent'], c=colors, s=100, edgecolors='black')
axes[1].set_xlabel('M (Magenta) [%]', fontsize=12)
axes[1].set_ylabel('C (Cyan) [%]', fontsize=12)
axes[1].set_title('M-C Plane', fontsize=14)
axes[1].set_xlim(0, 100)
axes[1].set_ylim(0, 100)
axes[1].grid(True, alpha=0.3)

# YC グラフ
axes[2].scatter(df['Y_percent'], df['C_percent'], c=colors, s=100, edgecolors='black')
axes[2].set_xlabel('Y (Yellow) [%]', fontsize=12)
axes[2].set_ylabel('C (Cyan) [%]', fontsize=12)
axes[2].set_title('Y-C Plane', fontsize=14)
axes[2].set_xlim(0, 100)
axes[2].set_ylim(0, 100)
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()