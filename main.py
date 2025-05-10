import pandas as pd
import time
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv("jalan_rusak.csv", parse_dates=["waktu"])

def analisis_kerusakan(data):
    print("\nANALISIS REAL-TIME")
    print(f"Total laporan: {len(data)}")
    
    rata = data["tingkat_kerusakan"].mean()
    print(f"Rata-rata tingkat kerusakan: {rata:.2f}")
    
    top_lokasi = data["lokasi"].value_counts().head(1)
    print("Lokasi paling sering dilaporkan:")
    print(top_lokasi)
    
    data.groupby("lokasi")["tingkat_kerusakan"].mean().sort_values().plot(kind="barh", title="Tingkat Kerusakan per Lokasi")
    plt.xlabel("Tingkat Kerusakan Rata-Rata")
    plt.tight_layout()
    plt.show()

print("Memulai analisis...\n")
current_data = pd.DataFrame(columns=df.columns)

for i in range(len(df)):
    current_data = pd.concat([current_data, df.iloc[[i]]])
    
    analisis_kerusakan(current_data)
    
    time.sleep(5)  
