# 🤖 Rule-Based Chatbot v1.0

A conversational AI chatbot built with pure **rule-based if-else logic** for the DecodeLabs AI Internship (Batch 2026) - **Project 1**.

## 📋 Overview

This chatbot demonstrates foundational AI concepts using decision trees and pattern matching instead of machine learning. It maintains an engaging personality with curated responses, knowledge about AI topics, and interactive features.

**Key Requirements:**
- ✅ Handle greetings and exit commands
- ✅ Use if-else logic for responses
- ✅ Run in a continuous loop
- ✅ Expanded vocabulary & personality

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+

### Installation
```bash
# Clone or navigate to the project directory
cd f:\RULEBASED\ CHATBOT

# Run the chatbot
python rule_based_chatbot.py
```

### First Interaction
```
🤖 Rule-Based Chatbot » Initializing Rule-Based Chatbot...
🤖 Rule-Based Chatbot » All systems operational. Hello, I'm your Rule-Based Chatbot! 👋
🤖 Rule-Based Chatbot » Type 'help' to see what I can do, or just start chatting!

👤 You » help
```

---

## 💬 Features & Capabilities

Type any of these to interact:

### 👋 Greetings
- `hello`, `hi`, `hey`, `howdy`, `good morning`
- **Bot replies:** Randomly selected greeting with personality

### 💬 Feelings Check
- `how are you?`, `how do you do?`
- `i am good`, `i feel great`, `feeling bad`, `stressed`
- **Bot replies:** Empathetic, contextual responses

### 😂 Entertainment
- `tell me a joke` → Humorous tech-related jokes
- `tell me a fact` → Interesting tech/AI facts

### 🌟 Motivation
- `motivate me`, `inspire me`, `give me a quote`
- **Bot replies:** Motivational quotes from industry leaders

### 🤖 AI Knowledge Base
- `machine learning`, `deep learning`, `neural network`
- `natural language processing`, `computer vision`
- `python`, `algorithm`, `data`
- **Bot replies:** In-depth explanations of AI concepts

### ⏰ Utilities
- `what time is it?` → Current date & time
- `calculate 25 * 4` → Math evaluations (supports +, -, *, /, **)
- `who are you?` → Bot introduction
- `help` → Full command menu

### 🚪 Exit
- `bye`, `goodbye`, `quit`, `exit`
- **Bot replies:** Farewell message + session ends

### ❓ Special Queries
- `repeat that` → Clarification
- `meaning of life` → Easter egg (42! 😄)
- `favorite language`, `favorite color`, `favorite movie` → Bot preferences
- `who made you?` → DecodeLabs & Internship info

---

## 🏗️ Project Structure

```
f:\RULEBASED CHATBOT\
├── rule_based_chatbot.py    # Main chatbot engine
├── bot.py                   # Alternative bot implementation
├── chatbot.py               # Legacy chatbot module
├── run_chatbot.py           # Alternative runner
├── intents.json             # Intent definitions (optional)
├── tests/
│   └── test_bot.py          # Unit tests
└── README.md                # This file
```

---

## 🔧 How It Works

### Core Architecture

1. **Input Normalization** (`normalize()`)
   - Converts user input to lowercase
   - Strips punctuation
   - Preserves alphanumeric characters

2. **Pattern Matching** (`contains_any()`)
   - Checks if keywords exist in normalized text
   - Single-word keywords use word-boundary regex (avoid "yo" matching inside "you")
   - Multi-word phrases matched as substrings

3. **Response Engine** (`get_response()`)
   - Pure if-else decision tree
   - ~20+ rule categories
   - Fallback to random default responses

4. **Main Loop** (`main()`)
   - Continuous input/output cycle
   - Graceful exit handling
   - Session statistics

### Example Flow
```python
User Input: "who are you?"
  ↓
Normalize: "who are you"
  ↓
Pattern Match: Triggers "ABOUT BOT" rule
  ↓
Response: Multi-line introduction
  ↓
Display with typing effect
```

---

## 📦 Dependencies

```
Python Standard Library:
  - random
  - time
  - typing
  - datetime (imported inside get_response)
  - re (for word-boundary matching)
```

No external packages required! This is a **pure Python** implementation.

---

## 🧪 Testing

Run unit tests:
```bash
python -m pytest tests/test_bot.py -v
```

Or use the legacy test runner:
```bash
python test_bot.py
```

---

## 🎨 Customization

### Add New Responses
Edit the response banks in `rule_based_chatbot.py`:
```python
GREETINGS = [
    "Your custom greeting here!",
    "Another greeting...",
]
```

### Add New Rules
Insert a new if-else block in `get_response()`:
```python
# ── CUSTOM RULE ───────────────────────────
if contains_any(text, ["your keywords here"]):
    return "Your custom response"
```

### Adjust Typing Speed
Modify the sleep duration in `bot_says()`:
```python
time.sleep(0.018)  # Decrease for faster typing
```

---

## 📊 Session Statistics

After exiting (typing "bye"), the bot displays:
```
📊 Session Stats: 12 message(s) exchanged.
```

This tracks conversation length for user engagement insights.

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ **Control Flow:** if-elif-else decision trees
- ✅ **String Processing:** normalization, pattern matching, regex
- ✅ **Data Structures:** dictionaries, lists, tuples
- ✅ **Functions:** modularity, type hints, docstrings
- ✅ **User I/O:** input validation, formatted output
- ✅ **Exception Handling:** graceful error recovery
- ✅ **Algorithm Design:** rule prioritization, fallback logic

---

## 👨‍💼 Author & Credits

**Project:** DecodeLabs AI Internship - Batch 2026  
**Project 1:** Rule-Based AI Chatbot  
**Engineer:** AI Intern  

---

## 📝 License

This project is part of the DecodeLabs Internship curriculum.

---

## 🤝 Support

For questions or issues:
1. Type `help` in the chatbot for command list
2. Review the docstrings in `rule_based_chatbot.py`
3. Check `tests/test_bot.py` for usage examples

---

**Enjoy chatting with your Rule-Based Chatbot! 🚀**
