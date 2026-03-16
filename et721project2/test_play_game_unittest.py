import unittest
from unittest.mock import patch
from io import StringIO
from main import Connect4


class TestPlayGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '1', '2', '2', '3', '3', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_player_x_wins(self, mock_stdout, mock_input):
        game = Connect4()
        game.play_game()

        output = mock_stdout.getvalue()

        self.assertIn("Player X wins!", output)

    @patch('builtins.input', side_effect=['a', '1', '1', '2', '2', '3', '3', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_game_handles_invalid_input_then_continues(self, mock_stdout, mock_input):
        game = Connect4()
        game.play_game()

        output = mock_stdout.getvalue()

        self.assertIn("Invalid input. Please enter a number between 1 and 7.", output)
        self.assertIn("Player X wins!", output)


if __name__ == '__main__':
    unittest.main()

#documentation in main python file