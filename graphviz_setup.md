
# How to Install Graphviz

This guide provides step-by-step instructions on how to install Graphviz, a powerful tool for visualizing graphs and parse trees.

## 1. Install Graphviz on Different Operating Systems

1. Go to the [Graphviz download page](https://graphviz.org/download/).
2. Download the appropriate installer for your system (usually the `.exe` file).
3. Run the installer and follow the installation instructions.
4. After installation, add the Graphviz `bin` folder to your system's `PATH` environment variable:
    - Open the **Start Menu** and search for "Environment Variables."
    - Select "Edit the system environment variables."
    - Click "Environment Variables" in the System Properties window.
    - Under "System variables," find the `Path` variable, select it, and click "Edit."
    - Add the path to the Graphviz `bin` folder (e.g., `C:\Program Files\Graphviz\bin`).
5. Open the Command Prompt and verify the installation:

    ```cmd
    dot -V
    ```

## 2. Verify the Installation

To confirm that Graphviz is installed correctly, run the following command in your terminal or command prompt:

```bash
dot -V
```

You should see output similar to the following:

```
dot - graphviz version 2.44.1 (20200629.0846)
```

## 3. Using Graphviz

After successfully installing Graphviz, you can use the `dot` command to generate visual representations of graphs from DOT files. For example, to generate a PNG from a DOT file:

```bash
dot -Tpng input.dot -o output.png
```

This will create a `output.png` file from the `input.dot` graph file.

## 4. Additional Resources

- [Official Graphviz Documentation](https://graphviz.org/documentation/)
- [Graphviz Gallery (Examples)](https://graphviz.org/gallery/)

Graphviz is now installed and ready to use! If you encounter any issues or need further assistance, refer to the official documentation or explore community forums.
