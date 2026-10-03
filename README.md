# ⚡ StudyBuddy

A clean, modern, and aesthetic study companion web application combining an animated **Pomodoro Focus Clock**, **3D Flashcards**, and a fully customizable **Quiz System** where you can create, edit, and take your own quizzes.

Built with a streamlined **3-file architecture** powered by Python Flask and modern Vanilla web technologies.

---

## 📁 Project Architecture

The entire project is structured into 3 core files:

```text
studybuddy/
├── app.py          # Python Flask backend server (with auto-browser launcher)
├── index.html      # Responsive frontend interface & application logic
├── style.css       # Design system, glassmorphism, animations & dark/light theme
└── README.md       # Project documentation & usage guide
```

---

## 🌟 Features

### 1. ⏱️ Pomodoro Focus Timer
- **3 Session Modes**: Focus (25 min), Short Break (5 min), and Long Break (15 min).
- **Circular SVG Countdown Ring**: Smooth real-time stroke animation showing your time progress.
- **Cycle & Goal Tracker**: Tracks sessions (e.g., *Cycle 1 of 4*) and displays daily total focus time.
- **Web Audio Chimes**: Synthesized bell chime alerts when focus or break sessions end.

### 2. 🗂️ Interactive 3D Flashcards ("Flask Card")
- **3D Card Flip**: Click the card or press <kbd>Space</kbd> to flip between Question (Front) and Answer (Back).
- **Decks Management**: Switch between pre-loaded study decks or click **📂 New Deck** to create your own subject.
- **Add & Manage Cards**: Click **➕ Add Card** to create custom questions and answers with subject tags.
- **Review Ratings**: Mark cards with **Need Practice** or **Mastered** to focus on harder concepts.
- **Deck Shuffling**: Randomize the card order with one click.
- **⚡ Make Quiz**: Convert any flashcard deck into an interactive multiple-choice quiz in 1 click!

### 3. 📝 Customizable Quiz System ("Where User Can Set It")
- **Custom Quiz Creator**: Click **📂 New Quiz** to create quizzes for any topic or exam.
- **Question Builder**: Click **➕ Add Question** to input your question prompt, add up to 4 choices, select the correct answer radio button, and write an optional explanation note.
- **Instant Interactive Feedback**: Options light up green with a checkmark for correct answers or red for wrong answers, revealing helpful explanations immediately.
- **Scorecard & Retry**: Displays your percentage score, encouraging feedback, and a button to retake the quiz.

### 4. 🎨 Design & Utilities
- **Dark & Light Modes**: One-click theme toggle (☀️ / 🌙) in the top right.
- **Local Persistence**: All created decks, flashcards, quizzes, and focus stats save automatically in browser `localStorage`.
- **Keyboard Shortcuts**:
  - <kbd>Space</kbd>: Flip active flashcard
  - Next/Prev buttons for quick card cycling

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed.

Install Flask (if not already installed):
```bash
pip install flask
```

### Running StudyBuddy
Simply run:
```bash
python app.py
```

The application will start and automatically open in your default browser at:
👉 **http://localhost:5000**

*(Note: If Flask is not installed, `app.py` includes a zero-dependency fallback that will automatically serve via Python's standard library).*

---

## 🐙 Git & GitHub

To commit and push your project to GitHub:

```bash
git add .
git commit -m "Add README and project documentation"
git push -u origin main
```
