*This is a submission for the [Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01)*

# ⚡ StudyBuddy: An Aesthetic All-in-One Study Companion Built for My Best Friend

---

## What I Built

Every exam season, I watch my friend struggle with digital clutter and burnout. Like many students, they were juggling three or four fragmented tools at once:
- A separate tab for a Pomodoro timer (filled with banner ads and subscription popups),
- A clunky flashcard app with paywalled decks, and
- A rigid quiz tool that didn't allow quick question customization without paying for "premium tiers."

This constant context-switching caused cognitive overload and drained focus right before critical study sessions.

To solve this, I built **StudyBuddy** — a streamlined, distraction-free study companion designed to bring all their study workflows under one elegant, calm roof. It is built around a lightweight, zero-bloat **3-file architecture** (`app.py`, `index.html`, `style.css`) that anyone can run locally in seconds.

### 🌟 Core Capabilities
1. **⏱️ Pomodoro Focus Timer**:
   - Smooth circular SVG progress ring with real-time countdown.
   - 3 focused modes: **Focus (25m)**, **Short Break (5m)**, and **Long Break (15m)**.
   - Synthesized Web Audio API bell chimes that sound without needing external audio downloads.
   - Session cycle tracking (*Cycle 1 of 4*) and daily focus minute counters.

2. **🗂️ Interactive 3D Flashcards**:
   - Realistic 3D card-flip animations on click or by pressing <kbd>Space</kbd>.
   - Custom deck creator to organize study materials by subject.
   - Spaced-repetition rating buttons (**Need Practice** / **Mastered**) to review tricky concepts.
   - **⚡ One-Click Quiz Generator**: Converts any flashcard deck into an interactive multiple-choice quiz instantly!

3. **📝 Customizable Quiz System ("Where You Can Set It")**:
   - Lets students create their own custom quizzes tailored to their exact exam syllabus.
   - Full question builder: Question prompt, 4 choices, radio selector for the correct answer, and an optional explanation note.
   - Instant visual feedback (green glow on correct answer, red highlight with shake on incorrect choice) and instant rationale display.
   - Results scorecard with percentage score and answer breakdown review.

4. **🎨 Calming Aesthetic Design**:
   - Minimalist glassmorphic dark mode (plus toggleable crisp light mode).
   - Zero external library dependencies — works offline and saves all progress directly to browser `localStorage`.

---

## Demo

Experience StudyBuddy by running it locally with Python:

```bash
# Clone the repository
git clone https://github.com/harsh4944/studybuddy.git
cd studybuddy

# Run the app (opens automatically in your browser!)
python app.py
```

The app will launch directly at **`http://localhost:5000`**.

### 📸 Application Preview
- **Pomodoro View**: Circular SVG timer with glowing accent progress, customizable intervals, and session counts.
- **Flashcard View**: 3D card scene with smooth perspective flips, keyboard shortcuts, and deck switcher.
- **Quiz Maker View**: Clean question builder with instant feedback checks and scorecard summaries.

---

## Code

The complete source code is open source and hosted on GitHub:

{% github harsh4944/studybuddy %}

👉 **Direct Repository Link**: [https://github.com/harsh4944/studybuddy](https://github.com/harsh4944/studybuddy)


### Minimalist 3-File Architecture
```text
studybuddy/
├── app.py          # Python Flask backend (serves app & launches browser)
├── index.html      # Responsive UI structure & self-contained client logic
├── style.css       # Complete modern CSS design system & animations
└── README.md       # Comprehensive documentation & setup instructions
```

---

## How I Built It

To build StudyBuddy rapidly without sacrificing visual quality or performance, I paired with the **Google Antigravity IDE** autonomous coding agent:

1. **Rapid Architecture Iteration**:
   - We initially explored a multi-module client-side setup and then refactored it into an ultra-clean **3-file setup** (`app.py`, `index.html`, `style.css`) to ensure maximum simplicity, readability, and zero installation friction for my friend.

2. **Zero-Dependency Web Audio Engineering**:
   - Instead of linking unreliable external `.mp3` files that fail offline or hit CORS issues, we leveraged the browser's native **Web Audio API** to synthesize harmonic chime frequencies (C5, E5, G5, C6) and soft tactile clicks purely through code oscillators.

3. **Pure Vanilla CSS Design System**:
   - Handcrafted custom CSS variables, glassmorphic backdrop blurs, 3D perspective transforms (`rotateY(180deg)` with `transform-style: preserve-3d`), and fluid CSS Grid/Flexbox layouts without heavy CSS frameworks like Tailwind or Bootstrap.

4. **Python Flask Backend**:
   - Built a lightweight server in `app.py` that serves the application, binds to `0.0.0.0:5000`, and includes an automatic browser launcher thread alongside a built-in fallback to Python’s `http.server` if Flask is absent.

---

## Why Does Open Innovation Matter?

Education is the ultimate equalizer, but modern educational tools are increasingly plagued by aggressive monetization, paywalls on flashcard decks, and data-harvesting trackers.

Open innovation matters because:
- **Privacy & Focus**: A study app should respect a student’s attention. By keeping StudyBuddy open source and offline-first, no personal data, study habits, or test scores ever leave the student’s machine.
- **Full Customizability**: No two learners study the same way. An open codebase means my friend (or any student worldwide) can fork the repository, tweak timer durations, craft custom quiz styles, and adapt the tool to their unique learning needs.
- **Community Empowerment**: Open source empowers developers to share educational resources freely, helping friends, classmates, and study groups grow together.

---

## My Agent Session

This project was built with the assistance of the **Google Antigravity IDE**:
- **Pair Programming**: We brainstormed the user flow, designed the Pomodoro and Quiz state machines, refined the 3D card animation physics, and verified HTTP endpoints via automated Python test harnesses.
- **Continuous Refactoring**: When simplifying the project layout, the agent automatically removed intermediate scaffold files and unified the codebase into 3 clean, maintainable files.

---

## Prize Categories

- **Build for a Friend**
- **Most Useful Hack**
- **Best Overall Project**

---

*Made with ❤️ for students everywhere. Happy Hacktoberfest!*
