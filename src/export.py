from pathlib import Path
from zipfile import ZipFile

def find_repo_root():
    cwd = Path.cwd()
    if cwd.name == "notebooks":
        return cwd.parent
    return cwd

def finalize_notebook(
    notebook="00_context.ipynb",
    zip_name="benefits-distribution-00-context-outputs.zip",
    folders=("figures", "results", "data"),
):
    """
    Create a zip archive of generated notebook outputs and display
    download links for both the notebook and the archive in Colab/Jupyter.
    """
    root = find_repo_root()
    zip_path = root / zip_name
    notebook_path = root / "notebooks" / notebook

    with ZipFile(zip_path, "w") as z:
        for folder_name in folders:
            folder = root / folder_name
            if folder.exists():
                for file in folder.rglob("*"):
                    if file.is_file():
                        z.write(file, file.relative_to(root))

    print(f"Created: {zip_path}")

    try:
        from IPython.display import FileLink, display
        if notebook_path.exists():
            print("Notebook:")
            display(FileLink(str(notebook_path)))
        print("Outputs zip:")
        display(FileLink(str(zip_path)))
    except Exception:
        print("Notebook:", notebook_path)
        print("Outputs zip:", zip_path)

    return zip_path
