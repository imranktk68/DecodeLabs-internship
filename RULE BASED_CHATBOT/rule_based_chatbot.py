"""
╔══════════════════════════════════════════════════════════════╗
║       DecodeLabs Internship — Batch 2026                     ║
║       Project 1: Rule-Based AI Chatbot                    ║
║       Engineer: AI Intern                                    ║
╚══════════════════════════════════════════════════════════════╝

Key Requirements Fulfilled:
  ✅ Handle greetings and exit commands
  ✅ Use if-else logic for responses
  ✅ Run in a continuous loop
  ✅ Expanded vocabulary & personality
"""

import random
import time
from typing import Optional


# ─────────────────────────────────────────────
#  BOT IDENTITY
# ─────────────────────────────────────────────
BOT_NAME = "Rule-Based Chatbot"
BOT_VERSION = "1.0"


# ─────────────────────────────────────────────
#  HELPER UTILITIES
# ─────────────────────────────────────────────

def bot_says(message: str) -> None:
    """Print the bot's response with a typing effect."""
    print(f"\n  🤖 {BOT_NAME} » ", end="", flush=True)
    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.018)
    print()


def divider() -> None:
    print("  " + "─" * 56)


def normalize(text: str) -> str:
    """Lowercase and strip punctuation for easy matching."""
    cleaned = ""
    for ch in text.lower():
        if ch.isalnum() or ch == " ":
            cleaned += ch
    return cleaned.strip()


def contains_any(text: str, keywords: list) -> bool:
    """Return True if any keyword appears in the text."""
    for word in keywords:
        if word in text:
            return True
    return False


# ─────────────────────────────────────────────
#  RESPONSE BANKS  (rule → list of replies)
# ─────────────────────────────────────────────

GREETINGS = [
    "Hey there! I'm your Rule-Based Chatbot, your AI companion. What's on your mind? 😊",
    "Hello, human! Rule-Based Chatbot online and ready to chat. How can I help?",
    "Hi! Great to see you. I'm your Rule-Based Chatbot — ask me anything!",
    "Greetings, explorer! Rule-Based Chatbot at your service. 🚀",
]

FAREWELLS = [
    "Goodbye! It was wonderful talking to you. Come back soon! 👋",
    "See you later! Stay curious and keep building. 🛠️",
    "Farewell! Remember: every expert was once a beginner. 💡",
    "Catch you next time! Rule-Based Chatbot signing off. 🤖",
]

THANKS_REPLIES = [
    "You're very welcome! That's what I'm here for. 😊",
    "Happy to help! Is there anything else on your mind?",
    "Anytime! Feel free to ask more questions.",
    "My pleasure! Keep those questions coming. 🌟",
]

FEELING_GOOD = [
    "That's fantastic! Positive energy makes everything better. ⚡",
    "Love to hear that! Keep up the great vibes! 🌟",
    "Awesome! You sound ready to conquer the day! 💪",
]

FEELING_BAD = [
    "I'm sorry to hear that. Remember, every storm runs out of rain. 🌈",
    "Tough days are part of the journey. You've got this! 💙",
    "I hear you. Take a deep breath — things will get better. 🌿",
]

JOKE_BANK = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "How many programmers does it take to change a light bulb? None — it's a hardware problem! 😄",
    "Why did the AI cross the road? It was optimizing its path-finding algorithm! 🤖",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I JOIN you?' 🍺",
    "Why do Python developers prefer snake_case? Because they can't camelCase properly! 🐍",
]

FACT_BANK = [
    "🔬 Fun Fact: The first computer bug was an actual bug — a moth found in a Harvard Mark II computer in 1947.",
    "🌐 Fun Fact: The Internet was originally called ARPANET and was created in 1969.",
    "🧠 Fun Fact: The human brain processes images 60,000 times faster than text.",
    "🤖 Fun Fact: The word 'robot' comes from the Czech word 'robota', meaning forced labor.",
    "💻 Fun Fact: The first computer virus was created in 1983 as an experiment — not for harm!",
    "🎮 Fun Fact: The first video game ever made was called 'Tennis for Two' (1958).",
]

