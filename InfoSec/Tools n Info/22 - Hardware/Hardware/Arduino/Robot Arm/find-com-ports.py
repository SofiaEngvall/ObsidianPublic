import win32com.client


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
    list_serial_port_devices()
