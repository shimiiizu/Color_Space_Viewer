import pandas as pd
import matplotlib.pyplot as plt

# ========== 設定 ==========
PLOT_SIZE = 3  # プロットサイズ（デフォルト: 3）

# データフレームを読み込む
df = pd.read_csv('./csv/RGBCMYK_step5.csv')

# RGB値を0-1の範囲に正規化（色として使用）
colors = df[['R', 'G', 'B']].values / 255.0

# パーセント変換
C_percent = (df['C'] / 255.0) * 100
M_percent = (df['M'] / 255.0) * 100
Y_percent = (df['Y'] / 255.0) * 100
K_percent = (df['K'] / 255.0) * 100

# 組み合わせ
MC_percent = M_percent + C_percent
MK_percent = M_percent + K_percent
YMC_percent = Y_percent + M_percent + C_percent
YMCK_percent = Y_percent + M_percent + C_percent + K_percent

YC_percent = Y_percent + C_percent
YK_percent = Y_percent + K_percent
CK_percent = C_percent + K_percent
MYC_percent = M_percent + Y_percent + C_percent
MYK_percent = M_percent + Y_percent + K_percent
CYK_percent = C_percent + Y_percent + K_percent

# ====================
# Yベースのグラフ
# ====================
fig1, axes1 = plt.subplots(4, 3, figsize=(13, 10))
fig1.suptitle('Y-based Graphs', fontsize=16, fontweight='bold')

# 1行目: Y vs M, Y vs C, Y vs K
axes1[0, 0].scatter(Y_percent, M_percent, c=colors, s=PLOT_SIZE)
axes1[0, 0].set_xlabel('Y [%]', fontsize=12)
axes1[0, 0].set_ylabel('M [%]', fontsize=12)
axes1[0, 0].set_title('Y vs M', fontsize=13)
axes1[0, 0].set_xlim(0, 100)
axes1[0, 0].set_ylim(0, 100)
axes1[0, 0].grid(True, alpha=0.3)

axes1[0, 1].scatter(Y_percent, C_percent, c=colors, s=PLOT_SIZE)
axes1[0, 1].set_xlabel('Y [%]', fontsize=12)
axes1[0, 1].set_ylabel('C [%]', fontsize=12)
axes1[0, 1].set_title('Y vs C', fontsize=13)
axes1[0, 1].set_xlim(0, 100)
axes1[0, 1].set_ylim(0, 100)
axes1[0, 1].grid(True, alpha=0.3)

axes1[0, 2].scatter(Y_percent, K_percent, c=colors, s=PLOT_SIZE)
axes1[0, 2].set_xlabel('Y [%]', fontsize=12)
axes1[0, 2].set_ylabel('K [%]', fontsize=12)
axes1[0, 2].set_title('Y vs K', fontsize=13)
axes1[0, 2].set_xlim(0, 100)
axes1[0, 2].set_ylim(0, 100)
axes1[0, 2].grid(True, alpha=0.3)

# 2行目: Y vs M+C, Y vs M+K
axes1[1, 0].scatter(Y_percent, MC_percent, c=colors, s=PLOT_SIZE)
axes1[1, 0].set_xlabel('Y [%]', fontsize=12)
axes1[1, 0].set_ylabel('M+C [%]', fontsize=12)
axes1[1, 0].set_title('Y vs M+C', fontsize=13)
axes1[1, 0].set_xlim(0, 100)
axes1[1, 0].set_ylim(0, 200)
axes1[1, 0].grid(True, alpha=0.3)

axes1[1, 1].scatter(Y_percent, MK_percent, c=colors, s=PLOT_SIZE)
axes1[1, 1].set_xlabel('Y [%]', fontsize=12)
axes1[1, 1].set_ylabel('M+K [%]', fontsize=12)
axes1[1, 1].set_title('Y vs M+K', fontsize=13)
axes1[1, 1].set_xlim(0, 100)
axes1[1, 1].set_ylim(0, 200)
axes1[1, 1].grid(True, alpha=0.3)

axes1[1, 2].axis('off')

# 3行目: Y vs Y+M+C
axes1[2, 0].scatter(Y_percent, YMC_percent, c=colors, s=PLOT_SIZE)
axes1[2, 0].set_xlabel('Y [%]', fontsize=12)
axes1[2, 0].set_ylabel('Y+M+C [%]', fontsize=12)
axes1[2, 0].set_title('Y vs Y+M+C', fontsize=13)
axes1[2, 0].set_xlim(0, 100)
axes1[2, 0].set_ylim(0, 300)
axes1[2, 0].grid(True, alpha=0.3)

