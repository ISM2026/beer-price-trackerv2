import requests
import pandas as pd
from datetime import datetime

# 👇 Aqui colocas os teus produtos reais depois
products = [
    {
        "brand": "Sagres",
        "retailer": "Pingo Doce",
        "url": "COLOCA_AQUI_URL_DO_PRODUTO"
    },
    {
        "brand": "Super Bock",
        "retailer": "Continente",
        "url": "COLOCA_AQUI_URL_DO_PRODUTO"
    }
]

def get_price(url):
    """
    Função base de scraping.
    Vais ter de ajustar isto por retailer mais tarde.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10)

    # ⚠️ placeholder (porque cada site é diferente)
    # depois substituímos por BeautifulSoup ou API parsing
    if r.status_code == 200:
        return "PRICE_NEEDS_PARSING"
    else:
        return None


rows = []

for p in products:
    price = get_price(p["url"])

    rows.append({
        "date": datetime.today().strftime("%Y-%m-%d"),
        "brand": p["brand"],
        "retailer": p["retailer"],
        "price": price
    })

df = pd.DataFrame(rows)

# cria pasta se não existir
import os
os.makedirs("data", exist_ok=True)

file_path = "data/prices.csv"

# guarda histórico (append simples)
df.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)

print("Scraping concluído")
