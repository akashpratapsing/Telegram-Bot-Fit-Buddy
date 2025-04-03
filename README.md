# Fit Buddy - Telegram Bot

## Overview
Fit Buddy is a Telegram bot designed to provide quick and accurate fitness calculations, including BMI, BMR, and body fat percentage. Built using Python and the Telegram Bot API, it ensures a smooth and interactive user experience with asynchronous processing for optimal performance.

## Features
- Supports **4 advanced fitness calculators** (BMI, BMR, body fat percentage, etc.).
- Implements **asynchronous workflows** for fast and efficient command processing.
- Uses **custom fitness computation algorithms**, improving reliability and reducing external API dependencies.
- Provides an **engaging and user-friendly interface** via the Telegram Bot API.

## Tech Stack
- **Python** – Core language for bot logic and fitness calculations.
- **Telegram Bot API** – Enables bot interactions with users.
- **python-telegram-bot** – Library for handling bot commands and API integration.
- **Asyncio** – Ensures efficient, non-blocking execution for better scalability.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/akashpratapsing/Telegram-Bot-Fit-Buddy
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your Telegram bot token:
   - Create a bot using [BotFather](https://t.me/BotFather) on Telegram.
   - Obtain the API token and set it in an environment variable:
     ```sh
     export TELEGRAM_BOT_TOKEN='your-bot-token-here'
     ```
4. Run the bot:
   ```sh
   python telegram_bot.py
   ```

## Usage
- **Start the bot**: `/start`
- **Calculate BMI**: `/bmi <weight_kg> <height_cm>`
- **Calculate BMR**: `/bmr <weight_kg> <height_cm> <age> <gender>`
- **Calculate Body Fat %**: `/bodyfat <weight_kg> <waist_cm> <gender>`

## Contributions
Feel free to contribute! Fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License.

---

🚀 **Stay fit with Fit Buddy!**
