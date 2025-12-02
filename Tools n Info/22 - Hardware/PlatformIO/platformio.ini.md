

[env:esp32dev]
platform = https://github.com/pioarduino/platform-espressif32/releases/download/stable/platform-espressif32.zip
board = esp32dev
framework = arduino


upload_port = COM9
monitor_speed = 9600
monitor_filters = esp32_exception_decoder


lib_deps = 
	https://github.com/pschatzmann/ESP32-A2DP.git
	https://github.com/pschatzmann/arduino-audio-tools.git


???
board_build.partitions = huge_app.csv