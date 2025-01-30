import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.spatial.distance import euclidean
import seaborn as sns

# Mengatur agar pandas menampilkan seluruh baris
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# --- 1. Fungsi AHP untuk menentukan bobot kriteria ---
def ahp(pairwise_matrix):
    eigvals, eigvecs = np.linalg.eig(pairwise_matrix)
    max_index = np.argmax(eigvals)
    weights = eigvecs[:, max_index].real
    weights = weights / np.sum(weights)
    return weights

# --- 2. Fungsi TOPSIS untuk menentukan peringkat karyawan ---
def topsis(data, weights, benefit_criteria):
    data = np.array(data)
    norm_data = data / np.linalg.norm(data, axis=0)
    weighted_data = norm_data * weights
    ideal_best = np.max(weighted_data, axis=0) * benefit_criteria + np.min(weighted_data, axis=0) * (1 - benefit_criteria)
    ideal_worst = np.min(weighted_data, axis=0) * benefit_criteria + np.max(weighted_data, axis=0) * (1 - benefit_criteria)
    
    dist_best = np.apply_along_axis(euclidean, 1, weighted_data, ideal_best)
    dist_worst = np.apply_along_axis(euclidean, 1, weighted_data, ideal_worst)
    scores = dist_worst / (dist_best + dist_worst)
    
    return scores

# --- 3. Load Dataset dan Jalankan Analisis ---
# Membaca dataset
file_path = "dataset100000kariawan.csv"
df = pd.read_csv(file_path)

# Pilih kriteria untuk evaluasi
evaluation_criteria = ['Performance_Score', 'Projects_Handled', 'Employee_Satisfaction_Score', 'Years_At_Company']

# Matriks perbandingan berpasangan AHP
pairwise_matrix = np.array([
    [1, 3, 5, 2],
    [1/3, 1, 3, 1/2],
    [1/5, 1/3, 1, 1/4],
    [1/2, 2, 4, 1]
])

# Hitung bobot kriteria dengan AHP
weights = ahp(pairwise_matrix)
# Kriteria yang bersifat benefit (1 = benefit, 0 = cost)
benefit_criteria = np.array([1, 1, 1, 1])

# Klasifikasi berdasarkan pengalaman
bins = [0, 2, 6, np.inf]
labels = ['Junior', 'Mid-Level', 'Senior']
df['Experience_Level'] = pd.cut(df['Years_At_Company'], bins=bins, labels=labels, ordered=True)

# Buat folder untuk menyimpan grafik
output_folder = "grafix"
os.makedirs(output_folder, exist_ok=True)

# Gunakan palet warna yang lebih menarik
colors = sns.color_palette("viridis", 3)
color_map = {'Junior': colors[0], 'Mid-Level': colors[1], 'Senior': colors[2]}

# Pisahkan analisis berdasarkan Departemen, Posisi, dan Level Pengalaman
ranked_results = []
for (dept, job, exp_level), group in df.groupby(['Department', 'Job_Title', 'Experience_Level'], observed=True):
    data_matrix = group[evaluation_criteria].values
    scores = topsis(data_matrix, weights, benefit_criteria)
    group['TOPSIS_Score'] = scores
    group = group.sort_values(by='TOPSIS_Score', ascending=False)
    ranked_results.append(group)
    
    # Ambil karyawan terbaik per kategori
    top = group.head(50)
    
    plt.figure(figsize=(12, 8))
    y_positions = range(len(top))
    plt.barh(y_positions, top['TOPSIS_Score'], color=color_map[exp_level], align='center')
    plt.yticks(y_positions, top['Employee_ID'].astype(str))
    
    plt.xlabel("TOPSIS Score")
    plt.ylabel("Employee ID")
    plt.title(f"Top 50 Employees - {dept} - {job} - {exp_level}")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    
    # Simpan grafik
    file_name = f"{output_folder}/{dept}_{job}_{exp_level}.png".replace(" ", "_")
    plt.savefig(file_name)
    plt.close()

# Gabungkan hasil per kategori
df_ranked = pd.concat(ranked_results)

# Tampilkan 10 karyawan terbaik dari masing-masing kategori
print(df_ranked[['Employee_ID', 'Department', 'Job_Title', 'Experience_Level', 'TOPSIS_Score']].groupby(['Department', 'Job_Title', 'Experience_Level']).head(10))
