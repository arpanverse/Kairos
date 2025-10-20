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

## 🎬 API Demo

### Step 1: Start the Server

```bash
cd ml
python -m src.app
```

You should see:
```
✅ GPU acceleration enabled (1 GPU(s) detected)
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 2: Open Interactive Documentation

Visit `http://localhost:8000/docs` in your browser for Swagger UI.

### Step 3: Build the Index

**Endpoint:** `POST /api/v1/index/build`

Click "Try it out" and paste this sample data:

```json
[
  {
    "business_id": "cafe_001",
    "business_name": "Green Leaf Cafe",
    "offer_text": "Catering services for corporate events, parties, and meetings. Fresh, organic ingredients.",
    "category": "food"
  },
  {
    "business_id": "ad_agency_001",
    "business_name": "Digital Buzz Marketing",
    "offer_text": "Social media advertising, Google Ads, content marketing, and SEO services",
    "category": "marketing"
  },
  {
    "business_id": "cowork_001",
    "business_name": "Innovation Hub",
    "offer_text": "Coworking space rental, meeting rooms, event venue, and office amenities",
    "category": "workspace"
  },
  {
    "business_id": "print_001",
    "business_name": "PrintPro Services",
    "offer_text": "Business cards, flyers, banners, brochures, and promotional materials printing",
    "category": "printing"
  },
  {
    "business_id": "designer_001",
    "business_name": "Creative Designs Co",
    "offer_text": "Logo design, brand identity, website UI/UX design, and graphic design services",
    "category": "design"
  },
  {
    "business_id": "photo_001",
    "business_name": "Lens & Light Photography",
    "offer_text": "Professional photography for events, products, corporate headshots, and marketing",
    "category": "media"
  },
  {
    "business_id": "law_001",
    "business_name": "Smith & Associates Law",
    "offer_text": "Legal consulting, contract review, business formation, and compliance services",
    "category": "legal"
  },
  {
    "business_id": "web_001",
    "business_name": "CodeCraft Solutions",
    "offer_text": "Web development, mobile app development, API integration, and tech consulting",
    "category": "technology"
  }
]
```

**Expected Response:**
```json
{
  "status": "success",
  "message": "Index built with 8 offers"
}
```

### Step 4: Find Matches

**Endpoint:** `POST /api/v1/match`

Try these example queries:

#### Example 1: Looking for Catering
```json
{
  "business_id": "startup_001",
  "need_text": "I need catering for my office lunch meetings",
  "top_k": 3
}
```

**Expected Response:**
```json
{
  "query": "I need catering for my office lunch meetings",
  "matches": [
    {
      "business_id": "cafe_001",
      "business_name": "Green Leaf Cafe",
      "offer_text": "Catering services for corporate events, parties, and meetings. Fresh, organic ingredients.",
      "category": "food",
      "similarity_score": 0.724,
      "confidence": "high"
    }
  ],
  "total_found": 1
}
```

#### Example 2: Looking for Marketing
```json
{
  "business_id": "cafe_001",
  "need_text": "Need help with online advertising and social media presence",
  "top_k": 3
}
```

**Expected Response:**
```json
{
  "query": "Need help with online advertising and social media presence",
  "matches": [
    {
      "business_id": "ad_agency_001",
      "business_name": "Digital Buzz Marketing",
      "offer_text": "Social media advertising, Google Ads, content marketing, and SEO services",
      "category": "marketing",
      "similarity_score": 0.812,
      "confidence": "high"
    }
  ],
  "total_found": 1
}
```

#### Example 3: Looking for Design Services
```json
{
  "business_id": "startup_002",
  "need_text": "Looking for a professional logo and brand identity design",
  "top_k": 5
}
```

**Expected Response:**
```json
{
  "query": "Looking for a professional logo and brand identity design",
  "matches": [
    {
      "business_id": "designer_001",
      "business_name": "Creative Designs Co",
      "offer_text": "Logo design, brand identity, website UI/UX design, and graphic design services",
      "category": "design",
      "similarity_score": 0.789,
      "confidence": "high"
    },
    {
      "business_id": "print_001",
      "business_name": "PrintPro Services",
      "offer_text": "Business cards, flyers, banners, brochures, and promotional materials printing",
      "category": "printing",
      "similarity_score": 0.412,
      "confidence": "low"
    }
  ],
  "total_found": 2
}
```