axes1[2, 1].axis('off')
axes1[2, 2].axis('off')

# 4行目: Y+M+C+Kのヒストグラム
axes1[3, 0].hist(YMCK_percent, bins=30, color='gray', edgecolor='black', alpha=0.7)
axes1[3, 0].set_xlabel('Y+M+C+K [%]', fontsize=12)
axes1[3, 0].set_ylabel('Frequency', fontsize=12)
axes1[3, 0].set_title('Histogram of Y+M+C+K', fontsize=13)
axes1[3, 0].grid(True, alpha=0.3)

axes1[3, 1].axis('off')
axes1[3, 2].axis('off')

plt.tight_layout()

# ====================
# Mベースのグラフ
# ====================
fig2, axes2 = plt.subplots(4, 3, figsize=(13, 10))
fig2.suptitle('M-based Graphs', fontsize=16, fontweight='bold')

# 1行目: M vs Y, M vs C, M vs K
axes2[0, 0].scatter(M_percent, Y_percent, c=colors, s=PLOT_SIZE)
axes2[0, 0].set_xlabel('M [%]', fontsize=12)
axes2[0, 0].set_ylabel('Y [%]', fontsize=12)
axes2[0, 0].set_title('M vs Y', fontsize=13)
axes2[0, 0].set_xlim(0, 100)
axes2[0, 0].set_ylim(0, 100)
axes2[0, 0].grid(True, alpha=0.3)

axes2[0, 1].scatter(M_percent, C_percent, c=colors, s=PLOT_SIZE)
axes2[0, 1].set_xlabel('M [%]', fontsize=12)
axes2[0, 1].set_ylabel('C [%]', fontsize=12)
axes2[0, 1].set_title('M vs C', fontsize=13)
axes2[0, 1].set_xlim(0, 100)
axes2[0, 1].set_ylim(0, 100)
axes2[0, 1].grid(True, alpha=0.3)

axes2[0, 2].scatter(M_percent, K_percent, c=colors, s=PLOT_SIZE)
axes2[0, 2].set_xlabel('M [%]', fontsize=12)
axes2[0, 2].set_ylabel('K [%]', fontsize=12)
axes2[0, 2].set_title('M vs K', fontsize=13)
axes2[0, 2].set_xlim(0, 100)
axes2[0, 2].set_ylim(0, 100)
axes2[0, 2].grid(True, alpha=0.3)

# 2行目: M vs Y+C, M vs Y+K
axes2[1, 0].scatter(M_percent, YC_percent, c=colors, s=PLOT_SIZE)
axes2[1, 0].set_xlabel('M [%]', fontsize=12)
axes2[1, 0].set_ylabel('Y+C [%]', fontsize=12)
axes2[1, 0].set_title('M vs Y+C', fontsize=13)
axes2[1, 0].set_xlim(0, 100)
axes2[1, 0].set_ylim(0, 200)
axes2[1, 0].grid(True, alpha=0.3)

axes2[1, 1].scatter(M_percent, YK_percent, c=colors, s=PLOT_SIZE)
axes2[1, 1].set_xlabel('M [%]', fontsize=12)
axes2[1, 1].set_ylabel('Y+K [%]', fontsize=12)
axes2[1, 1].set_title('M vs Y+K', fontsize=13)
axes2[1, 1].set_xlim(0, 100)
axes2[1, 1].set_ylim(0, 200)
axes2[1, 1].grid(True, alpha=0.3)

axes2[1, 2].axis('off')

# 3行目: M vs M+Y+C
axes2[2, 0].scatter(M_percent, MYC_percent, c=colors, s=PLOT_SIZE)
axes2[2, 0].set_xlabel('M [%]', fontsize=12)
axes2[2, 0].set_ylabel('M+Y+C [%]', fontsize=12)
axes2[2, 0].set_title('M vs M+Y+C', fontsize=13)
axes2[2, 0].set_xlim(0, 100)
axes2[2, 0].set_ylim(0, 300)
axes2[2, 0].grid(True, alpha=0.3)

axes2[2, 1].axis('off')
axes2[2, 2].axis('off')

