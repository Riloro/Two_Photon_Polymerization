import dash
import dash_html_components as html
import dash_vtk
import pyvista as pv
from dash_vtk.utils import to_mesh_state
from pyvista import examples
try:
    # VTK 9+
    from vtkmodules.vtkImagingCore import vtkRTAnalyticSource
except ImportError:
    # VTK =< 8
    from vtk.vtkImagingCore import vtkRTAnalyticSource


# Use VTK to get some data
data_source = vtkRTAnalyticSource()
print(type(data_source))
data_source.Update()  # <= Execute source to produce an output
dataset = data_source.GetOutput()

#Reading STL files with pyvista .... 
mesh_pv = pv.read(r'C:/Users/Public/PI/Microscope/E-727/GCS_LabVIEW/MicrofabricationSoftware/3D_examples_models/dinolowRes.stl')
#grafon = examples.download_dragon()
# Use helper to get a mesh structure that can be passed as-is to a Mesh
# RTData is the name of the field
mesh_state = to_mesh_state(mesh_pv)

print("Mesh state", type(mesh_state))
content = dash_vtk.View([
    dash_vtk.GeometryRepresentation([
        dash_vtk.Mesh(state=mesh_state)
    ]),
])

# Dash setup
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    style={"width": "100%", "height": "400px"},
    children=[content],
)

if __name__ == "__main__":
    app.run_server(debug=True)
