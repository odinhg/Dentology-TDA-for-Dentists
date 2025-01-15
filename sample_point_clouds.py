import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse
import pathlib
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample a point cloud from STL file")
    parser.add_argument("--filename", type=str, help="Path to the STL file", default="data/stl/premolar_normal.stl")
    parser.add_argument("--n_points", type=int, help="Number of points to sample", default=2000)
    parser.add_argument("--output", type=str, help="Path to save the point cloud", default="data/point_clouds/premolar_normal.npy")
    parser.add_argument("--plot", help="Plot the point cloud", action=argparse.BooleanOptionalAction, default = False)

    args = parser.parse_args()
    filename = args.filename
    n_points = args.n_points
    output = args.output
    plot = args.plot

    mesh = trimesh.load(filename)
    point_cloud, _ = trimesh.sample.sample_surface_even(mesh, n_points)

    if output:
        pathlib.Path(output).parent.mkdir(parents=True, exist_ok=True)
        np.save(output, point_cloud)

    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(*point_cloud.T, s=0.4)
        plt.show()

