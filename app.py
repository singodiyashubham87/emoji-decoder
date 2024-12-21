import boto3
import os
import random
from botocore.exceptions import ClientError

class EmojiDecoderGame:
    def __init__(self):
        # Initialize DynamoDB client
        self.dynamodb = boto3.resource('dynamodb',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        self.puzzles_table = self.dynamodb.Table('EmojiPuzzles')
        self.scores_table = self.dynamodb.Table('PlayerScores')

    def get_all_puzzles(self):
        try:
            response = self.puzzles_table.scan()
            return response.get('Items', [])
        except ClientError as e:
            print(f"Error fetching puzzles: {e}")
            return []

    def get_player_score(self, player_id):
        try:
            response = self.scores_table.get_item(
                Key={'PlayerID': player_id}  # Key name matches table schema
            )
            return response.get('Item', {}).get('Score', 0)  # Default to 0 if no record exists
        except ClientError as e:
            print(f"Error fetching score: {e}")
            return 0

    def update_player_score(self, player_id, new_score):
        try:
            self.scores_table.put_item(
                Item={
                    'PlayerID': player_id,  # Ensure this matches table schema
                    'Score': new_score
                }
            )
            return True
        except ClientError as e:
            print(f"Error updating score: {e}")
            return False

    def play_game(self):
        print("Welcome to Emoji Decoder!")
        player_id = int(input("Enter your player ID (number): "))  # Convert to int for correct data type

        # Get current score
        current_score = self.get_player_score(player_id)
        print(f"Your current score: {current_score}")

        # Get all puzzles
        puzzles = self.get_all_puzzles()
        if not puzzles:
            print("No puzzles available!")
            return

        # Select random puzzle
        puzzle = random.choice(puzzles)

        print("\nDecode this emoji sequence:")
        print(puzzle['Emojis'])

        # Get player's guess
        guess = input("Your answer: ").strip().lower()
        correct_answer = puzzle['Phrase'].lower()

        if guess == correct_answer:
            print("Correct! 🎉")
            new_score = current_score + 10
            if self.update_player_score(player_id, new_score):
                print(f"Score updated! New score: {new_score}")
        else:
            print(f"Sorry, that's not correct. The answer was: {puzzle['Phrase']}")
            print(f"Your score remains: {current_score}")

def main():
    game = EmojiDecoderGame()
    while True:
        game.play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
