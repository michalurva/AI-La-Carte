import os
import pydoc

def generate_recursive_docs(path, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = {'.venv'}

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_without_ext, _ = os.path.splitext(file_path)
                module_name = file_without_ext.replace(os.path.sep, ".")
                print(f"Generating docs for {module_name}")
                pydoc.writedoc(module_name)

if __name__ == "__main__":
    generate_recursive_docs(".")