MOTIVATIONAL = [
    "💡 'The only way to do great work is to love what you do.' — Steve Jobs",
    "🚀 'It does not matter how slowly you go as long as you do not stop.' — Confucius",
    "🔥 'Code is like humor. When you have to explain it, it's bad.' — Cory House",
    "🌟 'First, solve the problem. Then, write the code.' — John Johnson",
    "💪 'The best time to plant a tree was 20 years ago. The second best time is now.' — Proverb",
]

AI_TOPICS = {
    "machine learning": (
        "Machine Learning is a subset of AI where systems learn patterns from data "
        "without being explicitly programmed. Think of it as teaching by example! 📊"
    ),
    "deep learning": (
        "Deep Learning uses neural networks with many layers to model complex patterns. "
        "It powers image recognition, speech, and more! 🧠"
    ),
    "natural language processing": (
        "NLP helps computers understand and generate human language. "
        "That's how chatbots like me process your words! 🗣️"
    ),
    "computer vision": (
        "Computer Vision teaches machines to interpret visual information — "
        "like identifying objects in photos or videos. 📷"
    ),
    "neural network": (
        "A Neural Network is inspired by the human brain. "
        "It consists of layers of nodes that process and pass information to produce an output. 🕸️"
    ),
    "python": (
        "Python is the most popular language for AI/ML! "
        "Its simplicity and rich ecosystem (NumPy, TensorFlow, PyTorch) make it ideal. 🐍"
    ),
    "algorithm": (
        "An algorithm is a step-by-step set of instructions to solve a problem. "
        "Every AI system runs on carefully crafted algorithms! ⚙️"
    ),
    "data": (
        "Data is the fuel of AI. "
        "The quality and quantity of data directly impacts how smart your AI model becomes. 📦"
    ),
}

HELP_MENU = """
┌─────────────────────────────────────────────────────┐
│         Rule-Based Chatbot — What I Can Do          │
├─────────────────────────────────────────────────────┤
│  👋  Greetings    : hi, hello, hey                  │
│  💬  Feelings     : how are you, i feel sad/good    │
│  😂  Jokes        : tell me a joke                  │
│  🔬  Facts        : tell me a fact                  │
│  🌟  Motivation   : motivate me / quote             │
│  🤖  AI Topics    : machine learning, python, etc.  │
│  ⏰  Time/Date    : what time is it                 │
│  🧮  Math         : calculate / math                │
│  👤  About Bot    : who are you / what are you      │
│  📋  Help         : help / commands                 │
│  🚪  Exit         : bye, quit, exit                 │
└─────────────────────────────────────────────────────┘
"""


# ─────────────────────────────────────────────
#  MATH EVALUATOR  (simple rule-based)
# ─────────────────────────────────────────────

def try_math(user_input: str) -> Optional[str]:
    """
    Extract and evaluate a simple arithmetic expression.
    Supports: +  -  *  /  **  (integers & floats)
    Returns a formatted answer string, or None if not parseable.
    """
    expression = ""
    for ch in user_input:
        if ch in "0123456789.+-*/() ":
            expression += ch

    expression = expression.strip()
    if not expression:
        return None

    # Must contain at least one operator
    has_operator = any(op in expression for op in ["+", "-", "*", "/"])
    if not has_operator:
        return None

    try:
        result = eval(expression)  # Safe here: only digits/operators pass
        if isinstance(result, float):
            result = round(result, 6)
        return f"🧮 Result: {expression} = {result}"
    except Exception:
        return None


# ─────────────────────────────────────────────
#  CORE RESPONSE ENGINE  (if-else logic)
# ─────────────────────────────────────────────

