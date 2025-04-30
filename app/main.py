from fastapi import FastAPI
from app.api.routes import setup_routes

app = FastAPI()

# Middleware can be added here if needed

setup_routes(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)