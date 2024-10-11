# runner.py

import sys
import os
import asyncio
from threading import Thread
from app import ccrear_app 
from app.servicios.asyn_service import suscribir_eventos  

app = ccrear_app()

def run_flask():
    app.run(host='0.0.0.0', port=5001, debug=False) 


def run_nats():
    asyncio.run(suscribir_eventos())

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)
    nats_thread = Thread(target=run_nats)

    flask_thread.start()
    nats_thread.start()

    flask_thread.join()
    nats_thread.join()
