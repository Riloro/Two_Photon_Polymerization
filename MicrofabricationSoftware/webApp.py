import dash
import dash_vtk
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import numpy as np
from numpy.core.function_base import linspace
import pyvista as pv
import pandas as pd

def build_line(pi, pf, stepSize):
    #Maximum travel ranges of the piezo stage
    #x,y = 100 um
    #z = 20 um
    #Defining the parametric equation of a line in R^3
    point_0 = pi  # np.array([1,1,5])#Initial point
    point_f = pf  # np.array([2,2,10])#Final point
    #line length
    line_len = np.linalg.norm(point_f - point_0)
    print("Magnitud = ", line_len)
    # Step size for line resolution : Also, resolution depends on laser pulse repetition and focus speed
    step_size = stepSize
    line_frac = step_size/line_len  # Line fraction represented by the desiered stepSize
    # Defining all the desired fractions until complete the line
    t = np.linspace(0, 1, int(np.ceil(1/line_frac)) + 1)
    #Parametric line equations
    x_lin = t * (point_f[0] - point_0[0]) + point_0[0]
    y_lin = t * (point_f[1] - point_0[1]) + point_0[1]
    z_lin = t * (point_f[2] - point_0[2]) + point_0[2]
    #Return x,y,z coordinates
    return x_lin, y_lin, z_lin


def build_helix(heigth, r, numberofPoints, sliceDist):
    z_h = np.linspace(0, heigth, numberofPoints)
    t = ((2 * np.pi)/(sliceDist)) * z_h
    x_h = r * np.cos(t)
    y_h = r * np.sin(t)
    #z = t / ((2 * np.pi)/(sliceDist))
    return x_h, y_h, t
    

#Build a plane defining hatching distance ax + by + cz = D
#Plane with normal = <0,0,1>
def build_planes(x_0,x_f,y_0,y_f,z_0,z_f,hatching_dist,slicing_dist):
    #Define x y vectors
    #Define hatchin distance
    lenX = np.abs(x_f - x_0)
    lenY = np.abs(y_f - y_0)
    lenZ = np.abs(z_f - z_0)
    pointPerLine = int(np.ceil(lenX/hatching_dist)) + 1
    x_v = np.linspace(x_0, x_f, pointPerLine)
    y_v = np.linspace(y_0, y_f, int(np.ceil(lenY/hatching_dist)) + 1)
    #Define mesh grid 
    x_mesh,y_mesh = np.meshgrid(x_v,y_v)
    l, w = x_mesh.shape
    #constant matrix z 
    #z = z_0 * np.ones((l,w))
    #Define slicing distance and number of parallel planes 
    #Save the multiple planes in just 3 mattrices
    numberOfPlanes = int(np.ceil(lenZ/slicing_dist)) + 1
    multipleZVector = np.linspace(z_0, z_f, numberOfPlanes)
    #z matrix for the N planes 
    lenMatrix = l * w #lenMatrix : Defined by the dimensiones of a one plane matrix
    z_const_rows = np.tile(multipleZVector, (lenMatrix,1)) #Matrix with  z constant values per row
    x_flat = x_mesh.flatten().reshape(-1,1)
    y_flat = y_mesh.flatten().reshape(-1,1)
    x_data = np.tile(x_flat, (1, numberOfPlanes))
    y_data = np.tile(y_flat, (1, numberOfPlanes))
   # z = z_const_rows * np.ones((lenMatrix, numberOfPlanes))

    return x_data, y_data, z_const_rows, pointPerLine


def y_path_optimizer(y_matrix):
    y_matrix = y_matrix.copy()
    rows, cols = y_matrix.shape
    count = 1
    while count + 1 <= rows:
        y_matrix[count, :] = y_matrix[count, :][::-1]
        count += 2
    return y_matrix


#Optimzies the writing path for the x points 
#Function parameters: 
#pointNum: Number of points per line
#vector_opt: Vector containing the x data points
def x_path_optimizer(pointNum, vector_):
    vector_opt = vector_.copy()
    count = pointNum
    while count <= len(vector_opt) - pointNum:
        #Reverse the vector 
        vector_opt[count:count + pointNum] = vector_opt[count:count + pointNum][::-1]
        #New value for counter
        count += 2*pointNum
    #Return new vector 
    return vector_opt


