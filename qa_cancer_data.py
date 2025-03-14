import polars as pl
import matplotlib.pyplot as plt

# laod in the datasets 
full_df = pl.read_csv("data/breast_cancer.csv")
sample_df = pl.read_json("breast_cancer_sample_10.json")


# shoutout xAI for the plots below: 



# Prepare data for plotting
full_m = full_df.filter(pl.col("diagnosis") == "M")
full_b = full_df.filter(pl.col("diagnosis") == "B")
sample_m = sample_df.filter(pl.col("diagnosis") == "M")
sample_b = sample_df.filter(pl.col("diagnosis") == "B")

# Create scatter plots for radius vs. perimeter and texture vs. perimeter
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


# Plot 1: Radius vs. Perimeter
ax1.scatter(full_b["radius_mean"], full_b["perimeter_mean"], c="green", alpha=0.5, label="Benign (full)")
ax1.scatter(full_m["radius_mean"], full_m["perimeter_mean"], c="red", alpha=0.5, label="Malignant (full)")
ax1.scatter(sample_b["radius_mean"], sample_b["perimeter_mean"], c="blue", s=100, edgecolors="black", label="Benign (sample)")
ax1.scatter(sample_m["radius_mean"], sample_m["perimeter_mean"], c="orange", s=100, edgecolors="black", label="Malignant (sample)")
ax1.set_xlabel("Mean Radius")
ax1.set_ylabel("Mean Perimeter")
ax1.set_title("Radius vs. Perimeter by Diagnosis")
ax1.legend()

# Plot 2: Texture vs. Perimeter
ax2.scatter(full_b["texture_mean"], full_b["perimeter_mean"], c="green", alpha=0.5, label="Benign (full)")
ax2.scatter(full_m["texture_mean"], full_m["perimeter_mean"], c="red", alpha=0.5, label="Malignant (full)")
ax2.scatter(sample_b["texture_mean"], sample_b["perimeter_mean"], c="blue", s=100, edgecolors="black", label="Benign (sample)")
ax2.scatter(sample_m["texture_mean"], sample_m["perimeter_mean"], c="orange", s=100, edgecolors="black", label="Malignant (sample)")
ax2.set_xlabel("Mean Texture")
ax2.set_ylabel("Mean Perimeter")
ax2.set_title("Texture vs. Perimeter by Diagnosis")
ax2.legend()

plt.tight_layout()
plt.show()

# Print the assessed sample for reference
print(sample_df.select([
    "diagnosis",
    "radius_mean",
    "texture_mean",
    "perimeter_mean",
    "quality_assessment"
]))
