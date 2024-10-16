import win32com.client


def list_paired_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    bluetooth_devices = wmi.ExecQuery(
        "SELECT * FROM Win32_PnPEntity")  # WHERE Name LIKE '%Bluetooth%'")

    print("----------------------------------------------")
    print("- All bluetoth devices                       -")
    print("----------------------------------------------")

    for device in bluetooth_devices:
        if device.DeviceID.startswith("BTHENUM"):
            print("  Name: {}, Device ID: {}".format(
                device.Name, device.DeviceID))


def list_all_bluetooth_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    bluetooth_devices = wmi.ExecQuery(
        "SELECT * FROM Win32_PnPEntity")  # WHERE Name LIKE '%Bluetooth%'")

    print("----------------------------------------------")
    print("- All devices                                -")
    print("----------------------------------------------")

    for device in bluetooth_devices:
        print("  Name: {}, Device ID: {}".format(device.Name, device.DeviceID))


def list_com_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    bluetooth_devices = wmi.ExecQuery(
        "SELECT * FROM Win32_PnPEntity WHERE Name LIKE '%(COM%'")

    print("----------------------------------------------")
    print("- All COM port devices                       -")
    print("----------------------------------------------")

    for device in bluetooth_devices:
        print("  Name: {}, Device ID: {}".format(device.Name, device.DeviceID))


def list_serial_port_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    serial_port_devices = wmi.ExecQuery("SELECT * FROM Win32_SerialPort")

    print("----------------------------------------------")
    print("- Serial Port devices                        -")
    print("----------------------------------------------")

    for device in serial_port_devices:
        print("  Name: {}, Description: {}, Device ID: {}".format(
            device.Name, device.Description, device.DeviceID))


if __name__ == "__main__":
    # list_all_bluetooth_devices()
    # list_paired_devices()
    # list_com_devices()
    list_serial_port_devices()
