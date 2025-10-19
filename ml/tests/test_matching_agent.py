import sys
sys.path.append('..')

from src.agents.matching_agent import MatchingAgent

def test_matching_agent():
    """Test the matching agent with sample data"""
    
    # Sample business offers
    sample_offers = [
        {
            "business_id": "cafe_001",
            "business_name": "Green Leaf Cafe",
            "offer_text": "Catering services for corporate events, parties, and meetings",
            "category": "food"
        },
        {
            "business_id": "ad_agency_001",
            "business_name": "Digital Buzz Marketing",
            "offer_text": "Social media advertising, Google Ads, and content marketing",
            "category": "marketing"
        },
        {
            "business_id": "cowork_001",
            "business_name": "Innovation Hub",
            "offer_text": "Coworking space, meeting rooms, and event venue rental",
            "category": "workspace"
        },
        {
            "business_id": "print_001",
            "business_name": "PrintPro Services",
            "offer_text": "Business cards, flyers, banners, and promotional materials",
            "category": "printing"
        }
    ]
    
    # Initialize agent
    agent = MatchingAgent()
    
    # Build index
    print("Building index...")
    agent.build_index(sample_offers)
    
    # Test queries
    test_queries = [
        ("cafe_002", "I need food catering for my office events"),
        ("startup_001", "Looking for advertising and marketing services"),
        ("event_001", "Need a venue space for hosting workshops")
    ]
    
    print("\n" + "="*60)
    for business_id, query in test_queries:
        print(f"\n🔍 Query: '{query}'")
        print(f"   From: {business_id}")
        print("-" * 60)
        
        matches = agent.find_matches(query, business_id, top_k=3)
        
        for i, match in enumerate(matches, 1):
            print(f"\n{i}. {match['business_name']} ({match['confidence'].upper()})")
            print(f"   Score: {match['similarity_score']:.3f}")
            print(f"   Offer: {match['offer_text']}")
    
    print("\n" + "="*60)
    print("✅ Test completed successfully!")

if __name__ == "__main__":
    test_matching_agent()