"""
Cloud Referee - AWS Bedrock vs OpenAI API Comparison Tool
A tool that compares options and explains trade-offs, instead of giving a single answer.
"""

from referee import CloudReferee

def get_user_input():
    """Get user constraints for comparison"""
    print("\n" + "="*60)
    print("☁️  CLOUD REFEREE - AWS Bedrock vs OpenAI API")
    print("="*60)
    print("\nEnter your constraints to get a personalized comparison:\n")
    
    budget = input("Budget (low/medium/high): ").strip().lower()
    data_privacy = input("Data Privacy requirement (low/high): ").strip().lower()
    scalability = input("Scalability needs (low/high): ").strip().lower()
    vendor_lockin = input("Vendor lock-in tolerance (low/high): ").strip().lower()
    
    return {
        "budget": budget if budget in ["low", "medium", "high"] else "medium",
        "data_privacy": data_privacy if data_privacy in ["low", "high"] else "low",
        "scalability": scalability if scalability in ["low", "high"] else "low",
        "vendor_lockin_tolerance": vendor_lockin if vendor_lockin in ["low", "high"] else "low"
    }

def main():
    """Main application entry point"""
    constraints = get_user_input()
    
    referee = CloudReferee()
    result = referee.compare(constraints)
    
    print("\n" + "="*60)
    print("📊 COMPARISON RESULTS")
    print("="*60)
    
    print("\n🔷 AWS BEDROCK")
    print("  ✅ Pros:")
    for pro in result["aws_bedrock"]["pros"]:
        print(f"     • {pro}")
    print("  ❌ Cons:")
    for con in result["aws_bedrock"]["cons"]:
        print(f"     • {con}")
    
    print("\n🔶 OPENAI API")
    print("  ✅ Pros:")
    for pro in result["openai_api"]["pros"]:
        print(f"     • {pro}")
    print("  ❌ Cons:")
    for con in result["openai_api"]["cons"]:
        print(f"     • {con}")
    
    print("\n" + "="*60)
    print("⚖️  VERDICT (Trade-off Based)")
    print("="*60)
    print(f"\n{result['verdict']}")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()
