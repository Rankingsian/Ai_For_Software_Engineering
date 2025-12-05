# Task 2: AI-Driven IoT Concept - Smart Agriculture

## Scenario
Design a smart agriculture simulation system using AI and IoT to optimize crop management and predict yields.

## 1. Required Sensors
To monitor the health of the crops and the environment, the following sensors are essential:

*   **Soil Moisture Sensor:** Measures the water content in the soil to determine irrigation needs.
*   **Temperature & Humidity Sensor (e.g., DHT22):** Monitors ambient air temperature and humidity levels, which are critical for plant growth.
*   **Light Intensity Sensor (LDR or Lux Sensor):** Measures sunlight exposure to ensure crops receive adequate light.
*   **Soil pH Sensor:** Monitors soil acidity/alkalinity to optimize nutrient absorption.
*   **NPK Sensor:** Measures Nitrogen, Phosphorus, and Potassium levels in the soil (essential nutrients).

## 2. AI Model for Crop Yield Prediction
**Proposed Model:** Random Forest Regressor or Long Short-Term Memory (LSTM) Network.

*   **Input Features:** Historical data from sensors (moisture, temp, humidity, light, pH), weather forecasts, and historical yield data.
*   **Target Variable:** Predicted Crop Yield (e.g., kg/hectare).
*   **Justification:** A Random Forest is robust and handles non-linear relationships well for tabular data. An LSTM would be suitable if treating the sensor data as a time-series to capture temporal dependencies (e.g., growth stages).
*   **Function:** The model analyzes current conditions against historical patterns to predict the expected harvest. It can also suggest interventions (e.g., "Increase water by 10% to boost yield by 5%").

## 3. Data Flow Diagram

The following diagram illustrates how data flows from the sensors to the AI processing unit and back to the user or actuators.

```mermaid
graph TD
    subgraph IoT_Layer [IoT Device Layer]
        S1[Soil Moisture Sensor]
        S2[Temp & Humidity Sensor]
        S3[Light Sensor]
        S4[pH Sensor]
        MCU[Microcontroller (ESP32/Raspberry Pi)]
    end

    subgraph Edge_Layer [Edge Processing]
        GW[Edge Gateway]
        Local_Model[Lightweight Anomaly Detection]
    end

    subgraph Cloud_Layer [Cloud/Server Layer]
        DB[(Time-Series Database)]
        AI_Engine[AI Yield Prediction Model]
        API[Backend API]
    end

    subgraph User_Layer [User Interface]
        Dash[Farmer Dashboard]
        Alert[Mobile Alerts]
        Actuators[Irrigation System]
    end

    %% Data Flow
    S1 & S2 & S3 & S4 -->|Raw Data| MCU
    MCU -->|MQTT/CoAP| GW
    GW -->|Preprocessed Data| DB
    GW -->|Immediate Alerts| Local_Model
    
    DB -->|Historical Data| AI_Engine
    AI_Engine -->|Yield Prediction| API
    
    API -->|Insights & Stats| Dash
    Local_Model -->|Critical Alert| Alert
    API -->|Control Signal| Actuators
    
    style IoT_Layer fill:#e1f5fe,stroke:#01579b
    style Cloud_Layer fill:#fff3e0,stroke:#e65100
    style User_Layer fill:#e8f5e9,stroke:#1b5e20
```

## Explanation of Data Flow
1.  **Data Collection:** Sensors continuously collect environmental data.
2.  **Transmission:** The microcontroller (e.g., ESP32) reads sensor data and transmits it via MQTT to an Edge Gateway.
3.  **Edge Processing:** The gateway performs basic filtering and can run a lightweight model for immediate anomaly detection (e.g., "Critical drought detected").
4.  **Cloud Storage & AI:** Cleaned data is stored in a cloud database. The complex AI Yield Prediction Model runs periodically on this historical data to generate forecasts.
5.  **Action:** Predictions and insights are displayed on the Farmer's Dashboard. If the AI suggests irrigation, a control signal can be sent back to the automated irrigation system.
