Stock Price Alert
 
Overview
Stock Price Alert is a Python-based application that monitors the stock prices of your desired stocks and sends alerts via SMS and WhatsApp whenever the price changes by more than 5% compared to the previous day's closing price. This tool is invaluable for investors who need real-time updates on their portfolio's performance and want to stay informed about significant price fluctuations in the stock market.
The application utilizes multiple APIs, including Twilio for SMS alerts, Alpha Vantage for retrieving stock market data, and PythonAnywhere for cloud hosting and scheduling daily runs. Additionally, it fetches the latest news about the companies whose stocks you are monitoring to provide you with valuable insights alongside the price alerts.
Features
•	Real-time Price Monitoring: Stock Price Alert continuously checks the stock prices for the stocks you've specified, ensuring you're always aware of any significant changes.
•	Price Change Alerts: Whenever a stock's price increases or decreases by more than 5% compared to the previous day's closing price, you'll receive an alert via SMS and WhatsApp.
•	Latest Company News: The application fetches the latest news about the companies whose stocks you're tracking, giving you additional context for your investments.
•	Scheduled Daily Execution: Stock Price Alert is scheduled to run daily at 9:30 AM, making it ideal for monitoring pre-market movements.
•	Easy Configuration: You can easily configure the stocks you want to monitor and set up your Twilio and WhatsApp credentials for receiving alerts.
Usage
To use Stock Price Alert:
1.	Clone the repository to your local machine.
bashCopy code
git clone https://github.com/yourusername/stock-price-alert.git 
2.	Install the required Python packages using pip.
bashCopy code
pip install -r requirements.txt 
3.	Configure your Twilio and Alpha Vantage API credentials and WhatsApp settings in the config.py file.
4.	Specify the stocks you want to monitor and the desired percentage change in the stocks.json file.
5.	Run the application.
bashCopy code
python main.py 
Dependencies
•	Twilio: For SMS alerts.
•	Alpha Vantage: For retrieving stock market data.
•	PythonAnywhere: For cloud hosting and scheduled execution.

