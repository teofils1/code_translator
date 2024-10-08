from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from grammar.RubyLexer import RubyLexer
from grammar.RubyParser import RubyParser
from grammar.RubyVisitor import RubyVisitor

import PySimpleGUI as sg

class GUIErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Syntax error at {line}:{column} - {msg}"
        raise ValueError(error_message)

def main():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text("Ruby to Python Converter", font='Helvetica 15')],
        [sg.Text("Select a file to convert:", font='Helvetica 13')],
        [sg.Input(key="-FILE-", size=(30, 1), font='Helvetica 11'), sg.FileBrowse(font='Helvetica 11')],
        [sg.Text("Output Filename:", font='Helvetica 13')],
        [sg.Input(key="-OUTPUT-", size=(30, 1), font='Helvetica 11')],
        [sg.Button("Convert", key="-CONVERT-", font='Helvetica 11'),sg.Button("Quit", key="-QUIT-", font='Helvetica 11')],
        [sg.Column([[sg.Text("Input File:", font='Helvetica 13')],[sg.Multiline(size=(60, 20), key="-INPUT_TEXT-", disabled=True, font='Helvetica 11')]]),
         sg.Column([[sg.Text("Output:", font='Helvetica 13')],[sg.Output(size=(60, 20), key="-OUTPUT_LOG-", font='Helvetica 11')]])]
    ]
    window = sg.Window("Ruby to Python Converter", layout)
    output_element = window["-OUTPUT_LOG-"]
    input_element = window["-INPUT_TEXT-"]
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "-QUIT-":
            break
        if event == "-CONVERT-":
            output_element.update("")
            input_element.update("")
            file_path = values["-FILE-"]
            output_filename = values["-OUTPUT-"]
            if file_path:
                if output_filename:
                    try:
                        inp = FileStream(file_path)
                        lexer = RubyLexer(inp)
                        stream = CommonTokenStream(lexer)
                        parser = RubyParser(stream)
                        parser.addErrorListener(GUIErrorListener())
                        tree = parser.program()
                        visitor = RubyVisitor()
                        res = visitor.visit(tree)
                        if visitor.errors:
                            for error in visitor.errors:
                                output_element.print(f"Error: {error}")
                            output_element.print("Conversion aborted due to errors. Fix errors and try again.")
                        else:
                            output_filename = str(output_filename) + ".py"
                            output = open(output_filename, "w")
                            output.write(res)
                            output.close()
                            output_element.update(res)
                        input_file = open(file_path, "r")
                        input_element.update(input_file.read())
                    except ValueError as e:
                        output_element.print("")
                        input_file = open(file_path, "r")
                        input_element.update(input_file.read())
                else:
                    output_element.print("Enter a filename to save the output!")
            else:
                output_element.print("Select a file to convert!")
    window.close()

if __name__ == '__main__':
    main()