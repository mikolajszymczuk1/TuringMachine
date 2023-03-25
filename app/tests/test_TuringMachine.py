from ..TuringMachine import TuringMachine

class TestTuringMachine:
    def test_run_muchine(self):
        INSTRUCTIONS_FILE = './app/programs/palindrome/instructions.txt'

        tape = ['b', 'b', '_']
        assert TuringMachine(tape, INSTRUCTIONS_FILE, ['yes']).run_machine() == 'yes'

        tape = ['b', 'a', '_']
        assert TuringMachine(tape, INSTRUCTIONS_FILE, ['yes']).run_machine() == 'REJECT'

        tape = ['b', 'b', 'a', 'a', 'b', 'a', '_']
        assert TuringMachine(tape, INSTRUCTIONS_FILE, ['yes']).run_machine() == 'REJECT'

        tape = ['a', 'b', 'a', 'a', '_']
        assert TuringMachine(tape, INSTRUCTIONS_FILE, ['yes']).run_machine() == 'REJECT'

        tape = ['a', 'a', 'a', 'a', 'a', '_']
        assert TuringMachine(tape, INSTRUCTIONS_FILE, ['yes']).run_machine() == 'REJECT'

        tape = ['b', 'b', 'b', 'b', 'b', 'b', '_']
        assert TuringMachine(tape, INSTRUCTIONS_FILE, ['yes']).run_machine() == 'yes'

        tape = ['b', 'b', 'b', 'b', 'a', 'a', 'b', 'b', 'b', 'b', '_']
        assert TuringMachine(tape, INSTRUCTIONS_FILE, ['yes']).run_machine() == 'yes'
