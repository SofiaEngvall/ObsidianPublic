
```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

#define DHTPIN 2         // GPIO pin connected to the DHT sensor
#define DHTTYPE DHT11    // DHT 11 sensor type

// WiFi credentials
const char* ssid = "123";
const char* password = "456";

const char* mqtt_server = "172.2.0.80";  // Replace with your Raspberry Pi IP

const char* temperature_topic = "home/sensor/temperature";
const char* humidity_topic = "home/sensor/humidity";

DHT dht(DHTPIN, DHTTYPE);

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);

  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP().toString());
  delay(5000);
  // Setup MQTT
  client.setServer(mqtt_server, 1883);
}

void reconnect() {
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("Connected to MQTT");
    } else {
      Serial.print("Failed to connect. Retrying in 5 seconds...");
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor");
    delay(6900);
    return;
  }

  // Publish the temperature and humidity
  char tempString[8];
  dtostrf(t, 1, 2, tempString);
  client.publish(temperature_topic, tempString);

  char humString[8];
  dtostrf(h, 1, 2, humString);
  client.publish(humidity_topic, humString);

  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print("°C, Humidity: ");
  Serial.print(h);
  Serial.println("%");

  // Delay between readings
  delay(2000);  // Adjust delay as needed
}
```