def get_response(user_input: str) -> str:
    """
    The brain of the chatbot — pure if-else decision tree.
    Takes raw user input and returns an appropriate response.
    """
    raw = user_input.strip()
    text = normalize(raw)

    # ── EXIT ──────────────────────────────────
    if contains_any(text, ["bye", "goodbye", "exit", "quit", "see you", "later", "farewell"]):
        return random.choice(FAREWELLS) + "\n  [SESSION ENDED]"

    # ── GREETINGS ─────────────────────────────
    if contains_any(text, ["hi", "hello", "hey", "howdy", "good morning",
                            "good evening", "good afternoon", "sup", "yo"]):
        return random.choice(GREETINGS)

    # ── HELP / COMMANDS ───────────────────────
    if contains_any(text, ["help", "command", "what can you do", "options", "menu"]):
        return HELP_MENU

    # ── HOW ARE YOU ───────────────────────────
    if contains_any(text, ["how are you", "how r you", "you okay", "you good",
                            "hows it going", "whats up", "how do you do"]):
        return "I'm running at peak efficiency! ⚡ Thanks for asking. How are YOU doing today?"

    # ── USER FEELINGS: POSITIVE ───────────────
    if contains_any(text, ["i am good", "im good", "i feel great", "feeling good",
                            "doing well", "i am fine", "im fine", "i am great",
                            "never been better", "fantastic", "im happy", "i am happy"]):
        return random.choice(FEELING_GOOD)

    # ── USER FEELINGS: NEGATIVE ───────────────
    if contains_any(text, ["i am sad", "im sad", "not good", "feeling bad",
                            "not okay", "stressed", "tired", "exhausted",
                            "depressed", "i feel terrible", "awful", "horrible"]):
        return random.choice(FEELING_BAD)

    # ── THANKS ────────────────────────────────
    if contains_any(text, ["thank you", "thanks", "thx", "thank u", "ty",
                            "appreciate", "grateful"]):
        return random.choice(THANKS_REPLIES)

    # ── JOKES ─────────────────────────────────
    if contains_any(text, ["joke", "funny", "make me laugh", "something funny",
                            "tell me a joke", "humor"]):
        return random.choice(JOKE_BANK)

    # ── FACTS ─────────────────────────────────
    if contains_any(text, ["fact", "tell me something", "did you know",
                            "fun fact", "something interesting", "trivia"]):
        return random.choice(FACT_BANK)

    # ── MOTIVATION ────────────────────────────
    if contains_any(text, ["motivate", "motivation", "inspire", "quote",
                            "encouragement", "keep going", "i give up",
                            "feel like giving up"]):
        return random.choice(MOTIVATIONAL)

    # ── ABOUT BOT ─────────────────────────────
    if contains_any(text, ["who are you", "what are you", "your name",
                            "about you", "introduce yourself", "tell me about yourself"]):
        return (
            f"I'm {BOT_NAME} v{BOT_VERSION} 🤖\n"
            "  I'm a rule-based AI chatbot built as Project 1 of the DecodeLabs\n"
            "  AI Internship. I run on pure if-else logic and control flow. No\n"
            "  neural networks yet — just smart rules and a good personality! 😄"
        )

    # ── CREATOR / INTERNSHIP ──────────────────
    if contains_any(text, ["who made you", "who created you", "decodelabs",
                            "internship", "project"]):
        return (
            "I was built during the DecodeLabs AI Internship (Batch 2026) 🚀\n"
            "  Project 1: Rule-Based Chatbot — the foundation of all AI projects.\n"
            "  My creator is mastering control flow and decision-making logic!"
        )

    # ── TIME & DATE ───────────────────────────
    if contains_any(text, ["time", "date", "day", "today", "what year"]):
        from datetime import datetime
        now = datetime.now()
        return (
            f"⏰ Current Date & Time:\n"
            f"  📅 Date : {now.strftime('%A, %d %B %Y')}\n"
            f"  🕐 Time : {now.strftime('%I:%M:%S %p')}"
        )

    # ── MATH / CALCULATIONS ───────────────────
    if contains_any(text, ["calculate", "compute", "math", "what is",
                            "solve", "plus", "minus", "divide", "multiply"]):
        math_result = try_math(raw)
        if math_result:
            return math_result
        return (
            "I can handle basic math! Try typing an expression like:\n"
            "  👉 calculate 25 * 4\n"
            "  👉 what is 100 / 5\n"
            "  👉 solve 2 ** 10"
        )

    # Standalone math expression (e.g., user types "25 + 30")
    math_result = try_math(raw)
    if math_result:
        return math_result

    # ── AI TOPIC KNOWLEDGE BASE ───────────────
    for topic, explanation in AI_TOPICS.items():
        if topic in text:
            return explanation

    # ── REPEAT / WHAT DID YOU SAY ─────────────
    if contains_any(text, ["repeat", "say that again", "what did you say",
                            "can you repeat"]):
        return "I said: ask me anything and I'll do my best to answer! 😄"

    # ── MEANING OF LIFE ───────────────────────
    if contains_any(text, ["meaning of life", "purpose of life", "42"]):
        return "42. Obviously. 😄 (And also: learn, build, and help others!)"

    # ── FAVOURITE ─────────────────────────────
    if contains_any(text, ["favourite", "favorite", "best"]):
        if "language" in text or "programming" in text:
            return "Python, without a doubt! 🐍 Perfect for AI and incredibly readable."
        if "color" in text or "colour" in text:
            return "Electric Blue ⚡ — the color of electricity and innovation!"
        if "movie" in text or "film" in text:
            return "2001: A Space Odyssey 🌌 — a classic exploration of AI and humanity."
        if "food" in text:
            return "I don't eat, but if I could, I'd choose data — terabytes of it! 📦😄"

    # ── DEFAULT / UNKNOWN ─────────────────────
    defaults = [
        f"Hmm, I'm not sure about that yet. 🤔 Try asking me about AI, jokes, facts, or type 'help'!",
        f"Interesting! I haven't learned that rule yet. Type 'help' to see what I know. 📚",
        f"That's beyond my current rule set! I'm still learning. Type 'help' to explore my skills. 🌱",
        f"I didn't quite catch that. Could you rephrase, or type 'help' for my capabilities? 🤖",
    ]
    return random.choice(defaults)


# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────

def main():
    """Entry point — runs the continuous chatbot loop."""

    # ── BOOT SCREEN ───────────────────────────
    print()
    print("  ╔══════════════════════════════════════════════════════╗")
    print("  ║   🤖  Rule-Based Chatbot  v1.0                       ║")
    print("  ║   DecodeLabs Internship | Batch 2026 | Project 1     ║")
    print("  ╚══════════════════════════════════════════════════════╝")
    divider()
    bot_says("Initializing Rule-Based Chatbot...")
    time.sleep(0.4)
    bot_says("All systems operational. Hello, I'm your Rule-Based Chatbot! 👋")
    bot_says("Type 'help' to see what I can do, or just start chatting!")
    divider()

    # ── CONVERSATION TRACKER ──────────────────
    session_count = 0

    # ── MAIN LOOP ─────────────────────────────
    while True:
        try:
            print()
            user_input = input("  👤 You  » ").strip()
        except (EOFError, KeyboardInterrupt):
            bot_says("Caught an interrupt! Goodbye! 👋")
            break

        if not user_input:
            bot_says("It seems you didn't type anything. Try asking me something! 😊")
            continue

        session_count += 1
        response = get_response(user_input)

        divider()
        bot_says(response)
        divider()

        # Exit if a farewell response was generated
        if "[SESSION ENDED]" in response:
            print(f"\n  📊 Session Stats: {session_count} message(s) exchanged.")
            print()
            break


# ─────────────────────────────────────────────
#  RUN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    main()