# 4行目: Y+M+C+Kのヒストグラム
axes2[3, 0].hist(YMCK_percent, bins=30, color='gray', edgecolor='black', alpha=0.7)
axes2[3, 0].set_xlabel('Y+M+C+K [%]', fontsize=12)
axes2[3, 0].set_ylabel('Frequency', fontsize=12)
axes2[3, 0].set_title('Histogram of Y+M+C+K', fontsize=13)
axes2[3, 0].grid(True, alpha=0.3)

axes2[3, 1].axis('off')
axes2[3, 2].axis('off')

plt.tight_layout()

# ====================
# Cベースのグラフ
# ====================
fig3, axes3 = plt.subplots(4, 3, figsize=(13, 10))
fig3.suptitle('C-based Graphs', fontsize=16, fontweight='bold')

# 1行目: C vs Y, C vs M, C vs K
axes3[0, 0].scatter(C_percent, Y_percent, c=colors, s=PLOT_SIZE)
axes3[0, 0].set_xlabel('C [%]', fontsize=12)
axes3[0, 0].set_ylabel('Y [%]', fontsize=12)
axes3[0, 0].set_title('C vs Y', fontsize=13)
axes3[0, 0].set_xlim(0, 100)
axes3[0, 0].set_ylim(0, 100)
axes3[0, 0].grid(True, alpha=0.3)

axes3[0, 1].scatter(C_percent, M_percent, c=colors, s=PLOT_SIZE)
axes3[0, 1].set_xlabel('C [%]', fontsize=12)
axes3[0, 1].set_ylabel('M [%]', fontsize=12)
axes3[0, 1].set_title('C vs M', fontsize=13)
axes3[0, 1].set_xlim(0, 100)
axes3[0, 1].set_ylim(0, 100)
axes3[0, 1].grid(True, alpha=0.3)

axes3[0, 2].scatter(C_percent, K_percent, c=colors, s=PLOT_SIZE)
axes3[0, 2].set_xlabel('C [%]', fontsize=12)
axes3[0, 2].set_ylabel('K [%]', fontsize=12)
axes3[0, 2].set_title('C vs K', fontsize=13)
axes3[0, 2].set_xlim(0, 100)
axes3[0, 2].set_ylim(0, 100)
axes3[0, 2].grid(True, alpha=0.3)

# 2行目: C vs Y+M, C vs Y+K
axes3[1, 0].scatter(C_percent, Y_percent + M_percent, c=colors, s=PLOT_SIZE)
axes3[1, 0].set_xlabel('C [%]', fontsize=12)
axes3[1, 0].set_ylabel('Y+M [%]', fontsize=12)
axes3[1, 0].set_title('C vs Y+M', fontsize=13)
axes3[1, 0].set_xlim(0, 100)
axes3[1, 0].set_ylim(0, 200)
axes3[1, 0].grid(True, alpha=0.3)

axes3[1, 1].scatter(C_percent, YK_percent, c=colors, s=PLOT_SIZE)
axes3[1, 1].set_xlabel('C [%]', fontsize=12)
axes3[1, 1].set_ylabel('Y+K [%]', fontsize=12)
axes3[1, 1].set_title('C vs Y+K', fontsize=13)
axes3[1, 1].set_xlim(0, 100)
axes3[1, 1].set_ylim(0, 200)
axes3[1, 1].grid(True, alpha=0.3)

axes3[1, 2].axis('off')

# 3行目: C vs C+Y+M
axes3[2, 0].scatter(C_percent, YMC_percent, c=colors, s=PLOT_SIZE)
axes3[2, 0].set_xlabel('C [%]', fontsize=12)
axes3[2, 0].set_ylabel('C+Y+M [%]', fontsize=12)
axes3[2, 0].set_title('C vs C+Y+M', fontsize=13)
axes3[2, 0].set_xlim(0, 100)
axes3[2, 0].set_ylim(0, 300)
axes3[2, 0].grid(True, alpha=0.3)

axes3[2, 1].axis('off')
axes3[2, 2].axis('off')

# 4行目: Y+M+C+Kのヒストグラム
axes3[3, 0].hist(YMCK_percent, bins=30, color='gray', edgecolor='black', alpha=0.7)
axes3[3, 0].set_xlabel('Y+M+C+K [%]', fontsize=12)
axes3[3, 0].set_ylabel('Frequency', fontsize=12)
axes3[3, 0].set_title('Histogram of Y+M+C+K', fontsize=13)
axes3[3, 0].grid(True, alpha=0.3)

