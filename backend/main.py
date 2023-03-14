import os

import uvicorn
from api.app import app

if __name__ == "__main__":
    # Ejecutamos el servidor de desarrollo de FastAPI con Uvicorn
    uvicorn.run(app)  # , host="1313", port=80)