#### Example 4: Looking for Event Space
```json
{
  "business_id": "event_org_001",
  "need_text": "Need a venue for hosting a product launch event",
  "top_k": 3
}
```

### Step 5: Check Health Status

**Endpoint:** `GET /api/v1/health`

**Expected Response:**
```json
{
  "status": "healthy",
  "agent": "MatchingAgent",
  "model": "all-MiniLM-L6-v2",
  "hardware": "GPU",
  "num_gpus": 1,
  "index_size": 8
}
```

## 🧪 Testing with cURL

If you prefer command line testing:

### Build Index
```bash
curl -X POST "http://localhost:8000/api/v1/index/build" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "business_id": "cafe_001",
      "business_name": "Green Leaf Cafe",
      "offer_text": "Catering services for corporate events",
      "category": "food"
    }
  ]'
```

### Find Matches
```bash
curl -X POST "http://localhost:8000/api/v1/match" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "startup_001",
    "need_text": "I need catering for my office",
    "top_k": 5
  }'
```

### Health Check
```bash
curl http://localhost:8000/api/v1/health
```

## 🐍 Python Client Example

```python
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

# Sample businesses
businesses = [
    {
        "business_id": "cafe_001",
        "business_name": "Green Leaf Cafe",
        "offer_text": "Catering services for events",
        "category": "food"
    },
    {
        "business_id": "ad_agency_001",
        "business_name": "Digital Buzz Marketing",
        "offer_text": "Social media and digital advertising",
        "category": "marketing"
    }
]

# 1. Build index
print("Building index...")
response = requests.post(f"{BASE_URL}/index/build", json=businesses)
print(json.dumps(response.json(), indent=2))

# 2. Find matches
print("\nFinding matches...")
match_request = {
    "business_id": "startup_001",
    "need_text": "I need marketing services",
    "top_k": 3
}
response = requests.post(f"{BASE_URL}/match", json=match_request)
matches = response.json()

print(f"\nQuery: {matches['query']}")
print(f"Found {matches['total_found']} matches:\n")

for i, match in enumerate(matches['matches'], 1):
    print(f"{i}. {match['business_name']} ({match['confidence'].upper()})")
    print(f"   Score: {match['similarity_score']:.3f}")
    print(f"   Category: {match['category']}")
    print(f"   Offer: {match['offer_text']}\n")

# 3. Check health
print("Checking API health...")
response = requests.get(f"{BASE_URL}/health")
print(json.dumps(response.json(), indent=2))
```

**Expected Output:**
```
Building index...
{
  "status": "success",
  "message": "Index built with 2 offers"
}

Finding matches...

Query: I need marketing services
Found 1 matches:

1. Digital Buzz Marketing (HIGH)
   Score: 0.856
   Category: marketing
   Offer: Social media and digital advertising

Checking API health...
{
  "status": "healthy",
  "agent": "MatchingAgent",
  "model": "all-MiniLM-L6-v2",
  "hardware": "GPU",
  "num_gpus": 1,
  "index_size": 2
}
```

## 📊 Understanding the Results

### Similarity Scores
- **> 0.7**: High confidence - Strong semantic match
- **0.5 - 0.7**: Medium confidence - Partial match
- **< 0.5**: Low confidence - Weak match

### Confidence Levels
The agent automatically categorizes matches:
- **HIGH**: Very relevant, recommended for trade
- **MEDIUM**: Somewhat relevant, worth exploring
- **LOW**: Marginally relevant, consider alternatives

## 🎯 Demo Scenarios

### Scenario 1: Restaurant ↔ Marketing Agency
```
Cafe needs: Digital marketing
Agency needs: Event catering
Result: Perfect mutual match!
```

### Scenario 2: Startup ↔ Designer ↔ Printer
```
Startup needs: Logo design
Designer needs: Business cards
Printer needs: Website development
Result: 3-way trade enabled by Trade Credits!
```