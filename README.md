# Stock Price Alert

## Overview

**Stock Price Alert** is a Python-based application designed to monitor the stock prices of your selected stocks and send timely alerts via SMS and WhatsApp whenever there is a price change of more than 5% compared to the previous day's closing price. This tool is particularly beneficial for investors seeking real-time updates on their portfolio's performance and staying informed about significant price fluctuations in the stock market.

The application leverages multiple APIs, including Twilio for SMS alerts, Alpha Vantage for retrieving stock market data, and PythonAnywhere for cloud hosting and scheduling daily runs. In addition to price alerts, the tool fetches the latest news about the companies whose stocks you are monitoring, providing valuable insights alongside the alerts.

## Features

- **Real-time Price Monitoring:** Continuously checks stock prices for specified stocks, ensuring you are always aware of any significant changes.
- **Price Change Alerts:** Receive alerts via SMS and WhatsApp whenever a stock's price increases or decreases by more than 5% compared to the previous day's closing price.
- **Latest Company News:** Fetches the latest news about the companies you're tracking, offering additional context for your investments.
- **Scheduled Daily Execution:** Scheduled to run daily at 9:30 AM, making it ideal for monitoring pre-market movements.
- **Easy Configuration:** Easily configure the stocks to monitor and set up Twilio and WhatsApp credentials for receiving alerts.

## Usage

To use **Stock Price Alert**:

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/stock-price-alert.git
    ```

2. Install the required Python packages using pip.

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your Twilio and Alpha Vantage API credentials and WhatsApp settings in the `config.py` file.

4. Specify the stocks you want to monitor and the desired percentage change in the `stocks.json` file.

5. Run the application.

    ```bash
    python main.py
    ```

## Dependencies

- **Twilio:** For SMS alerts.
- **Alpha Vantage:** For retrieving stock market data.
- **PythonAnywhere:** For cloud hosting and scheduled execution.
