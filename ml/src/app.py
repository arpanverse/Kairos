from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router

# Create FastAPI app
app = FastAPI(
    title="Kairos ML API",
    description="AI Agents for B2B Barter Platform",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Kairos ML API",
        "docs": "/docs",
        "health": "/api/v1/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)