# Currency Converter API

A Python-based RESTful API that provides real-time currency conversion using live exchange rates from external APIs.

## Features

- 💱 Convert between multiple international currencies
- 📊 Fetch real-time exchange rates
- 🚀 RESTful API endpoints for easy integration
- ⚡ Fast and lightweight
- 🔄 Support for major world currencies

## Technologies Used

- **Python 3.x** - Core programming language
- **Requests** - HTTP library for fetching exchange rates
- **External API** - Real-time currency data provider

## Project Structure

```
02-Currency-Converter-API/
├── main.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Python-RealWorld-Projects.git
    cd Python-RealWorld-Projects/02-Currency-Converter-API
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Start the API server:**
    ```bash
    python main.py
    ```
## API Endpoints

### Convert Currency
- **Endpoint:** `/convert`
- **Method:** GET
- **Parameters:**
  - `from` (required): Source currency code (e.g., USD)
  - `to` (required): Target currency code (e.g., EUR)
  - `amount` (required): Amount to convert
- **Response:**
  ```json
  {
     "from": "USD",
     "to": "EUR",
     "amount": 100,
     "result": 85.50,
     "rate": 0.855
  }
  ```

### Get Exchange Rates
- **Endpoint:** `/rates`
- **Method:** GET
- **Parameters:**
  - `base` (optional): Base currency (default: USD)
- **Response:**
  ```json
  {
     "base": "USD",
     "rates": {
        "EUR": 0.855,
        "GBP": 0.732,
        "JPY": 110.25
     }
  }
  ```

## Supported Currencies

Common currencies include: USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR, and more.

