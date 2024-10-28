from antlr4 import *
from grammar.RubyLexer import RubyLexer
from grammar.RubyParser import RubyParser
from antlr4.tree.Trees import Trees


def generate_dot(tree, parser):
    """ Recursively convert the parse tree to a more detailed DOT format """
    dot = ['digraph ParseTree {']
    
    def traverse(node, parent_id=None, node_id=0, depth=0):
        # Create labels for terminal and non-terminal nodes with more details
        if isinstance(node, TerminalNode):
            # For terminal nodes, show both the text and the token type
            token_type = parser.symbolicNames[node.symbol.type] if node.symbol.type >= 0 else "UNKNOWN"
            label = f"'{node.getText()}' ({token_type})"
        else:
            # For non-terminal nodes, include the rule name and the depth in the parse tree
            rule_name = parser.ruleNames[node.getRuleIndex()]
            label = f"{rule_name} (depth={depth})"

        label = label.replace('"', '\\"')  # Escape quotes for DOT format

        # Create the DOT node with label
        dot.append(f'{node_id} [label="{label}"];')
        
        # Create an edge between parent and child
        if parent_id is not None:
            dot.append(f'{parent_id} -> {node_id};')

        # Recursively process child nodes for non-terminal nodes
        if not isinstance(node, TerminalNode):
            for i, child in enumerate(node.children, start=1):
                traverse(child, node_id, node_id * 10 + i, depth + 1)

    # Start traversing the tree from the root node
    traverse(tree)
    
    # End of the DOT graph
    dot.append('}')
    return '\n'.join(dot)


def main():
    input_stream = FileStream("../tests/CorrectTests/classes.rb")

    lexer = RubyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RubyParser(token_stream)

    # Parse the input and get the parse tree
    tree = parser.program()

    # Convert the parse tree to a more detailed DOT format
    dot_representation = generate_dot(tree, parser)

    # Save the DOT file
    with open("tree.dot", "w") as f:
        f.write(dot_representation)

    print("DOT file generated as 'tree.dot'")

if __name__ == "__main__":
    main()
