import nbformat


def merge_notebooks(notebook1_path, notebook2_path, output_path):
    # Load both notebooks
    with open(notebook1_path, "r", encoding="utf-8") as f1:
        nb1 = nbformat.read(f1, as_version=4)
    with open(notebook2_path, "r", encoding="utf-8") as f2:
        nb2 = nbformat.read(f2, as_version=4)

    # Append the cells of the second notebook to the first
    nb1.cells.extend(nb2.cells)

    # Save the merged notebook
    with open(output_path, "w", encoding="utf-8") as out:
        nbformat.write(nb1, out)


# Example usage
merge_notebooks("Task 01.ipynb", "03_classification.ipynb", "MergedNotebook.ipynb")
