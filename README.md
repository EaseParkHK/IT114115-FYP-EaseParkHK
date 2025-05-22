# EaseParkHK

[![Flask 3.1.0](https://img.shields.io/badge/Flask-3.1.0-000?logo=flask)](https://flask.palletsprojects.com/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-886FBF?logo=googlegemini&logoColor=fff)](#)
[![Powered by data.gov.hk](https://img.shields.io/badge/Powered%20by-data.gov.hk-blue)](https://data.gov.hk/en/)
[![MIT License](https://img.shields.io/github/license/EaseParkHK/EaseParkHK?color=yellow)](https://github.com/EaseParkHK/EaseParkHK/blob/main/LICENSE)

[![Code Size](https://img.shields.io/github/languages/code-size/EaseParkHK/EaseParkHK?style=flat-square&logo=github)](https://github.com/EaseParkHK/EaseParkHK)

**EaseParkHK** is a Flask-based car park vacancy system providing real-time parking availability for car parks across Hong Kong districts. It offers an intuitive interface to help users find available parking, view traffic information, check road conditions, and interact with an AI assistant for parking queries.

**Academic Context**  
This project is developed as part of the Final Year Project for the [Higher Diploma in Cloud and Data Centre Administration](https://www.vtc.edu.hk/admission/en/programme/it114115-higher-diploma-in-cloud-and-data-centre-administration/) at the Hong Kong Institute of Vocational Education (IVE).

## Features

- **Real-time car park vacancy updates** for Hong Kong.
- **Meter parking space availability**.
- **Traffic camera feeds** for real-time road monitoring.
- **Traffic notices** for road closures, accidents, and alerts.
- **AI assistant** for car park vacancy queries.
- **Filter by vehicle type** (e.g., private cars, motorcycles).
- **Detailed car park info** (address, contact, website).
- **Interactive map** showing car park and meter locations.

## Installation & Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/easeparkhk/IT114115-FYP-EaseParkHK
    cd IT114115-FYP-EaseParkHK
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate         # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Populate the database:**
    ```bash
    python test_data.py
    ```

5. **Run the application:**
    ```bash
    flask --debug run --host=0.0.0.0
    ```
    
## Ports and Services

- Port 5000: EaseParkHK website (main application)
- Port 5050: pgAdmin (Docker-based database management)
- Port 8025: Email reset website (for password recovery)

---

## Usage

1. Go to [http://localhost:5000](http://localhost:5000) to access EaseParkHK.
2. Use the navigation bar to browse car parks and meter parking by district.
3. Filter by vehicle type or view locations on the map.
4. Access traffic cameras and notices for real-time updates.
5. Ask the AI assistant questions (e.g., “Which car parks in Kowloon have spaces now?”).
6. Manage the database with pgAdmin at [http://localhost:5050](http://localhost:5050).
7. Use [http://localhost:8025](http://localhost:8025) for email-based password resets.

## Contributors

### Development Team
- **Henry Lok**  
  [GitHub](https://github.com/HenryLok0) | [LinkedIn](https://www.linkedin.com/in/ihenrylok/)

- **Percy Wong**  
  [GitHub](https://github.com/wongpakhei) | [LinkedIn](https://www.linkedin.com/in/percy-wong/)

- **Peter Chan**  
  [GitHub](https://github.com/Peterop-Chan) | [LinkedIn](https://www.linkedin.com/in/chan-cheuk-nam-19ab75364/)

- **Ben Ho**  
  [GitHub](https://github.com/HoChiWa01) | [LinkedIn](https://www.linkedin.com/in/hochiwa-ben/)

### Project Supervisor
- **Harry Li**  
  [GitHub](https://github.com/i45000) | [LinkedIn](https://www.linkedin.com/in/harry-li-61949017a/)

---

## License

[MIT License](https://github.com/EaseParkHK/EaseParkHK/blob/main/LICENSE)
