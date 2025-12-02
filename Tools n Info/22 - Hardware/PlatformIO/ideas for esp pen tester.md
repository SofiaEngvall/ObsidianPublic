
```cpp
String mainMenu[] = {
  "Wi-Fi Deauth",          // Mass deauthentication attacks
  "BLE Recon",             // Bluetooth device discovery
  "Bad USB",               // HID injection attacks
  "RFID Cloner",           // 125kHz/13.56MHz reading
  "Packet Sniffer",        // Network traffic capture
  "Signal Jammer",         // RF disruption tests
  "Physical Triggers",     // GPIO-based automation
  "Credential Harvest",    // Fake AP with captive portal
  "Hardware Debug",        // UART/JTAG discovery
  "Settings"
};
```
also have eula in menu talking about ethical use only

**1. Wi-Fi Attacks**

```cpp
// Wi-Fi menu options
String wifiAttacks[] = {
  "Deauth Attack",       // Mass deauthentication
  "Beacon Flood",        // Fake AP spam
  "Probe Request Flood", 
  "AP Reconnaissance",   // Network discovery
  "Evil Twin",           // Rogue AP setup
  "WPS Pixie Dust",      // WPS attacks
  "Captive Portal",      // Fake login page
  "PMKID Harvest",       // WPA3 handshake capture
  "Back"
};
```

**2. Bluetooth/BLE Attacks**

```cpp
String bleAttacks[] = {
  "BLE Device Scan",     // Discover devices
  "GATT Exploration",    // Service enumeration
  "Spoofing Attacks",    // Impersonate devices
  "Jammer Test",         // Interference testing
  "Beacon Spoofing",     // iBeacon/Eddystone
  "Back"
};
```

**3. Hardware Attacks**

```cpp
String hardwareAttacks[] = {
  "UART Discovery",      // Find debug consoles
  "JTAG Detection",      // Test for debug ports
  "GPIO Bruteforce",     // Pin enumeration
  "Power Analysis",      // Simple side-channel
  "Signal Injection",    // GPIO pulse attacks
  "Back"
};
```

**4. Social Engineering**

```cpp
String socialEngineering[] = {
  "BadUSB Attacks",      // Keyboard injection
  "QR Code Generator",   // Malicious QR codes
  "Fake Update Screen",  // Psychological attack
  "Back"
};
```

Suggested **Hardware Add-ons (Inexpensive)**

- **NRF24L01+** ($2) → 2.4GHz attacks
- **RC522 RFID** ($3) → RFID cloning
- **433/315MHz TX/RX** ($4) → RF attacks
- **IR transmitter** ($1) → Infrared attacks
- **SD card** ($5) → Data logging

data save methods

- Wi-Fi Direct to attacker machine
- BLE data transfer to phone
- SD card storage for physical extraction

advanced Features

String advancedFeatures[] = {
  "Attack Scheduler",    // Timed attacks
  "Macro Recorder",      // Record/replay sequences
  "Signal Analysis",     // Basic RF analysis
  "Pattern Generation",  // Custom signal patterns
  "Firmware Flasher",    // Device reprogramming
  "Back"
};

pins left

GPIO 12-14, 25-27, 32-39 → Free for attack modules
GPIO 34-39 → Input only (good for sensing)
GPIO 25,26 → DAC outputs (signal generation)
GPIO 32,33 → Touch capable (covert triggers)

suggested ## **Implementation Priority**
1. **Wi-Fi deauthentication** (most impactful)
2. **BLE reconnaissance** (quick wins)
3. **BadUSB functionality** (physical access)
4. **UART discovery** (hardware hacking)
5. **Captive portal** (credential harvesting)


blue tools?
String defenseTools[] = {
  "Network Monitor",     // Detect attacks
  "Device Hardening",    // Security checklist
  "Signal Detection",    // RF attack detection
  "Integrity Checker",   // System verification
  "Back"
};

---

previous lists

- **Wi-Fi Sniffer & Packet Analyzer** – Capture and analyze Wi-Fi packets, detect nearby networks, and learn about WPA/WPA2 handshakes.
    
- **Bluetooth Low Energy (BLE) Scanner** – Scan and log BLE devices around you, track advertising packets, or experiment with device fingerprinting.
    
- **Rogue Access Point** – Set up a fake AP for testing purposes in a lab, to study client behavior and network security awareness.
    
- **Keylogger Emulator (USB HID)** – Use the ESP32 as a USB keyboard/mouse to simulate input and study security of unattended machines in a controlled environment.
    
