
# How to Generate Files from a `.g4` Grammar File

This guide explains how to generate lexer, parser, and related files from a `.g4` grammar file using ANTLR.

## 1. Download ANTLR Jar

First, download the [ANTLR jar](https://www.antlr.org/download.html) from the official ANTLR download page. Make sure to download the latest version, e.g., `antlr-4.13.0-complete.jar`.

## 2. Set Up the ANTLR Environment

To simplify running ANTLR commands, set up your environment by adding the ANTLR jar to your `CLASSPATH`.

### Linux/macOS

Set the `CLASSPATH` in your terminal:

```bash
export CLASSPATH=".:/path/to/antlr-4.13.0-complete.jar:$CLASSPATH"
```

### Windows

Set the `CLASSPATH` in the command prompt:

```cmd
set CLASSPATH=.;C:\path\to\antlr-4.13.0-complete.jar;%CLASSPATH%
```

Replace `/path/to/antlr-4.13.0-complete.jar` with the actual path to the ANTLR jar file on your system.

## 3. Generate Files from a `.g4` File

You can generate lexer, parser, and related files using the following command:

### For Python

```bash
java -jar /path/to/antlr-4.13.0-complete.jar -Dlanguage=Python3 MyGrammar.g4
```

This will generate Python files based on your grammar:
- `MyGrammarLexer.py`
- `MyGrammarParser.py`

### Optional Flags

- `-visitor`: Generates a visitor interface.
- `-listener`: Generates a listener interface.
- `-no-listener`: Skips generating the listener.
- `-no-visitor`: Skips generating the visitor.

For example, to generate both the visitor and listener:

```bash
java -jar /path/to/antlr-4.13.0-complete.jar -Dlanguage=Python3 -visitor -listener MyGrammar.g4
```

## 4. Check the Generated Files

After running the command, the necessary lexer and parser files will be generated in the same directory as your `.g4` file. You should see files like:
- `MyGrammarLexer.py`
- `MyGrammarParser.py`
- `MyGrammarVisitor.py` (if you used the `-visitor` flag)
- `MyGrammarListener.py` (if you used the `-listener` flag)

## 5. Use the Generated Files

You can now use the generated files in your Python project. Here's an example of how to use the generated lexer and parser:

```python
from antlr4 import *
from MyGrammarLexer import MyGrammarLexer
from MyGrammarParser import MyGrammarParser

def main():
    input_stream = FileStream("path/to/your/input/file.rb")  # Input file
    lexer = MyGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(token_stream)
    
    tree = parser.program()  # Start from the 'program' rule

    print(tree.toStringTree(recog=parser))  # Print the parse tree

if __name__ == "__main__":
    main()
```

## 6. Use ANTLR in Other Languages

If you're generating code for other programming languages, change the `-Dlanguage=Python3` flag to the appropriate language:
- For Java: `-Dlanguage=Java`
- For C#: `-Dlanguage=CSharp`
- For JavaScript: `-Dlanguage=JavaScript`

## Conclusion

1. Download the ANTLR jar.
2. Set up the environment variables for easy command execution.
3. Run the appropriate command to generate lexer and parser files from your `.g4` grammar file.
4. Use the generated files in your project.

Let me know if you need further clarification!
