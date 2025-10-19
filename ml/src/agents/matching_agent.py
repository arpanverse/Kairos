from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class MatchingAgent:
    """
    AI Agent that matches business needs with available offers using semantic similarity.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initialize the matching agent with a sentence transformer model.
        """
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.business_offers: List[Dict] = []

    def build_index(self, offers: List[Dict]):
        """
        Build FAISS index from business offers.

        Args:
            offers: List of dicts with 'business_id', 'offer_text', 'category'
        """
        if not offers:
            raise ValueError("Offers list is empty.")

        self.business_offers = offers

        offer_texts = [offer["offer_text"] for offer in offers]
        embeddings = self.model.encode(offer_texts, convert_to_numpy=True)

        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings)

        # Build FAISS index (Inner Product used as cosine similarity on normalized vectors)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

    def find_matches(self, need_text: str, business_id: str, top_k: int = 5) -> List[Dict]:
        """
        Find top matching offers for a given need.

        Args:
            need_text: The requesting business need text.
            business_id: ID of the requesting business.
            top_k: Number of matches to return.

        Returns:
            List of matched offers with scores and confidence.
        """
        if self.index is None:
            raise ValueError("Index not built. Call build_index() first.")

        need_embedding = self.model.encode([need_text], convert_to_numpy=True)
        faiss.normalize_L2(need_embedding)

        # Search for more than needed to account for self-matches
        search_k = min(top_k + 5, len(self.business_offers))
        distances, indices = self.index.search(need_embedding, search_k)

        matches: List[Dict] = []
        seen_business_ids = set()  # Track unique businesses
        
        for idx, score in zip(indices[0], distances[0]):
            # Skip invalid FAISS results (padding)
            if score < -1e10:
                continue
                
            offer = self.business_offers[idx]
            
            # Skip if it's the same business or already added
            if offer["business_id"] == business_id or offer["business_id"] in seen_business_ids:
                continue
            
            seen_business_ids.add(offer["business_id"])
            
            matches.append({
                "business_id": offer["business_id"],
                "business_name": offer.get("business_name", "Unknown"),
                "offer_text": offer["offer_text"],
                "category": offer.get("category", "general"),
                "similarity_score": float(score),
                "confidence": self._score_to_confidence(float(score)),
            })

            if len(matches) >= top_k:
                break

        return matches

    def _score_to_confidence(self, score: float) -> str:
        if score > 0.7:
            return "high"
        if score > 0.5:
            return "medium"
        return "low"

