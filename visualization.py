import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_top_brands(df, top_n=10, save_path="static/plots/brands.png"):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # ✅ auto-create folder
    top = df['brand'].value_counts().nlargest(top_n)
    sns.barplot(x=top.index, y=top.values)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(save_path)
