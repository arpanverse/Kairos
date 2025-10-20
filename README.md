# Kairos - AI-Powered B2B Barter Platform

**Tagline**: Smart, Scalable, Trust-Based Business Exchange

## 🎯 The Problem

Traditional barter systems suffer from three critical defects:
1. **Lack of Double Coincidence of Wants** - Hard to find matching needs
2. **No Common Measure of Value** - Difficult to determine fair exchanges
3. **Contract Complexity** - Expensive legal overhead and trust issues

## 💡 Our Solution

Kairos leverages **Agentic AI** and **Fintech** to solve these problems:

- 🤖 **AI Matching Agent** - Semantic search to find perfect business matches
- 💰 **AI Valuation Agent** - Fair trade credit valuation using market data
- 📝 **AI Contract Agent** - Automated smart contract generation
- 🔄 **Trade Credit System** - Internal currency enabling multi-party trades

## 🏗️ Project Structure

```
kairos/
├── ml/                    # Machine Learning API
│   ├── src/
│   │   ├── agents/       # AI Agents (Matching, Valuation, Contract)
│   │   ├── api/          # FastAPI routes and schemas
│   │   └── app.py        # Main application
│   ├── tests/            # Unit tests
│   └── data/             # Sample/training data
├── frontend/             # (Coming soon) React/Next.js UI
└── docs/                 # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Conda (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/arpanverse/Kairos.git
cd kairos

# Navigate to ML directory
cd ml

# Create conda environment
conda env create -f envWindows.yml
conda activate kairos
pip install -r requirements.txt
```

### Run the API

```bash
# From the ml/ directory
python -m src.app
```

Visit `http://localhost:8000/docs` for interactive API documentation.

## 📊 Current Features

### ✅ Matching Agent (v0.1)
- Semantic similarity search using Sentence Transformers
- FAISS vector indexing for fast retrieval
- Confidence scoring (high/medium/low)
- Category-based filtering

### 🔜 Coming Soon
- **Valuation Agent** - AI-powered trade credit valuation
- **Contract Generation Agent** - Smart contract automation
- **Multi-party Trade Support** - A→B→C→A circular trades
- **Reputation System** - Trust scores and reviews
- **Blockchain Integration** - Immutable contract records

## 🧪 Testing

```bash
# Test the matching agent
cd ml/tests
python test_matching_agent.py
```

## 📖 API Documentation

### Build Index
```http
POST /api/v1/index/build
Content-Type: application/json

[
  {
    "business_id": "cafe_001",
    "business_name": "Green Leaf Cafe",
    "offer_text": "Catering services for corporate events",
    "category": "food"
  }
]
```

### Find Matches
```http
POST /api/v1/match
Content-Type: application/json

{
  "business_id": "startup_001",
  "need_text": "I need catering for my office",
  "top_k": 5
}
```

### Response
```json
{
  "query": "I need catering for my office",
  "matches": [
    {
      "business_id": "cafe_001",
      "business_name": "Green Leaf Cafe",
      "offer_text": "Catering services for corporate events",
      "category": "food",
      "similarity_score": 0.724,
      "confidence": "high"
    }
  ],
  "total_found": 1
}
```

## 🏆 Hackathon Impact

### Financial Benefits
- **Cash Flow Optimization** - Trade excess capacity instead of cash
- **Asset Utilization** - Convert unused inventory/services to value
- **Market Expansion** - Access new customers through barter
- **Improved Margins** - Cost of goods < retail value received

### Technical Innovation
- **Agentic AI** - Autonomous agents for matching, valuation, and contracts
- **Fintech Integration** - Trade credit system as financial instrument
- **Trust Mechanism** - Milestone-based escrow and smart contracts