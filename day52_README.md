# Day 52 - Weather Intelligence Network

## Problem Statement

A global weather agency needs a dashboard that fetches live weather information from different cities.

The system communicates with a weather API, processes JSON responses, and displays useful weather insights.

---

# Objectives

- Fetch weather data from a public API
- Parse JSON responses
- Display formatted weather summaries
- Handle API failures gracefully

---

# API Used

OpenWeatherMap API

Endpoint:

https://api.openweathermap.org/data/2.5/weather

---

# Request Flow

User
 |
 | Requests Weather
 v
Application
 |
 | API Request
 v
Weather API
 |
 | JSON Response
 v
Application
 |
 | Parse Data
 v
Formatted Weather Report

---

# JSON Response Example

{
  "name": "Delhi",
  "main": {
      "temp": 31.4,
      "humidity": 68
  },
  "weather": [
      {
         "description": "scattered clouds"
      }
  ]
}

---

# Parsed Information

- City Name
- Temperature
- Humidity
- Weather Condition

---

# Error Handling

### Invalid City

Returns:

404 Not Found

---

### Invalid API Key

Returns:

401 Unauthorized

---

### Network Failure

Handled using:

try-except block

---

# Why APIs Matter

APIs allow independent systems to communicate.

Examples:

- Weather Apps
- Payment Gateways
- Google Maps
- Social Media Platforms
- Food Delivery Apps

---

# Complexity Analysis

API Request:

O(1)

JSON Parsing:

O(1)

Space Complexity:

O(1)

---

# Real-World Impact

API integrations are used in:

- Mobile Applications
- Web Applications
- Banking Systems
- Logistics Platforms
- Cloud Services

---

# Conclusion

APIs act as bridges between systems. By fetching live weather information and processing JSON responses, we can build intelligent applications that use real-time data.