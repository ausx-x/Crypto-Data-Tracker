import datetime
import os
import urllib.request
import json

def fetch_crypto_price():
    try:
        # Fetching data from CoinGecko free public API
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            price = data['bitcoin']['usd']
            
            # Format data line
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_line = f"{current_time},Bitcoin,{price}\n"
            
            # Append data to local CSV file
            file_exists = os.path.isfile("crypto_data.csv")
            with open("crypto_data.csv", "a") as f:
                if not file_exists:
                    f.write("Timestamp,Asset,Price_USD\n") # Header
                f.write(log_line)
                
            print(f"Successfully logged price: ${price}")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_crypto_price()
