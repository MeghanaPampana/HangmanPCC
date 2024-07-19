import random
from hangman_words import qa_list
from hangman_art import logo, stages

def play_hangman(questions, reveal_percentage=0.20):
    # Select a random question and its corresponding answer
    question, answer = random.choice(questions)
    questions.remove((question, answer))
    word_length = len(answer)
    end_of_game = False
    lives = 6

    print(logo)

    # Print the question
    print(question)

    # Initialize the display with underscores, preserving non-letter characters
    display = [char if not char.isalpha() else "_" for char in answer]

    # Calculate the number of letters to reveal based on the percentage
    num_to_reveal = max(1, int(word_length * reveal_percentage))
    reveal_indices = random.sample(
        [i for i, char in enumerate(answer) if char.isalpha()], num_to_reveal
    )
    for index in reveal_indices:
        display[index] = answer[index]

    while not end_of_game:
        print(f"\nQuestion: {question}")  # Display the question before each guess
        
        try:
            guess = input("Guess a letter: ").lower()
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            return None

        if guess in display:
            print(f"You've already guessed {guess}")

        if guess.isalpha() and len(guess) == 1:
            if guess in answer:
                for position in range(word_length):
                    letter = answer[position]
                    if letter == guess:
                        display[position] = letter
            else:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose.")
                    print(f"The correct answer was: {answer}")
        else:
            print("Please enter a valid single letter.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])

    return questions

def main():
    remaining_questions = qa_list.copy()
    while remaining_questions:
        remaining_questions = play_hangman(remaining_questions)
        if remaining_questions is None:
            break
        if not remaining_questions:
            print("No more questions available. Thank you for playing!")
            break
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
