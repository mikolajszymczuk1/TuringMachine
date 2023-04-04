from typing import List

class TuringMachine:
    """ Class that represents basic version of Turing Machine """

    def __init__(self, input_tape: List[str], instructions_filename_path: str, machine_stop_keys: List[str], left_symbol = 'L', right_symbol = 'R') -> None:
        self.state = ''
        self.current_head_position = 0
        self.tape = input_tape
        self.left_symbol = left_symbol
        self.right_symbol = right_symbol
        self.machine_stop_keys = machine_stop_keys
        self.instructions_filename_path = instructions_filename_path
        self.instructions = {}  # Prepared instructions structure
        self.prepare_instructions()

    def prepare_instructions(self) -> None:
        """ Create instructions dict structure for better instructions management """

        with open(self.instructions_filename_path, 'r') as instructionsFile:
            for line in instructionsFile:
                state, symbol_to_find, new_state, symbol_to_replace, move_dir = line.replace('\n', '').split(',')

                if state not in self.instructions:
                    self.instructions[state] = {}

                self.instructions[state][symbol_to_find] = {
                    'new_state': new_state,
                    'symbol_to_replace': symbol_to_replace,
                    'move_dir': move_dir
                }

        self.state = list(self.instructions)[0] # Set first state as default

    def run_machine(self) -> str:
        """ Run machine computing process """

        while True:
            # Read symbol
            read_character = self.tape[self.current_head_position]
            if read_character not in self.instructions[self.state]:
                return 'REJECT'

            current_instruction = self.instructions[self.state][read_character]

            # Update state
            self.state = current_instruction['new_state']
            if current_instruction['new_state'] in self.machine_stop_keys:
                break

            # Write new/prev symbol
            self.tape[self.current_head_position] = current_instruction['symbol_to_replace']

            # Move machine head
            if current_instruction['move_dir'] == self.left_symbol:
                if self.current_head_position > 0:
                    self.current_head_position -= 1
            elif current_instruction['move_dir'] == self.right_symbol:
                self.current_head_position += 1

        return self.state
