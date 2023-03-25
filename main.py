from app.TuringMachine import TuringMachine

TAPE = ['b', 'b', 'a', 'a', 'b', 'b', '_']
INSTRUCTIONS_FILE = './app/programs/palindrome/instructions.txt'

tm = TuringMachine(TAPE, INSTRUCTIONS_FILE, ['yes'])
print(tm.run_machine())
