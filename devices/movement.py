from sensor import Sensor
import random

def main():
    temp_sensor = Sensor(topic="movement", output_function=random.choice([True, False]))
    temp_sensor.connect()
    temp_sensor.run()

if __name__ == "__main__":
    main()
