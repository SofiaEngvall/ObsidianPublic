from flask import Flask, request, render_template
import serial
import time
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__),"templates"), static_folder=os.path.join(os.path.dirname(__file__),"static"))
directions = "bcdfloru"
ser = None

print("Template folder path:", app.template_folder)
print("Static folder path:", app.static_folder)

def init_serial():
    global ser
    ser = serial.Serial()
    ser.port = 'COM20'
    ser.baudrate = 9600
    ser.timeout = 60

@app.route("/")
def move_robot_arm():
    global ser

    degrees = request.args.get("degrees", 5, type=int)
    direction = request.args.get("direction")
    if (direction is not None) and (direction in directions) and (len(direction)==1):
        tries = 0
        while tries < 5:
            try:
                ser.open()
                ser.write(bytearray("%"+direction+"#"+str(degrees)+"&",'ascii'))
                ser.close()
                tries = 5
            except Exception as e:
                tries = tries + 1
                print(str(e))
                time.sleep(2)
    else:
        if direction is None:
            direction = "Please add ?direction=[bcdfloru]&ampdegrees=number to move the robot arm."
        else:
            direction = "The directions are b, c, d, f, l, o, r and u."

    match direction:
        case "b": return render_template("robot.html", feedback="Moving robot arm back " + str(degrees) + " degrees.")
        case "c": return render_template("robot.html", feedback="Closing robot arm grip " + str(degrees) + " degrees.")
        case "d": return render_template("robot.html", feedback="Moving robot arm down " + str(degrees) + " degrees.")
        case "f": return render_template("robot.html", feedback="Moving robot arm forward " + str(degrees) + " degrees.")
        case "l": return render_template("robot.html", feedback="Rotating robot arm " + str(degrees) + " degrees to the left.")
        case "o": return render_template("robot.html", feedback="Opening robot arm grip " + str(degrees) + " degrees.")
        case "r": return render_template("robot.html", feedback="Rotating robot arm " + str(degrees) + " degrees to the right.")
        case "u": return render_template("robot.html", feedback="Moving robot arm up " + str(degrees) + " degrees.")
        case _: return direction

if __name__ == "__main__":
    init_serial()
    time.sleep(6)
    app.run(debug=True)
