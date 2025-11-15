import pandas as pd
import matplotlib.pyplot as plt

# データフレームを読み込む
df = pd.read_csv('./csv/RGBCMYK.csv')

# RGB値を0-1の範囲に正規化（色として使用）
colors = df[['R', 'G', 'B']].values / 255.0

# パーセント変換
C_percent = (df['C'] / 255.0) * 100
M_percent = (df['M'] / 255.0) * 100
Y_percent = (df['Y'] / 255.0) * 100
K_percent = (df['K'] / 255.0) * 100
MC_percent = M_percent + C_percent
MK_percent = M_percent + K_percent
YMC_percent = Y_percent + M_percent + C_percent
YMCK_percent = Y_percent + M_percent + C_percent + K_percent

# 4行3列のサブプロット（サイズを半分に）
fig, axes = plt.subplots(4, 3, figsize=(9, 8))

# 1行目: Y vs M, Y vs C, Y vs K
axes[0, 0].scatter(Y_percent, M_percent, c=colors, s=50, edgecolors='black')
axes[0, 0].set_xlabel('Y [%]', fontsize=10)
axes[0, 0].set_ylabel('M [%]', fontsize=10)
axes[0, 0].set_title('Y vs M', fontsize=11)
axes[0, 0].set_xlim(0, 100)
axes[0, 0].set_ylim(0, 100)
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(Y_percent, C_percent, c=colors, s=50, edgecolors='black')
axes[0, 1].set_xlabel('Y [%]', fontsize=10)
axes[0, 1].set_ylabel('C [%]', fontsize=10)
axes[0, 1].set_title('Y vs C', fontsize=11)
axes[0, 1].set_xlim(0, 100)
axes[0, 1].set_ylim(0, 100)
axes[0, 1].grid(True, alpha=0.3)

axes[0, 2].scatter(Y_percent, K_percent, c=colors, s=50, edgecolors='black')
axes[0, 2].set_xlabel('Y [%]', fontsize=10)
axes[0, 2].set_ylabel('K [%]', fontsize=10)
axes[0, 2].set_title('Y vs K', fontsize=11)
axes[0, 2].set_xlim(0, 100)
axes[0, 2].set_ylim(0, 100)
axes[0, 2].grid(True, alpha=0.3)

# 2行目: Y vs M+C, Y vs M+K
axes[1, 0].scatter(Y_percent, MC_percent, c=colors, s=50, edgecolors='black')
axes[1, 0].set_xlabel('Y [%]', fontsize=10)
axes[1, 0].set_ylabel('M+C [%]', fontsize=10)
axes[1, 0].set_title('Y vs M+C', fontsize=11)
axes[1, 0].set_xlim(0, 100)
axes[1, 0].set_ylim(0, 200)
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].scatter(Y_percent, MK_percent, c=colors, s=50, edgecolors='black')
axes[1, 1].set_xlabel('Y [%]', fontsize=10)
axes[1, 1].set_ylabel('M+K [%]', fontsize=10)
axes[1, 1].set_title('Y vs M+K', fontsize=11)
axes[1, 1].set_xlim(0, 100)
axes[1, 1].set_ylim(0, 200)
axes[1, 1].grid(True, alpha=0.3)

# 2行目右を非表示
axes[1, 2].axis('off')

# 3行目: Y vs Y+M+C
axes[2, 0].scatter(Y_percent, YMC_percent, c=colors, s=50, edgecolors='black')
axes[2, 0].set_xlabel('Y [%]', fontsize=10)
axes[2, 0].set_ylabel('Y+M+C [%]', fontsize=10)
axes[2, 0].set_title('Y vs Y+M+C', fontsize=11)
axes[2, 0].set_xlim(0, 100)
axes[2, 0].set_ylim(0, 300)
axes[2, 0].grid(True, alpha=0.3)

# 3行目の残りを非表示
axes[2, 1].axis('off')
axes[2, 2].axis('off')

# 4行目: Y+M+C+Kのヒストグラム
axes[3, 0].hist(YMCK_percent, bins=30, color='gray', edgecolor='black', alpha=0.7)
axes[3, 0].set_xlabel('Y+M+C+K [%]', fontsize=10)
axes[3, 0].set_ylabel('Frequency', fontsize=10)
axes[3, 0].set_title('Histogram of Y+M+C+K', fontsize=11)
axes[3, 0].grid(True, alpha=0.3)

# 4行目の残りを非表示
axes[3, 1].axis('off')
axes[3, 2].axis('off')

plt.tight_layout()
plt.show()