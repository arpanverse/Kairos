from pydantic import BaseModel, Field
from typing import List

class BusinessOffer(BaseModel):
    """Schema for a business offer"""
    business_id: str
    business_name: str
    offer_text: str
    category: str = "general"

class MatchRequest(BaseModel):
    """Schema for match request"""
    business_id: str
    need_text: str = Field(..., description="What the business needs")
    top_k: int = Field(default=5, ge=1, le=20)

class MatchResult(BaseModel):
    """Schema for a single match result"""
    business_id: str
    business_name: str
    offer_text: str
    category: str
    similarity_score: float
    confidence: str

class MatchResponse(BaseModel):
    """Schema for match response"""
    query: str
    matches: List[MatchResult]
    total_found: int