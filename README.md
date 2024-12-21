# 🎮 Emoji Decoder Game

Welcome to **Emoji Decoder**, a fun and engaging game where you decode emoji sequences into words or phrases! 🐍📜 → "Python Script" 🎉

## 🚀 Features

- Randomly selected emoji puzzles to keep the game exciting!
- Score tracking for each player stored in a DynamoDB table.
- Unlimited fun with a dynamic database of puzzles! 🌟

---

## 🛠️ How It Works

1. **Enter Your Player ID**: Each player is identified by a unique number (e.g., `1`).
2. **Decode the Emoji Sequence**: Guess the correct word or phrase that matches the emoji shown.
3. **Earn Points**: Each correct answer adds **+10 points** to your score.
4. **Save Progress**: Your score is stored in the database, so you can pick up where you left off! 💾

---

## 🧩 How the Game Works Internally

The game uses **AWS DynamoDB** to manage puzzles and player scores:

### Database Tables
1. **EmojiPuzzles Table**:
   - Stores emoji sequences and their corresponding answers.
   - Schema:
     - `PuzzleID` (Number): Unique ID for each puzzle.
     - `Emojis` (String): Emoji sequence.
     - `Phrase` (String): Correct answer.

   Example:
   | PuzzleID | Emojis | Phrase          |
   |----------|--------|-----------------|
   | 1        | 🐍📜   | Python Script   |
   | 2        | 🎸🌟   | Rockstar        |
   | 3        | 🌍📖   | World Book      |

2. **PlayerScores Table**:
   - Tracks scores for each player.
   - Schema:
     - `PlayerID` (Number): Unique ID for each player.
     - `Score` (Number): Current score of the player.

   Example:
   | PlayerID | Score |
   |----------|-------|
   | 1        | 10    |
   | 2        | 20    |

---

## 📋 Prerequisites

Before running the game, ensure the following:
1. **Python Installed**: Python 3.6+ is required.
2. **AWS Credentials**:
   - Set up your environment variables for AWS access:
     ```bash
     export AWS_ACCESS_KEY_ID="your_access_key"
     export AWS_SECRET_ACCESS_KEY="your_secret_key"
     export AWS_REGION="your_region"
     ```
3. **DynamoDB Tables**:
   - Create the `EmojiPuzzles` and `PlayerScores` tables in AWS DynamoDB as described above.
   - Populate the `EmojiPuzzles` table with sample data.

---

## 🖥️ How to Run the Game

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/emoji-decoder-game.git
   cd emoji-decoder-game
   ```
2. **Install Dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   pip install boto3
   ```
3. **Set AWS credentials**:
   ```bash
   export AWS_ACCESS_KEY_ID="your_access_key"
   export AWS_SECRET_ACCESS_KEY="your_secret_key"
   export AWS_REGION="your_region"
   ```
4. **Run the game**:
   ```bash
   python app.py
   ```

---

## 📚 Game Flow

1. **Start the Game**:
   - Enter your player ID (must be a number).
   - Your current score is retrieved from the `PlayerScores` table (or starts at `0` if you're a new player).

2. **Solve the Puzzle**:
   - A random emoji sequence is displayed.
   - Type your guess (case-insensitive).

3. **Scoring**:
   - Each correct answer adds **10 points** to your score.
   - Incorrect answers do not penalize your score.

4. **Play Again or Exit**:
   - Choose to solve another puzzle or exit the game.

---

## 🛠️ Behind the Scenes

### Code Explanation

1. **Initialization**:
   - The `boto3` library is used to connect to DynamoDB with AWS credentials provided through environment variables.

2. **Fetching Puzzles**:
   - The `get_all_puzzles()` method retrieves all puzzles from the `EmojiPuzzles` table in DynamoDB.
   - It scans the table and returns all items (emoji sequences and corresponding phrases).

3. **Player Score Management**:
   - The `get_player_score(player_id)` method retrieves the current score of a player from the `PlayerScores` table.
   - If the player does not exist, it defaults the score to `0`.
   - The `update_player_score(player_id, new_score)` method updates or adds the player's score in the `PlayerScores` table.

4. **Gameplay**:
   - The game randomly selects a puzzle from the `EmojiPuzzles` table.
   - It displays the emoji sequence to the player, accepts input for the guessed phrase, and validates it against the correct answer.
   - If the guess is correct, the score is incremented by **10 points** and updated in the database.
   - The game can be played repeatedly until the player chooses to exit.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features, improvements, or additional emoji puzzles, feel free to open an issue or submit a pull request. Let's make this game even more fun together! 🎉

---

## 🧑‍💻 Author

Developed by **[Shubham Singodiya](https://shubham-s-socials.vercel.app/)**.  
Feel free to reach out for any questions, feedback, or collaboration opportunities.  

Radhe-Radhe! 🌟
