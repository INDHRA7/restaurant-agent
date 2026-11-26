from fastapi import FastAPI

from backend.app.api.v1.routes.booking import router as booking_router

app = FastAPI()
app.include_router(booking_router , prefix = "/api/v1")

@app.get("/")
def book():
    return "your mother fucker I am back :)"
@app.get("/health")
def health():
    health_status = {
        "status" : "running" ,
        "message" : "hello world !",
        "service" : "restaurant-agent"
    }
    return health_status


