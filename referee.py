"""
Cloud Referee Module
Core comparison logic - compares AWS Bedrock vs OpenAI API based on constraints
"""

class CloudReferee:
    """
    A referee tool that compares cloud AI services and explains trade-offs.
    Does NOT give a single answer - provides conditional recommendations.
    """
    
    def __init__(self):
        self.services = {
            "aws_bedrock": {
                "name": "AWS Bedrock",
                "features": {
                    "data_privacy": "high",
                    "aws_integration": True,
                    "model_variety": True,
                    "pay_per_use": True,
                    "enterprise_ready": True
                }
            },
            "openai_api": {
                "name": "OpenAI API",
                "features": {
                    "cutting_edge_models": True,
                    "easy_setup": True,
                    "large_community": True,
                    "rapid_updates": True,
                    "simple_pricing": True
                }
            }
        }
    
    def compare(self, constraints: dict) -> dict:
        """
        Compare AWS Bedrock vs OpenAI API based on user constraints.
        Returns pros, cons, and a conditional verdict for both options.
        """
        budget = constraints.get("budget", "medium")
        data_privacy = constraints.get("data_privacy", "low")
        scalability = constraints.get("scalability", "low")
        vendor_lockin = constraints.get("vendor_lockin_tolerance", "low")
        
        # Build pros and cons based on constraints
        bedrock_pros = []
        bedrock_cons = []
        openai_pros = []
        openai_cons = []
        
        # Data Privacy Analysis
        if data_privacy == "high":
            bedrock_pros.append("Data stays within AWS infrastructure - better for compliance")
            bedrock_pros.append("VPC integration for isolated environments")
            openai_cons.append("Data sent to external OpenAI servers")
        else:
            openai_pros.append("Simple data handling for non-sensitive use cases")
        
        # Budget Analysis
        if budget == "low":
            openai_pros.append("Pay-as-you-go with predictable per-token pricing")
            openai_pros.append("Free tier available for experimentation")
            bedrock_cons.append("AWS infrastructure costs can add up")
        elif budget == "high":
            bedrock_pros.append("Enterprise pricing and committed use discounts")
            bedrock_pros.append("Consolidated billing with other AWS services")
        else:
            bedrock_pros.append("Flexible pricing with multiple model options")
            openai_pros.append("Transparent token-based pricing")
        
        # Scalability Analysis
        if scalability == "high":
            bedrock_pros.append("Seamless scaling with AWS infrastructure")
            bedrock_pros.append("Auto-scaling and load balancing built-in")
            openai_cons.append("Rate limits may require enterprise plan")
        else:
            openai_pros.append("Simple API sufficient for moderate workloads")
        
        # Vendor Lock-in Analysis
        if vendor_lockin == "low":
            openai_pros.append("Easier to switch - standard REST API")
            openai_pros.append("Model-agnostic integration possible")
            bedrock_cons.append("Tighter AWS ecosystem integration may increase dependency")
        else:
            bedrock_pros.append("Deep AWS integration benefits outweigh lock-in concerns")
            bedrock_pros.append("Access to multiple foundation models (Claude, Llama, etc.)")
        
        # Add general pros
        bedrock_pros.append("Access to multiple AI models (Claude, Llama, Titan, etc.)")
        bedrock_pros.append("Native AWS service integration (Lambda, S3, etc.)")
        openai_pros.append("Access to GPT-4 and latest OpenAI models")
        openai_pros.append("Extensive documentation and community support")
        openai_pros.append("Rapid model updates and improvements")
        
        # Build conditional verdict
        verdict = self._build_verdict(constraints)
        
        return {
            "aws_bedrock": {
                "pros": bedrock_pros,
                "cons": bedrock_cons if bedrock_cons else ["May require AWS expertise to fully utilize"]
            },
            "openai_api": {
                "pros": openai_pros,
                "cons": openai_cons if openai_cons else ["Limited to OpenAI's model ecosystem"]
            },
            "verdict": verdict
        }
    
    def _build_verdict(self, constraints: dict) -> str:
        """Build a conditional verdict - never a single absolute answer"""
        verdicts = []
        
        verdicts.append("🔷 Choose AWS BEDROCK if:")
        verdicts.append("   • You need high data privacy and compliance (HIPAA, SOC2)")
        verdicts.append("   • You're already in the AWS ecosystem")
        verdicts.append("   • You need access to multiple AI models (Claude, Llama, Titan)")
        verdicts.append("   • You require enterprise-grade scaling")
        
        verdicts.append("\n🔶 Choose OPENAI API if:")
        verdicts.append("   • You want fastest access to cutting-edge GPT models")
        verdicts.append("   • You prefer simple setup and integration")
        verdicts.append("   • You're building prototypes or MVPs quickly")
        verdicts.append("   • You want strong community support and resources")
        
        # Add constraint-specific recommendation
        if constraints.get("data_privacy") == "high":
            verdicts.append("\n⚠️ Based on your HIGH data privacy requirement:")
            verdicts.append("   → AWS Bedrock is STRONGLY recommended")
        
        if constraints.get("budget") == "low" and constraints.get("scalability") == "low":
            verdicts.append("\n⚠️ Based on your LOW budget + LOW scalability:")
            verdicts.append("   → OpenAI API may be more cost-effective for starting out")
        
        return "\n".join(verdicts)
