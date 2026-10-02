
`upower -i $(upower -e | grep 'BAT')`

```sh
┌──(fixit42㉿x1)-[~/Downloads/obs-git/obs-studio]
└─$ upower -i $(upower -e | grep 'BAT')
  native-path:          BAT0
  vendor:               SMP
  model:                01AV430
  serial:               949
  power supply:         yes
  updated:              Thu 01 Oct 2026 07:23:34 PM CEST (8 seconds ago)
  has history:          yes
  has statistics:       yes
  battery
    present:             yes
    rechargeable:        yes
    state:               pending-charge
    warning-level:       none
    energy:              37.46 Wh
    energy-empty:        0 Wh
    energy-full:         42.49 Wh
    energy-full-design:  57.02 Wh
    voltage-min-design:  11.52 V
    capacity-level:      Normal
    energy-rate:         0 W
    voltage:             12.813 V
    charge-cycles:       73
    percentage:          88%
    capacity:            74.5177%
    technology:          lithium-polymer
    charge-start-threshold:        75%
    charge-end-threshold:          80%
    charge-threshold-supported:    yes
    icon-name:          'battery-full-charging-symbolic'
  History (voltage):
    1790875414  12.813  pending-charge
    1790875411  12.778  pending-charge
    1790875382  12.813  pending-charge
    1790875379  12.778  pending-charge
    1790875357  12.793  pending-charge
    1790875355  12.777  pending-charge
    1790875353  12.779  pending-charge
    1790875323  12.819  pending-charge
    1790875321  12.777  pending-charge



┌──(fixit42㉿x1)-[~/Downloads/obs-git/obs-studio]
└─$ upower -e                          
/org/freedesktop/UPower/devices/battery_BAT0
/org/freedesktop/UPower/devices/line_power_AC
/org/freedesktop/UPower/devices/line_power_ucsi_source_psy_USBC000o001
/org/freedesktop/UPower/devices/line_power_ucsi_source_psy_USBC000o002
/org/freedesktop/UPower/devices/DisplayDevice


┌──(fixit42㉿x1)-[~/Downloads/obs-git/obs-studio]
└─$ upower -i /org/freedesktop/UPower/devices/battery_BAT0
  native-path:          BAT0
  vendor:               SMP
  model:                01AV430
  serial:               949
  power supply:         yes
  updated:              Fri 02 Oct 2026 12:54:46 PM CEST (23 seconds ago)
  has history:          yes
  has statistics:       yes
  battery
    present:             yes
    rechargeable:        yes
    state:               discharging
    warning-level:       low
    energy:              6.39 Wh
    energy-empty:        0 Wh
    energy-full:         42.49 Wh
    energy-full-design:  57.02 Wh
    voltage-min-design:  11.52 V
    capacity-level:      Normal
    energy-rate:         5.927 W
    voltage:             10.623 V
    charge-cycles:       73
    time to empty:       1.1 hours
    percentage:          15%
    capacity:            74.5177%
    technology:          lithium-polymer
    charge-start-threshold:        75%
    charge-end-threshold:          80%
    charge-threshold-supported:    yes
    icon-name:          'battery-caution-symbolic'
  History (charge):
    1790938426  15.000  discharging
  History (rate):
    1790938486  5.927   discharging
    1790938456  7.800   discharging
    1790938426  10.203  discharging
    1790938396  14.923  discharging
  History (voltage):
    1790938486  10.623  discharging
    1790938456  10.599  discharging
    1790938426  10.275  discharging
    1790938396  9.697   discharging


┌──(fixit42㉿x1)-[~/Downloads/obs-git/obs-studio]
└─$ cat /sys/class/power_supply/BAT0/charge_control_start_threshold
cat /sys/class/power_supply/BAT0/charge_control_end_threshold

0
100


┌──(fixit42㉿x1)-[~/Downloads/obs-git/obs-studio]
└─$ sudo nano /etc/tlp.conf

[sudo] password for fixit42: 
```