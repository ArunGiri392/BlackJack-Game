from importlib import reload
from unittest import TestCase, main
from unittest.mock import patch
import io
import sys

def print_value(question, answer):
    print(question + answer)
    return answer

def run_test(user_cards, answers, dealer_cards, randint_mock, input_mock, imported):
    """
    Mocks randint and runs function with mock

    Args:
      randint_mock - patched random.randint()
      cards - desired input for random.randint()
      input_mock - patched bultins.input()
      answers - desired input for builtins.input()
      imported - whether module was imported already; always pass in True for your tests
    """
    answers.reverse() # reverses answers so can pop off list
    randint_mock.side_effect = user_cards + dealer_cards # set randint calls to cards
    input_mock.side_effect = \
        lambda question: print_value(question, answers.pop()) # print input question along with given answer

    # Save printed output into variable so can return it to compare in test
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    import blackjack_final
    if imported:
        reload(blackjack_final)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    return output # return printed statements in student-run code

class BlackjackPart6Test(TestCase):

    @patch('random.randint')
    @patch('builtins.input')
    def test_0_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''

        # Pass in True as the last argument in all your tests
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock, False)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.
    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final1(self, input_mock, randint_mock):
        '''
            Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([3, 5, 1], ['y', 'n'], [1, 6, 3], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a Ace\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 6\n" \
                   "Drew a 3\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final2(self, input_mock, randint_mock):
        '''
             Both the dealer and user receive cards that end up with a hand gretaer than 21.
        The result is tie as both of them gets busted.
        '''
        output = run_test([1, 5, 1], ['y', 'n'], [1, 6, 1], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 5\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a Ace\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 6\n" \
                   "Drew a Ace\n" \
                   "Final hand: 28.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Tie.\n"
                   
                   
                 
                   
        self.assertEqual(output, expected)
    
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final3(self, input_mock, randint_mock):
        '''
            Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        
        '''
        output = run_test([1, 6, 2], ['y', 'n'], [2, 7, 9], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 6\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 7\n" \
                   "Drew a 9\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final4(self, input_mock, randint_mock):
        '''
             Both the dealer and user receive cards that end up with a hand of 21.
        The result is tie as both of them gets Blackjack.
    
        '''
        output = run_test([1, 5, 5], ['y', 'n'], [7, 9, 5], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 5\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 9\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Tie.\n"
        self.assertEqual(output, expected)   
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final5(self, input_mock, randint_mock):
        '''
             The dealer receives card less than 21 and user receive cards greater than 21.
        The dealer wins as user gets busted.
    
        '''
        output = run_test([10, 5, 11], ['y', 'n'], [12, 3, 6], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a Jack\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 3\n" \
                   "Drew a 6\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
                   
                   
                 
                   
        self.assertEqual(output, expected)
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final6(self, input_mock, randint_mock):
        '''
             The dealer receives card greater than 21 and user receive cards less than 21.
        The user wins as dealer gets busted.
    
        '''
        output = run_test([3, 5, 4], ['y', 'n'], [7, 8, 1], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 12. Hit (y/n)? n\n" \
                   "Final hand: 12.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 8\n" \
                   "Drew a Ace\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
                   
                  
                   
                 
                   
        self.assertEqual(output, expected)
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final7(self, input_mock, randint_mock):
        '''
              The  user receive cards equal to 21 and dealer receive less than 21
        The user wins as user cards gets Blackjack.
    
        '''
        output = run_test([10, 6, 5], ['y', 'n'], [1, 6, 2], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 6\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 6\n" \
                   "Drew a 2\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final8(self, input_mock, randint_mock):
        '''
              The  dealer receive cards equal to 21 and user receive less than 21
        The dealer wins as dealer cards gets Blackjack.
    
        '''
        
        output = run_test([8, 4, 3], ['y', 'n'], [7, 10, 4], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 8\n" \
                   "Drew a 4\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 15. Hit (y/n)? n\n" \
                   "Final hand: 15.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 10\n" \
                   "Drew a 4\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)   
        
        
    @patch('random.randint')
    @patch('builtins.input')
    def test_blackjack_final9(self, input_mock, randint_mock):
        '''
              Both the dealer and user receive cards less than 21 but have equal so the result is tie.
    
        '''
        output = run_test([3, 5, 1], ['y', 'n'], [1, 6, 2], randint_mock, input_mock, True)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a Ace\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Ace\n" \
                   "Drew a 6\n" \
                   "Drew a 2\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Tie.\n"
        self.assertEqual(output, expected)
        
                  
    
   
    
        
        
    
    
        
        
        
    
                   
    
        
        
    

        
    
    

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
