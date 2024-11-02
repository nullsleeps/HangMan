import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.word_list = ["python", "hangman", "challenge", "complex", "programming", "computer"]
        self.reset_game()

        self.label_word = tk.Label(master, text=self.display_word, font=('Arial', 24))
        self.label_word.pack(pady=20)

        self.label_guessed = tk.Label(master, text="Guessed Letters: ", font=('Arial', 14))
        self.label_guessed.pack(pady=10)

        self.label_attempts = tk.Label(master, text=f"Attempts Remaining: {self.attempts}", font=('Arial', 14))
        self.label_attempts.pack(pady=10)

        self.entry = tk.Entry(master, font=('Arial', 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess, font=('Arial', 14))
        self.guess_button.pack(pady=5)

        self.restart_button = tk.Button(master, text="Restart", command=self.reset_game, font=('Arial', 14))
        self.restart_button.pack(pady=5)

        self.message = tk.Label(master, text="", font=('Arial', 14))
        self.message.pack(pady=20)

    def reset_game(self):
        self.word = random.choice(self.word_list).lower()
        self.guessed_letters = set()
        self.attempts = 6
        self.display_word = '_' * len(self.word)
        self.update_display()

    def update_display(self):
        self.label_word.config(text=self.display_word)
        self.label_guessed.config(text="Guessed Letters: " + ' '.join(sorted(self.guessed_letters)))
        self.label_attempts.config(text=f"Attempts Remaining: {self.attempts}")

    def make_guess(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        if len(letter) == 1 and letter.isalpha() and letter not in self.guessed_letters:
            self.guessed_letters.add(letter)

            if letter in self.word:
                self.display_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
                if '_' not in self.display_word:
                    self.message.config(text="Congratulations! You've won!")
            else:
                self.attempts -= 1
                if self.attempts == 0:
                    self.message.config(text=f"Game Over! The word was: {self.word}")

            self.update_display()
        else:
            self.message.config(text="Invalid input or letter already guessed.")

if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()
