import asyncio
from bleak import BleakScanner, BleakClient, exc

MODEL_NBR_UUID = "2A24"


async def getModelNr(address):
    print("Attempting to read model number for device with address:", address)
    try:
        async with BleakClient(address) as client:
            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            print("Model Number: {0}".format("".join(map(chr, model_number))))
    except (asyncio.exceptions.CancelledError, exc.BleakDeviceNotFoundError, exc.BleakError, AttributeError) as e:
        # print("Error reading model number for device with address:", address)
        print("Exception:", e)
# bleak.exc.BleakDeviceNotFoundError: Device with address 1C:52:16:12:3A:D0 was not found.
# bleak.exc.BleakError: Could not get GATT services: Unreachable
# AttributeError: 'NoneType' object has no attribute 'bluetooth_address'


async def main():
    devices = await BleakScanner.discover()
    print("----------------------------------------------")
    print("- Discovered devices                         -")
    print("----------------------------------------------")

    for d in devices:
        print("d.name: ", d.name)
        print("d.address: ", d.address)

        if d.name == None:
            print("d.details: ", d.details)
            print("d.metadata: ", d.metadata)
            # print("d.rssi: ", d.rssi)
        await getModelNr(d.address)

        print("----------------------------------------------")

asyncio.run(main())
