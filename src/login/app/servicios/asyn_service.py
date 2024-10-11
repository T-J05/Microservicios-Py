import asyncio
import json
from nats.aio.client import Client as NATS
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

async def procesar_evento(msg):
    evento = json.loads(msg.data.decode())
    logging.info(f"Evento recibido: {evento}")

async def suscribir_eventos():
    nc = NATS()


    await nc.connect("nats://localhost:4222")

    await nc.subscribe("eventos_buses", cb=procesar_evento)


    await asyncio.sleep(3600)  

