from typing import List, Dict
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class MatchingAgent:
    """
    AI Agent that matches business needs with available offers using semantic similarity.
    Automatically uses GPU acceleration if available.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", use_gpu: bool = True):
        """
        Initialize the matching agent with a sentence transformer model.
        
        Args:
            model_name: HuggingFace model for embeddings
            use_gpu: Whether to use GPU acceleration if available
        """
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.business_offers: List[Dict] = []
        self.use_gpu = use_gpu and faiss.get_num_gpus() > 0
        self.gpu_resources = None
        
        if self.use_gpu:
            self.gpu_resources = faiss.StandardGpuResources()
            print(f"✅ GPU acceleration enabled ({faiss.get_num_gpus()} GPU(s) detected)")
        else:
            print("ℹ️  Running on CPU (no GPU detected or GPU disabled)")

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
        
        # Create CPU index first
        cpu_index = faiss.IndexFlatIP(dimension)
        cpu_index.add(embeddings)
        
        # Transfer to GPU if available
        if self.use_gpu:
            try:
                self.index = faiss.index_cpu_to_gpu(self.gpu_resources, 0, cpu_index)
                print(f"✅ Index built with {len(offers)} offers (GPU-accelerated)")
            except Exception as e:
                print(f"⚠️  GPU transfer failed: {e}. Falling back to CPU.")
                self.index = cpu_index
                self.use_gpu = False
        else:
            self.index = cpu_index
            print(f"✅ Index built with {len(offers)} offers (CPU)")

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
        for idx, score in zip(indices[0], distances[0]):
            offer = self.business_offers[idx]
            if offer["business_id"] == business_id:
                continue

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
        """Convert similarity score to confidence level"""
        if score > 0.7:
            return "high"
        if score > 0.5:
            return "medium"
        return "low"
    
    def get_status(self) -> Dict:
        """Get agent status and hardware info"""
        return {
            "model": self.model._model_card_data.model_name if hasattr(self.model, '_model_card_data') else "all-MiniLM-L6-v2",
            "hardware": "GPU" if self.use_gpu else "CPU",
            "num_gpus": faiss.get_num_gpus() if self.use_gpu else 0,
            "index_size": len(self.business_offers) if self.business_offers else 0
        }