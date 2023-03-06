import random
import time
import paho.mqtt.client as mqtt

# Credenciales de conexión
host = "myinstance-security.cloud.shiftr.io"
port = 1883
username = "myinstance-security"
password = "SygyutF8JyLDfz5D"

# Temas MQTT
temp_topic = "security/temperature"

# Función de conexión con shiftr.io
def on_connect(client, userdata, flags, rc):
    print("Conectado a shiftr.io con código de resultado: "+str(rc))

# Conexión con shiftr.io
client = mqtt.Client()
client.username_pw_set(username, password)
client.on_connect = on_connect
client.connect(host, port, 60)

# Bucle principal
while True:
    # Generar valores aleatorios de temperatura
    temperatura = random.uniform(18, 25)
    # Publicar los valores en los temas MQTT correspondientes
    client.publish(temp_topic, temperatura)
    # Esperar 5 segundos antes de la siguiente lectura
    time.sleep(5)