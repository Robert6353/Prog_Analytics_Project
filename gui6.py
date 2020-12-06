import dash  #(version 1.12.0)
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
#warnings.filterwarnings()
# -------------------------------------------------------------------------------------
# Import the cleaned data (importing csv into pandas)
def gui(csv):
    df = pd.read_csv(csv)


# -------------------------------------------------------------------------------------
# App layout
    app = dash.Dash(__name__, prevent_initial_callbacks=True) # this was introduced in Dash version 1.12.0

# Sorting operators (https://dash.plotly.com/datatable/filtering)
    bar_choice = input("What bar chart do you want? ")
    app.layout = html.Div([
        dash_table.DataTable(
            id='datatable-interactivity',
            columns=[
                {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
                for i in df.columns
                ],
            data=df.to_dict('records'),  # the contents of the table
            editable=True,              # allow editing of data inside all cells
            filter_action="native",     # allow filtering of data by user ('native') or not ('none')
            sort_action="native",       # enables data to be sorted per-column by user or not ('none')
            sort_mode="single",         # sort across 'multi' or 'single' columns
            column_selectable="multi",  # allow users to select 'multi' or 'single' columns
            row_selectable="multi",     # allow users to select 'multi' or 'single' rows
            row_deletable=True,         # choose if user can delete a row (True) or not (False)
            selected_columns=[],        # ids of columns that user selects
            selected_rows=[],           # indices of rows that user selects
            page_action="native",       # all data is passed to the table up-front or not ('none')
            page_current=0,             # page number that user is on
            page_size=18,                # number of rows visible per page
            style_cell={                # ensure adequate header width when text is shorter than cell's text
                        'minWidth': 95, 'maxWidth': 95, 'width': 95
                        },
            style_data={                # overflow cells' content into multiple lines
                        'whiteSpace': 'normal',
                        'height': 'auto'
                        }
            ),

        html.Br(),
        html.Br(),
        html.Div(id='bar-container'),

    ])


# -------------------------------------------------------------------------------------
# Create bar chart
    @app.callback(
        Output(component_id='bar-container', component_property='children'),
        [Input(component_id='datatable-interactivity', component_property="derived_virtual_data"),
         Input(component_id='datatable-interactivity', component_property='derived_virtual_selected_rows'),
         Input(component_id='datatable-interactivity', component_property='derived_virtual_selected_row_ids'),
         Input(component_id='datatable-interactivity', component_property='selected_rows'),
         Input(component_id='datatable-interactivity', component_property='derived_virtual_indices'),
         Input(component_id='datatable-interactivity', component_property='derived_virtual_row_ids'),
         Input(component_id='datatable-interactivity', component_property='active_cell'),
         Input(component_id='datatable-interactivity', component_property='selected_cells')]
        )
    def update_bar(all_rows_data, slctd_row_indices, slct_rows_names, slctd_rows,
                   order_of_rows_indices, order_of_rows_names, actv_cell, slctd_cell):
        print('***************************************************************************')
        print('Data across all pages pre or post filtering: {}'.format(all_rows_data))
        print('---------------------------------------------')
        print("Indices of selected rows if part of table after filtering:{}".format(slctd_row_indices))
        print("Names of selected rows if part of table after filtering: {}".format(slct_rows_names))
        print("Indices of selected rows regardless of filtering results: {}".format(slctd_rows))
        print('---------------------------------------------')
        print("Indices of all rows pre or post filtering: {}".format(order_of_rows_indices))
        print("Names of all rows pre or post filtering: {}".format(order_of_rows_names))
        print("---------------------------------------------")
        print("Complete data of active cell: {}".format(actv_cell))
        print("Complete data of all selected cells: {}".format(slctd_cell))


        dff = pd.DataFrame(all_rows_data)
    
        if "Date" and bar_choice in dff:
            return [
                dcc.Graph(id='bar-chart',
                          figure=px.bar(
                              data_frame=dff,
                              x= "Date",
                              y=bar_choice,
                              ).update_layout(showlegend=False, xaxis={'categoryorder': 'total ascending'})
                          )
                ]


    # -------------------------------------------------------------------------------------
    # Highlight selected column
    @app.callback(
        Output('datatable-interactivity', 'style_data_conditional'),
        [Input('datatable-interactivity', 'selected_columns')]
        )
    def update_styles(selected_columns):
        return [{
            'if': {'column_id': i},
            'background_color': '#D2F3FF'
            } for i in selected_columns]

 
    dl = pd.read_csv('berkshire.csv')

    fig = go.Figure([go.Scatter(x=dl['Date'], y=dl['Volume'])])
    fig.show()
# -------------------------------------------------------------------------------------


    if __name__ == '__main__':
        app.run_server()

gui("berkshire.csv")
