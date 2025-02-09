from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError, RPCError
import pandas as pd
import time
import json
from datetime import datetime

# Telegram API credentials (Replace with your credentials)
API_ID = "29939453"
API_HASH = "32e841f7734e95f765609e6ae9261531"

# List of Telegram channels to scrape
CHANNELS = [
    "dagilaptop",
    # "liqtechnologies",
    # "beracomputer",
    # "ethioelectronicsnew",
    # "mesaymobile"
]

# Output CSV file
OUTPUT_FILE = "telegram_data_large1.csv"

# Function to extract messages
def scrape_telegram_messages():
    all_messages = []

    with TelegramClient("session_name", API_ID, API_HASH) as client:
        for channel in CHANNELS:
            try:
                print(f"Scraping messages from: {channel}...")
                for message in client.iter_messages(channel, limit=4000,offset_date=datetime(2024, 1, 1)):  # Adjust limit as needed
                    if message.text:
                        all_messages.append({
                            "channel": channel,
                            "message_id": message.id,
                            "date": message.date.strftime("%Y-%m-%d %H:%M:%S"),
                            "sender_id": message.sender_id,
                            "message_text": message.text
                        })
                print(f"✅ Done scraping {channel}")
            except FloodWaitError as e:
                print(f"⚠️ Rate limit hit! Sleeping for {e.seconds} seconds...")
                time.sleep(e.seconds)
            except RPCError as e:
                print(f"❌ RPC Error: {e}")
            except Exception as e:
                print(f"❌ Error scraping {channel}: {e}")

    return all_messages

# Main execution
if __name__ == "__main__":
    print("🚀 Starting Telegram Scraper...")
    messages = scrape_telegram_messages()

    # Convert to DataFrame and save as CSV
    if messages:
        df = pd.DataFrame(messages)
        df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")  # UTF-8-sig to support Amharic text
        print(f"✅ Data saved to {OUTPUT_FILE}")
    else:
        print("⚠️ No data scraped!")

    print("🎉 Scraping Completed!")
