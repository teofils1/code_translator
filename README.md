# Code Translator: Ruby to Python

A code translator tool that converts Ruby code to Python. The project leverages ANTLR to parse Ruby syntax and generate the corresponding Python code. The project is packaged with [Poetry](https://python-poetry.org/) for environment management and dependency handling.

## Features
- Converts Ruby code to Python syntax.
- Supports various Ruby constructs such as loops, conditionals, classes, and methods.
- Error handling for undeclared variables and missing methods.
- Easily extensible for adding more language constructs.

## Installation

This project uses [Poetry](https://python-poetry.org/) for environment and dependency management. To set up the project:

### 1. Clone the Repository
Start by cloning the repository and navigating to the project directory:

```bash
git clone https://github.com/your-repo/code_translator.git
cd code_translator
```

### 2. Install Dependencies
Use Poetry to install all required dependencies:

```bash
poetry install
```

### 3. Activate the Virtual Environment
Activate the environment created by Poetry:

```bash
poetry shell
```

### 4. Generate the Parse Tree
To generate a `.dot` file for a specific Ruby file, navigate to the `app/app` directory and run the `parse_tree.py` script:

```bash
cd app/app
python parse_tree.py
```

Make sure the script is properly set up to point to the `.rb` file you want to parse.

### 5. Install Graphviz
Ensure Graphviz is installed on your system. You can find detailed installation instructions in this [Graphviz Installation Guide](graphviz_install_guide.md). After installation, use Graphviz to convert the `.dot` file into an SVG representation of the parse tree:

```bash
dot -Tsvg tree.dot -o tree.svg
```

This will create an SVG file (`tree.svg`) representing the parse tree for the Ruby file.

### 6. Run the GUI
To launch the graphical user interface, run `main.py` from the `app/app` directory:

```bash
python main.py
```

Alternatively, you can debug the project in your preferred development environment.
