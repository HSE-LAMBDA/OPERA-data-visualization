import pandas as pd
import numpy as np


dZ = 205. # 0.0205 cm emulsion

def plot_dataframe(data: pd.DataFrame, vertex: pd.DataFrame,  azim=-84, elev=10):
    """
    Function for plotting shower
    """
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Line3DCollection
    import matplotlib.pyplot as plt
    
    x_v, y_v, z_v = vertex.posX.values, vertex.posY.values, vertex.posZ.values
    
    vertecis = np.array([z_v, y_v, x_v]).T.reshape(-1, 3)
    vertecis_ = np.array([z_v+7.0, y_v+7.0, x_v+7.0]).T.reshape(-1, 3)
    
    C0 = plt.cm.Reds(0.9)
    lc0 = Line3DCollection(list(zip(vertecis, vertecis_)), colors=C0, alpha=0.9, lw=2)

    x0, y0, z0 = data.SX.values, data.SY.values, data.SZ.values
    sx, sy = data.TX.values, data.TY.values

    x1 = x0 + dZ * sx
    y1 = y0 + dZ * sy
    z1 = z0 + dZ
    
    start_points = np.array([z0, y0, x0]).T.reshape(-1, 3)
    end_points = np.array([z1, y1, x1]).T.reshape(-1, 3)

    C = plt.cm.Blues(0.9)
    lc = Line3DCollection(list(zip(start_points, end_points)), colors=C, alpha=0.9, lw=2)

    fig = plt.figure(figsize=(12, 12))
    ax = fig.gca(projection='3d')
    ax.view_init(azim=azim, elev=elev)
    ax.add_collection3d(lc0)
    ax.add_collection3d(lc)
    
    ax.set_xlabel("z")
    ax.set_ylabel("y")
    ax.set_zlabel("x") 
    ax.set_xlim(z0.min(), z1.max())
    ax.set_ylim(y0.min(), y1.max())
    ax.set_zlim(x0.min(), x1.max())
    
    plt.show()
    

    
def plot_dataframe_lines(data: pd.DataFrame,  azim=-84, elev=10):
    """
    Function for plotting shower
    """
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Line3DCollection
    import matplotlib.pyplot as plt

    x0, y0, z0 = data.posX1.values, data.posY1.values, data.posZ1.values 

    x1, y1, z1 = data.posX2.values, data.posY2.values, data.posZ2.values
    
    start_points = np.array([z0, y0, x0]).T.reshape(-1, 3)
    end_points = np.array([z1, y1, x1]).T.reshape(-1, 3)

    C = plt.cm.Greens(0.9)
    lc = Line3DCollection(list(zip(start_points, end_points)), colors=C, alpha=0.9, lw=2)

    fig = plt.figure(figsize=(12, 12))
    ax = fig.gca(projection='3d')
    ax.view_init(azim=azim, elev=elev)
    ax.add_collection3d(lc)
    
    ax.set_xlabel("z")
    ax.set_ylabel("y")
    ax.set_zlabel("x") 
    ax.set_xlim(z0.min(), z1.max())
    ax.set_ylim(y0.min(), y1.max())
    ax.set_zlim(x0.min(), x1.max())
    
    plt.show()

