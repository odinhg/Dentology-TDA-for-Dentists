import argparse
import trimesh
import pathlib
import numpy as np
from gudhi import SimplexTree, plot_persistence_diagram
import matplotlib.pyplot as plt

def load_mesh(input_file: pathlib.Path, scale: float=0.1) -> trimesh.Trimesh:
    mesh = trimesh.load_mesh(input_file)
    mesh.apply_scale(scale)
    return mesh

def show_mesh(mesh: trimesh.Trimesh) -> None:
    mesh.show(viewer="gl")

def build_simplex_tree(mesh: trimesh.Trimesh) -> SimplexTree:
    points = mesh.vertices
    edges = mesh.edges_unique
    f = lambda x: x[-1] # Use Z coordinate as filtration value
    st = SimplexTree()

    for i in range(len(points)):
        st.insert([i], filtration=f(points[i]))

    for e in edges:
        st.insert(e, filtration=max(map(f, points[e])))

    return st

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Sample a point cloud from STL file")
    parser.add_argument("--filename", type=str, help="Path to the STL file", default="data/premolar_normal.stl")
    parser.add_argument("--plot_mesh", help="Plot the 3D mesh", action=argparse.BooleanOptionalAction, default = False)
    args = parser.parse_args()
    filename = pathlib.Path(args.filename)
    plot_mesh = args.plot_mesh

    mesh = load_mesh(filename)
    st = build_simplex_tree(mesh)
    
    if plot_mesh:
        show_mesh(mesh)

    # Compute persistence diagram
    diag = st.persistence(homology_coeff_field=2)

    # Plot persistence diagram
    fig, ax = plt.subplots(figsize=(10, 10))
    plot_persistence_diagram(diag, axes=ax)
    plt.title(f"Persistence Diagram of {filename}")
    fig.tight_layout()
    plt.show()
