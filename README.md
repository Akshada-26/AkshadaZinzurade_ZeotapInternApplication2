
# Real-Time Weather Monitoring System

## Description
A web application that fetches real-time weather data from the OpenWeatherMap API and provides summaries and alerts based on user-defined thresholds.

## Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Akshada-26/AkshadaZinzurade_ZeotapInternApplication2
  
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
   - Ensure your MySQL server is running and the database is set up.
4. **Or use Docker:**
   ```bash
   docker-compose up
   ```

## Design Choices
- **Backend Framework:** Flask
- **Database:** MySQL for data storage
- **API:** OpenWeatherMap API for fetching weather data

## Testing
- Ensure that the MySQL server is running.
- Access the application via `http://localhost/`.

## Non-Functional Items
### Security Measures
- Input validation to prevent SQL injection.
- Use environment variables for sensitive information like API keys.

### Performance Considerations
- Optimize data retrieval by caching responses from the OpenWeatherMap API when necessary.
- Batch updates to the database instead of individual inserts to reduce load.

## OUTPUT
![image](https://github.com/user-attachments/assets/12e437a1-55a0-4df6-995c-f05e6872e3c5)

