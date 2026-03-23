import pandas as pd
import matplotlib.pyplot as plt

# Data project portfolio (contoh dummy)
data = {
    "Project": ["Flutter Portfolio", "QA Automation", "Python API", "Analytics Dashboard"],
    "Views": [1200, 800, 600, 400],
    "Clicks": [300, 200, 150, 100]
}

df = pd.DataFrame(data)

# Hitung CTR (Click Through Rate)
df["CTR"] = (df["Clicks"] / df["Views"]) * 100

print("=== Portfolio Analytics ===")
print(df)

# Visualisasi Views
plt.bar(df["Project"], df["Views"], color="skyblue")
plt.title("Project Views")
plt.xlabel("Project")
plt.ylabel("Views")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("views_chart.png")  # simpan grafik ke file
plt.show()
