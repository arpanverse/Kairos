# Kairos ML - AI Agents for B2B Barter Platform

## Setup

### 1. Create Conda Environment
```bash
cd ml
conda env create -f envWindows.yml
conda activate kairos
```

### 2. Run the API
```bash
python -m src.app
```

The API will be available at `http://localhost:8000`

### 3. Test the Matching Agent
```bash
cd tests
python test_matching_agent.py
```

## API Endpoints

### Build Index
```bash
POST /api/v1/index/build
```

### Find Matches
```bash
POST /api/v1/match
```

### Health Check
```bash
GET /api/v1/health
```

## Example Usage

```python
import requests

# Build index
offers = [
    {
        "business_id": "cafe_001",
        "business_name": "Green Leaf Cafe",
        "offer_text": "Catering services for events",
        "category": "food"
    }
]
requests.post("http://localhost:8000/api/v1/index/build", json=offers)

# Find matches
response = requests.post("http://localhost:8000/api/v1/match", json={
    "business_id": "startup_001",
    "need_text": "I need catering for my office",
    "top_k": 5
})
print(response.json())
```

## Interactive API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`