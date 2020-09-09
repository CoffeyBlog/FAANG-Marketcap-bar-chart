import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background':'#111111', 'text':'#7FDBFF', }


app.layout = html.Div(children=[
    html.H1('2020 Big Tech Marketcap', style={'textAlign': 'center',
                                         'color':colors['text']}),
    dcc.Graph(id='example',
                figure={'data':[
                {'x':[1,2,3], 'y':[2,4,15], 'type': 'bar', 'name':'Facebook'},
                {'x':[1,2,3], 'y':[4,8,12], 'type': 'bar', 'name':'Amazon'},
                {'x':[1,2,3], 'y':[4,8,12], 'type': 'bar', 'name':'Apple'},
                {'x':[1,2,3], 'y':[2,4,15], 'type': 'bar', 'name':'Netflix'},
                {'x':[1,2,3], 'y':[4,8,12], 'type': 'bar', 'name':'Google'}
                ],
                    'layout':{
                        'plot_bgcolor':colors['background'],
                        'paper_bgcolor':colors['background'],
                        'font':{'color':colors['text']},
                        'title':'FAANG Stocks by Marketcap'}})
],
    style={'backgroundColor':colors['background']}



)

if __name__ == '__main__':
    app.run_server()

