# import yfinance as yf
# usd_brl = yf.Ticker("USD=X")
# cotacao_dolar = usd_brl.info["regularMarketPrice"]
# print(f"Cotação dólar em 17/02/2024: R$ {}")

import yfinance as yf
import matplotlib.pyplot as plt

ticker = "BRL=X"
ticker_data = yf.Ticker(ticker)
recent_data = ticker_data.history(period="10d")
print(recent_data)

# gráfico
plt.figure(figsize=(10, 6))
plt.plot(recent_data.index, recent_data["Close"], marker="o", linestyle="-")
plt.title(f"Cotação do Dólar em relação ao Real brasileiro")
plt.xlabel("Data")
plt.ylabel("Preço do Fechamento (BRL)")
plt.grid(True)
plt.show()