axes3[3, 1].axis('off')
axes3[3, 2].axis('off')

plt.tight_layout()

# ====================
# Kベースのグラフ
# ====================
fig4, axes4 = plt.subplots(4, 3, figsize=(13, 10))
fig4.suptitle('K-based Graphs', fontsize=16, fontweight='bold')

# 1行目: K vs Y, K vs M, K vs C
axes4[0, 0].scatter(K_percent, Y_percent, c=colors, s=PLOT_SIZE)
axes4[0, 0].set_xlabel('K [%]', fontsize=12)
axes4[0, 0].set_ylabel('Y [%]', fontsize=12)
axes4[0, 0].set_title('K vs Y', fontsize=13)
axes4[0, 0].set_xlim(0, 100)
axes4[0, 0].set_ylim(0, 100)
axes4[0, 0].grid(True, alpha=0.3)

axes4[0, 1].scatter(K_percent, M_percent, c=colors, s=PLOT_SIZE)
axes4[0, 1].set_xlabel('K [%]', fontsize=12)
axes4[0, 1].set_ylabel('M [%]', fontsize=12)
axes4[0, 1].set_title('K vs M', fontsize=13)
axes4[0, 1].set_xlim(0, 100)
axes4[0, 1].set_ylim(0, 100)
axes4[0, 1].grid(True, alpha=0.3)

axes4[0, 2].scatter(K_percent, C_percent, c=colors, s=PLOT_SIZE)
axes4[0, 2].set_xlabel('K [%]', fontsize=12)
axes4[0, 2].set_ylabel('C [%]', fontsize=12)
axes4[0, 2].set_title('K vs C', fontsize=13)
axes4[0, 2].set_xlim(0, 100)
axes4[0, 2].set_ylim(0, 100)
axes4[0, 2].grid(True, alpha=0.3)

# 2行目: K vs Y+M, K vs Y+C
axes4[1, 0].scatter(K_percent, Y_percent + M_percent, c=colors, s=PLOT_SIZE)
axes4[1, 0].set_xlabel('K [%]', fontsize=12)
axes4[1, 0].set_ylabel('Y+M [%]', fontsize=12)
axes4[1, 0].set_title('K vs Y+M', fontsize=13)
axes4[1, 0].set_xlim(0, 100)
axes4[1, 0].set_ylim(0, 200)
axes4[1, 0].grid(True, alpha=0.3)

axes4[1, 1].scatter(K_percent, YC_percent, c=colors, s=PLOT_SIZE)
axes4[1, 1].set_xlabel('K [%]', fontsize=12)
axes4[1, 1].set_ylabel('Y+C [%]', fontsize=12)
axes4[1, 1].set_title('K vs Y+C', fontsize=13)
axes4[1, 1].set_xlim(0, 100)
axes4[1, 1].set_ylim(0, 200)
axes4[1, 1].grid(True, alpha=0.3)

axes4[1, 2].axis('off')

# 3行目: K vs K+Y+M+C
axes4[2, 0].scatter(K_percent, YMCK_percent, c=colors, s=PLOT_SIZE)
axes4[2, 0].set_xlabel('K [%]', fontsize=12)
axes4[2, 0].set_ylabel('K+Y+M+C [%]', fontsize=12)
axes4[2, 0].set_title('K vs K+Y+M+C', fontsize=13)
axes4[2, 0].set_xlim(0, 100)
axes4[2, 0].set_ylim(0, 400)
axes4[2, 0].grid(True, alpha=0.3)

axes4[2, 1].axis('off')
axes4[2, 2].axis('off')

# 4行目: Y+M+C+Kのヒストグラム
axes4[3, 0].hist(YMCK_percent, bins=30, color='gray', edgecolor='black', alpha=0.7)
axes4[3, 0].set_xlabel('Y+M+C+K [%]', fontsize=12)
axes4[3, 0].set_ylabel('Frequency', fontsize=12)
axes4[3, 0].set_title('Histogram of Y+M+C+K', fontsize=13)
axes4[3, 0].grid(True, alpha=0.3)

axes4[3, 1].axis('off')
axes4[3, 2].axis('off')

plt.tight_layout()

# すべてのグラフを表示
plt.show()