def flatten_to_matrix(x, y, z):
    #Concatenate the x,y,z data in order to visualize it with
    new_x = x.reshape(-1, 1)
    new_z = z.reshape(-1, 1)
    new_y = y.reshape(-1, 1)
    # Matrix representing the points to render (points per row)
    return np.concatenate((new_x, new_y, new_z), axis=1)

#Function that translate a matrix in the x axis
def x_translation(matrix, t):
    cMatrix = matrix.copy()
    x_t = cMatrix[:, 0] + t
    cMatrix[:, 0] = x_t
    return cMatrix

#Function that translate a matrix in the y axis
def y_translation(matrix, t):
    cMatrixY = matrix.copy()
    y_t = cMatrixY[:, 1] + t
    cMatrixY[:, 1] = y_t
    return cMatrixY

#Function that translate a matrix in the y axis
def z_translation(matrix, t):
    cMatrixZ = matrix.copy()
    z_t = cMatrixZ[:, 2] + t
    cMatrixZ[:, 2] = z_t
    return cMatrixZ

#translate the origing of the structure ... 
def origin_translation(matrix, x, y, z):
    new_matrix = matrix.copy()
    t1 = x_translation(new_matrix, x)
    t2 = y_translation(t1, y)
    return z_translation(t2, z)   


#Function returns information of a plane per colum
#T transposes the data  (information of a plane per row)
#x_data, y_data, z_data, points_per_line = build_planes(0, 12, 0, 12, 0, 15, hatching_dist =.2, slicing_dist = .2)
x_data, y_data, z_data, points_per_line = build_planes(0, 12, 0, 12, 0, 0, hatching_dist=.5, slicing_dist = 1)
x_data = x_data.T
y_data = y_data.T
z_data = z_data.T


#Writing optimizers
xOpt_data = x_path_optimizer(points_per_line, x_data.flatten())
yOpt_data = y_path_optimizer(y_data).flatten()
zOpt_data = z_data.flatten()
# print(xOpt_data, "\n \n")
# print(yOpt_data, "\n \n")
# print(zOpt_data, "\n \n")
print(xOpt_data.size)

#Building a line from p_0 to p_f with stepSize of 100 nm 
xL, yL, zL = build_line(np.array([0, 6, 8.01]), np.array([32, 6, 8.01]), .1)
#Build helix
x_he, y_he, z_he = build_helix(16, 8, 10000, 1) #Step size or arc length must be determined

#Concatenate the x,y,z data in order to visualize it with 
planes_matrix = flatten_to_matrix(xOpt_data,yOpt_data, zOpt_data) #Matrix representing the points to render (points per row)
line_matrix = flatten_to_matrix(xL, yL, zL)
helix_matrix = flatten_to_matrix(x_he,y_he,z_he)
#Translations
planes_matrix_tx = x_translation(planes_matrix, 20)
#Concatenate all structures in just one matrix
points_matrix = np.concatenate((planes_matrix,line_matrix,helix_matrix,planes_matrix_tx ))

np.savetxt("nanoBuild_data.txt", points_matrix, delimiter="  ")

with open('nanoBuildData.txt') as f:
    contents = f.read()

# Create random XYZ points
#10M points is the "limit", therefore we need to take a sample 
points = points_matrix
#IF points number is greater than 8M
# subset = 0.2
# selection = np.random.randint(
#     low=0, high=10000000 - 1, size=int(10000000 * subset)
# )
# points = points[selection]
xyz = points.ravel()

print(f"Number of points: {points.shape}")

# Setup VTK rendering of PointCloud
app = dash.Dash(__name__)
server = app.server

vtk_view = dash_vtk.View(
    [
        dash_vtk.PointCloudRepresentation(
            xyz=xyz,
            property={"pointSize": 2}
        )
    ]
)


app.layout = html.Div(
    style={"height": "calc(100vh - 16px)"},
    children=[html.Button("Download Text", id="btn-download-txt"),
              dcc.Download(id="download-text"), html.Div(vtk_view, style={"height": "100%", "width": "100%"})],
)


    


@app.callback(
    Output("download-text", "data"),
    Input("btn-download-txt", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dict(content=contents, filename="data_NanoBuild.txt")




if __name__ == "__main__":
    app.run_server(debug=True)
