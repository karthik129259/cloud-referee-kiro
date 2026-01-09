# ☁️ Cloud Referee - AWS Bedrock vs OpenAI API

> A tool that **compares options and explains trade-offs**, instead of giving a single answer.

## 🎯 Problem

Developers often get one-sided answers when choosing AI platforms. This leads to poor architectural decisions because:
- Every project has different constraints
- There is no universally "best" tool
- Trade-offs matter more than rankings

## ✅ Solution

**Cloud Referee** compares AWS Bedrock and OpenAI API based on **your real constraints**:
- Budget (low/medium/high)
- Data Privacy (low/high)
- Scalability needs (low/high)
- Vendor lock-in tolerance (low/high)

Instead of saying "X is better", it explains:
- ✅ Pros of each option
- ❌ Cons of each option
- ⚖️ Conditional verdict: "Choose A if..., Choose B if..."

## 🛠️ How Kiro Helped

Kiro accelerated development by:
- **Prompt Design**: Helped craft the referee prompt logic
- **Code Generation**: Generated comparison logic structure
- **Debugging**: Identified edge cases in constraint handling
- **Refinement**: Improved output formatting

## 📁 Project Structure

```
cloud-referee-kiro/
├── app.py                    # Main application
├── referee.py                # Core comparison logic
├── prompts/
│   └── referee_prompt.txt    # Referee prompt template
├── .kiro/                    # Kiro session data
└── README.md
```

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/karthik129259/cloud-referee-kiro.git
cd cloud-referee-kiro

# Run the application
python app.py
```

## 📊 Example Output

```
☁️  CLOUD REFEREE - AWS Bedrock vs OpenAI API
============================================================

🔷 AWS BEDROCK
  ✅ Pros:
     • Data stays within AWS infrastructure
     • Access to multiple AI models (Claude, Llama, Titan)
  ❌ Cons:
     • May require AWS expertise

🔶 OPENAI API
  ✅ Pros:
     • Access to GPT-4 and latest models
     • Simple setup and integration
  ❌ Cons:
     • Data sent to external servers

⚖️  VERDICT
Choose AWS Bedrock if you need high data privacy...
Choose OpenAI API if you want fastest access to GPT models...
```

## 🏆 AI for Bharat - Kiro Week 6 Challenge

This project was built for **Kiro Week 6: The Referee** challenge.

**Challenge Goal**: Build a tool that compares options and explains trade-offs, helping users choose rather than just consume information.

## 📝 License

MIT