- **RFID/NFC Reader & Emulator** – Explore RFID security and emulate cards for research on access control systems.
    
- **IoT Honeypot** – Emulate vulnerable devices to study attack patterns and learn IoT defense techniques.
    
- **Network Traffic Logger** – Monitor and log traffic in your own network using ESP32 as a tiny sniffing device.
    
- **Pen-testing Tool Controller** – Control small pen-testing gadgets remotely via ESP32 web interface or BLE.


**practical ESP32-WROOM projects** you could actually use in real-world physical pentests (with permission):

1. **Wi-Fi Deauthenticator / Jammer** – Test how resilient client devices are to deauthentication/disassociation attacks and observe failover behavior.
    
2. **Rogue AP / Evil Twin** – Spin up a fake AP with same SSID to capture credentials or force clients to connect, useful in red team scenarios.
    
3. **Wi-Fi Handshake Capture Tool** – Passive sniffer for WPA/WPA2 handshakes, later crack offline with tools like hashcat.
    
4. **Beacon Flooder** – Spam multiple SSIDs to test wireless monitoring/defense tools and SOC alerting.
    
5. **BLE Scanner & Impersonator** – Enumerate nearby Bluetooth devices and emulate them to test pairing security.
    
6. **BadUSB Emulator** – Program the ESP32 as a malicious keyboard to deliver payloads on unlocked endpoints (similar to Rubber Ducky).
    
7. **Credential Harvester via Captive Portal** – Combine rogue AP with a fake login portal to test user security awareness.
    
8. **Portable DoS / Stress Test Device** – Controlled test of device robustness against malformed Wi-Fi/BLE packets.


**Core Functions**

- **Wi-Fi Deauthenticator** – Select target AP/clients from the menu and launch controlled deauth.
    
- **Rogue AP / Evil Twin + Captive Portal** – Start a fake AP with optional phishing login page.
    
- **Handshake Capture** – Put the ESP32 into sniffing mode to collect WPA/WPA2 handshakes for later cracking.
    
- **Beacon Flooder** – Generate multiple SSIDs (configurable from menu) for stress testing detection/monitoring tools.
    
- **BLE Scanner** – Show nearby BLE devices, MACs, and signal strength on the LCD.
    
- **BLE Impersonation / Replay** – Try to impersonate a scanned BLE device (e.g., to test insecure pairing).
    

**Extra Add-ons That Fit Well**

- **Simple Packet Monitor / Logger** – Store traffic metadata (SSID, BSSID, RSSI, channel) on SD card for post-analysis.
    
- **IoT Honeypot Mode** – Fake an insecure IoT device (e.g., HTTP service with default creds) to see who probes it.
    
- **Field Notes Storage** – Small onboard logbook where you save targets, captured SSIDs, or BLE IDs.


ESP32 Marauder provides Wi-Fi and Bluetooth analysis, frame capture, device enumeration, and transmission capabilities [GitHub](https://github.com/justcallmekoko/ESP32Marauder/wiki/faq?utm_source=chatgpt.com). The v6 hardware adds GPS, dual SMA antenna, SD-card PCAP storage, LiPo charging, a touch TFT display, and a robust enclosure [JustCallMeKoko LLC](https://justcallmekokollc.com/products/esp32-marauder-v6?utm_source=chatgpt.com). There’s also a more compact “Mini” version with tactile input instead of touch, and CLI control via PC/phone [JustCallMeKoko LLC](https://justcallmekokollc.com/products/marauder-mini?utm_source=chatgpt.com).

hw
Rotary encoder + clickable knob? or buttons only (fake worm game)
RFID/NFC??

Wi-Fi deauth/jammer, rogue APs, beacon flood, handshake capture, Evil Portal
BLE scanning, spoofing, fuzzing, dynamic payload injection
PCAP, GPS tagging for wardriving

Wi-Fi deauth, handshake capture, rogue AP/Evil Twin with customizable captive portal.
Beacon flooder, PMKID harvest, probe scanning.
BLE: BLE scanner, fuzzer, impersonator; handshake replay.

├── Wi-Fi
│   ├─ Scan & Capture
│   ├─ Deauthify (select AP/client)
│   ├─ Rogue AP + Portal
│   └─ Beacon Flooder
├── BLE
│   ├─ Scan Devices
│   ├─ Impersonate Device
│   └─ Fuzz / Replay


