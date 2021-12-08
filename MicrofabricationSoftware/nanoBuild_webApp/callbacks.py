from dash.dependencies import Input, Output
from app import app
from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_daq as daq
import numpy as np
import dash_vtk

@app.callback(
    Output('app-1-display-value', 'children'),
    Input('app-1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    Output('numeric-input-output-1', 'children'),
    Input('my-numeric-input-1', 'value')
)
def update_output(value):
    return 'The value is {}.'.format(value)


@app.callback(Output("cardBody_params", "children"), [Input("radios", "value")])
def display_value(value):

        line_parameters = html.Div([
                html.Div([
                    # html.Div(["Empleados"], className= "col d-flex justify-content-start"),   
                    # html.Div(["Periodo"], className="col d-flex justify-content-start"),             
                    # html.Div([], className="col "),
                    html.Div([html.P("Set initial and final points in the ranges x[-100,100], y[-100,100] and z[-10,10]  (*all units are in um)")], className="row pb-2"),

                    html.Div([
                        #Set initial point ...
                        daq.NumericInput(
                            id='step_size_line',
                            min= 0,
                            max=200,
                            label='step Size',
                            labelPosition='bottom',
                            value=0.2,

                        ),


                        ], className="col"),
                    
                    html.Div([
                        #Set initial point ...
                        daq.NumericInput(
                            id='x_initialP',
                            min=-100,
                            max=100,
                            label='X (initial point)',
                            labelPosition='bottom',
                            value=1,
                            
                        ),
                        

                    ], className = "col"),
                    html.Div([
                        #Set initial point ...
                        daq.NumericInput(
                            id='y_initialP',
                            min=-100,
                            max=100,
                            label='Y (initial point)',
                            labelPosition='bottom',
                            value=1,

                            ),
                    

                    ], className="col"),
                    html.Div([
                        #Set initial point ...
                        daq.NumericInput(
                            id='z_initialP',
                            min=-10,
                            max=10,
                            label='Z (initial point)',
                            labelPosition='bottom',
                            value=1,

                            ),
                    

                    ], className="col"),
                    html.Div([
                        #Set initial point ...
                        daq.NumericInput(
                            id='x_finalP',
                            min=-100,
                            max=100,
                            label='X (final point)',
                            labelPosition='bottom',
                            value=2,

                        ),
                    

                    ], className="col"),
                    html.Div([
                        #Set initial point ...
                        daq.NumericInput(
                            id='y_finalP',
                            min=-100,
                            max=100,
                            label='Y (final point)',
                            labelPosition='bottom',
                            value=2,

                        ),
                    

                    ], className="col"),
                    html.Div([
                        #Set initial point ...
                        daq.NumericInput(
                            id='z_finalP',
                            min=-10,
                            max=10,
                            label='z (final point)',
                            labelPosition='bottom',
                            value=2,

                        ),
                    

                    ], className="col"),
                    
                
                
                ], className="row")
            ], className="container-fluid  ")


        #...........................Plane parameters .......................#
        plane_parameters = html.Div([
            html.Div([
                # html.Div(["Empleados"], className= "col d-flex justify-content-start"),
                # html.Div(["Periodo"], className="col d-flex justify-content-start"),
                # html.Div([], className="col "),
                html.Div([html.P(
                    "Set width, length and hatching distance (step size) for the plane (*all units are in um)")], className="row pb-2"),

            

                html.Div([
                    #Set initial point ...
                    daq.NumericInput(
                        id='width_plane',
                        min=0,
                        max=200,
                        label='Width',
                        labelPosition='bottom',
                        value=50,

                    ),


                ], className="col"),
                html.Div([
                    #Set initial point ...
                    daq.NumericInput(
                        id='length_plane',
                        min=0,
                        max=200,
                        label='length',
                        labelPosition='bottom',
                        value=50,

                    ),


                ], className="col"),

                html.Div([
                    #Set initial point ...
                    daq.NumericInput(
                        id='hatch_plane',
                        min=0,
                        max=200,
                        label='Hatching distance ',
                        labelPosition='bottom',
                        value=0.2,

                    ),


                ], className="col"),



            ], className="row")
        ], className="container-fluid  ")
        
        #...........................hexaedron parameters .......................#
        hexaedron_parameters = html.Div([
            html.Div([
                # html.Div(["Empleados"], className= "col d-flex justify-content-start"),
                # html.Div(["Periodo"], className="col d-flex justify-content-start"),
                # html.Div([], className="col "),
                html.Div([html.P(
                    "Set width, length, heigth, hatching and slicing distance (step size) for the hexaedron (*all units are in um)")], className="row pb-2"),



                html.Div([
                    #Set initial point ...
                    daq.NumericInput(
                        id='width_hexa',
                        min=0,
                        max=200,
                        label='Width',
                        labelPosition='bottom',
                        value=50,

                    ),


                ], className="col"),
                html.Div([
                    #Set initial point ...
                    daq.NumericInput(
                        id='length_hexa',
                        min=0,
                        max=200,
                        label='length',
                        labelPosition='bottom',
                        value=50,

                    ),


                ], className="col"),
                html.Div([
                    #Set initial point ...
                    daq.NumericInput(
                        id='heigth_hexa',
                        min=0,
                        max=20,
                        label='Heigth',
                        labelPosition='bottom',
                        value=5,

                    ),


                ], className="col"),

                html.Div([
                    #Set initial point ...
                    daq.NumericInput(
                        id='hatch_hexa',
                        min=0,
                        max=200,
                        label='Hatching distance ',
                        labelPosition='bottom',
                        value=0.2,

                    ),


                ], className="col"),

                html.Div([
                    daq.NumericInput(
                        id='slicing_hexa',
                        min=0,
                        max=200,
                        label='Slicing distance ',
                        labelPosition='bottom',
                        value=0.2,

                    ),


                ], className="col"),




            ], className="row")
        ], className="container-fluid  ")


        #parameters list
        paramsList = [line_parameters, plane_parameters, hexaedron_parameters]
        
        return paramsList[value - 1]


def flatten_to_matrix(x, y, z):
    #Concatenate the x,y,z data in order to visualize it with
    new_x = x.reshape(-1, 1)
    new_z = z.reshape(-1, 1)
    new_y = y.reshape(-1, 1)
    # Matrix representing the points to render (points per row)
    return np.concatenate((new_x, new_y, new_z), axis=1)

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


@app.callback(
    Output('vtk_test', 'children'),
   # Output('build_structure', 'n_clicks'),
    Output('step_size_line', 'value'),
    Output('x_initialP', 'value'),
    Output('y_initialP', 'value'),
    Output('z_initialP', 'value'),
    Output('x_finalP', 'value'),
    Output('y_finalP', 'value'),
    Output('z_finalP', 'value'),
    Input('step_size_line', 'value'),
    Input('x_initialP', 'value'),
    Input('y_initialP', 'value'),
    Input('z_initialP', 'value'),
    Input('x_finalP', 'value'),
    Input('y_finalP', 'value'),
    Input('z_finalP', 'value'),
    Input('build_structure', 'n_clicks')
)
def showing_line(stepSize,xInitial,yInitial,zInitial,xFinal,yFinal,zFinal,clicks):
    
    if  clicks > 0:

        #Building a line from p_0 to p_f with stepSize of 100 nm
        initial_point = np.array([xInitial, yInitial, zInitial])
        final_point = np.array([xFinal, yFinal, zFinal])
        xL, yL, zL = build_line(initial_point, final_point, stepSize)
        line_matrix = flatten_to_matrix(xL, yL, zL)
        pointsData = line_matrix.ravel()
        np.savetxt("nanoBuildData.txt", line_matrix, delimiter="  ")
        return dash_vtk.View(
            [
                dash_vtk.PointCloudRepresentation(
                    xyz=pointsData,
                    property={"pointSize": 2}
                )
            ]
        ), stepSize, xInitial, yInitial,zInitial,xFinal,yFinal,zFinal
    else:
        return 'No se ha confirmado la construccion',.1,1,1,1,2,2,2


@app.callback(
    Output("download-text", "data"),
    Input("downloadData", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    with open('nanoBuildData.txt') as f:
        contents = f.read()
    return dict(content=contents, filename="nanoBuildDataFinal.txt")


