import re

class Translator:
    def __init__(self):
        self.patterns = [
            # Method definitions
            (r'def\s+(\w+)\((.*?)\)', r'def \1(\2):'),
            (r'end', r''),  # Remove Ruby 'end'

            # Conditionals
            (r'if\s+(.*)', r'if \1:'),
            (r'elsif\s+(.*)', r'elif \1:'),
            (r'else', r'else:'),

            # Loops
            (r'while\s+(.*)', r'while \1:'),
            (r'for\s+(\w+)\s+in\s+(.*)', r'for \1 in \2:'),
            (r'(\w+)\.(each|map|select|reject|inject|reduce)\s+do\s*\|(\w+)\|', r'for \3 in \1:'),
            (r'(\w+)\.(each_with_index)\s+do\s*\|(\w+),\s*(\w+)\|', r'for \4, \3 in enumerate(\1):'),

            # Ranges
            (r'(\d+)\.\.(\d+)', r'range(\1, \2+1)'),  # Inclusive range
            (r'(\d+)\.\.(\d+)\.', r'range(\1, \2)'),  # Exclusive range

            # Ruby 'puts' -> Python 'print'
            (r'puts\s+(.*)', r'print(\1)'),
            (r'print\s*"(.*)"\s*%\s*\[(.*)\]', r'print(\1.format(\2))'),  # Ruby string formatting with %

            # Block conversion
            (r'\|\s*(\w+)\s*\|', r'\1'),

            # Lambdas
            (r'lambda\s*do\s*\|(\w+)\|', r'lambda \1: '),

            # Hashes (converted to Python dictionaries)
            (r':(\w+)\s*=>\s*(\w+)', r'"\1": \2'),  # Symbol keys
            (r'(\w+)\s*=>\s*(\w+)', r'"\1": \2'),   # String or other literal keys

            # Classes and Modules
            (r'class\s+(\w+)', r'class \1:'),
            (r'module\s+(\w+)', r'class \1:'),
            (r'include\s+(\w+)', r'from \1 import *'),  # Basic Mixin behavior

            # Function return
            (r'return\s+(.*)', r'return \1'),
            (r'(\w+)\.(first|last)', r'\1[0]' if r'\2' == 'first' else r'\1[-1]'),  # first/last to index access

            # Ruby attr_accessor
            (r'attr_accessor\s*:(\w+)', r'def __init__(self, \1=None):\n        self.\1 = \1'),

            # Exceptions
            (r'rescue', r'except'),
            (r'raise\s+(.*)', r'raise Exception(\1)'),

            # Single line comments
            (r'#(.*)', r'#\1'),
        ]

    def translate(self, ruby_code):
        python_code = ruby_code

        # Apply regex patterns for Ruby to Python translation
        for pattern, replacement in self.patterns:
            python_code = re.sub(pattern, replacement, python_code)

        return python_code