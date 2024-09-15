import os
import shutil

def remove_pycache():
    """Remove __pycache__ directories from the project."""
    project_root = os.path.dirname(os.path.abspath(__file__))
    for root, dirs, files in os.walk(project_root):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            shutil.rmtree(pycache_path)
            print(f"Removed: {pycache_path}")

if __name__ == "__main__":
    remove_pycache()
    print("All __pycache__ directories have been removed.")
