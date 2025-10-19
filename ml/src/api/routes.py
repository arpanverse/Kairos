from fastapi import APIRouter, HTTPException
from typing import List
from ..agents.matching_agent import MatchingAgent
from .schemas import MatchRequest, MatchResponse, BusinessOffer, MatchResult

# Initialize router
router = APIRouter(prefix="/api/v1", tags=["matching"])

# Global agent instance
matching_agent = MatchingAgent()

@router.post("/index/build")
async def build_index(offers: List[BusinessOffer]):
    """
    Build the matching index from business offers
    """
    try:
        offer_dicts = [offer.model_dump() for offer in offers]
        matching_agent.build_index(offer_dicts)
        return {
            "status": "success",
            "message": f"Index built with {len(offers)} offers"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/match", response_model=MatchResponse)
async def find_matches(request: MatchRequest):
    """
    Find matching offers for a business need
    """
    try:
        matches = matching_agent.find_matches(
            need_text=request.need_text,
            business_id=request.business_id,
            top_k=request.top_k
        )
        
        return MatchResponse(
            query=request.need_text,
            matches=[MatchResult(**match) for match in matches],
            total_found=len(matches)
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "agent": "MatchingAgent",
        "model": "all-MiniLM-L6-v2"
    }