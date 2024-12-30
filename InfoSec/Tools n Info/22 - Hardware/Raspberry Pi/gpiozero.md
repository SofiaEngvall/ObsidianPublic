

![[Images/input_device_hierarchy.svg]]
*Input devices* - https://gpiozero.readthedocs.io/en/stable/source_values.html

![[Images/output_device_hierarchy.svg]]
*Output devices* - https://gpiozero.readthedocs.io/en/latest/api_output.html


```python
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

```python
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(3)

button.when_pressed = led.on
button.when_released = led.off

pause()
```

```python
from gpiozero import OutputDevice, MotionSensor, LightSensor
from gpiozero.tools import booleanized, all_values
from signal import pause

garden = OutputDevice(17)
motion = MotionSensor(4)
light = LightSensor(5)

garden.source = all_values(booleanized(light, 0, 0.1), motion)

pause()
```

