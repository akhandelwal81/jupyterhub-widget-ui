import matplotlib.pyplot as plt
%matplotlib inline
import ipywidgets as ipywidgets
from ipywidgets import Layout, Button, Box, ButtonStyle, GridspecLayout
from IPython.display import display

### Initialise a Tab Widget

tab = widgets.Tab()


## Define a Layout of the various contols
# This is used in conjunction of layout attribute that all interactive widgets have.
# This helps in setting up the CSS properties that impacts how widgets are laid Out
# Quite a few CSS propoerties are exposed including - height, width, ma_height, max_width, min_height and min_width

items_layout = Layout(width = '20%', height='30px')

# Once the Tab has been initialised, you can initialise a Label attribute/control using the above Layout and propoerties

prompt_date = widgets.Label(value= "Date:", layout = items_layout)

# Associated with the prompt_date, you can lay out a DatePicker for user to select the date. The DatePicker can be customised to only display months, year or DDMMYYYY format.
input_date = widgets.DatePicker(description='', disabled=False, layout=items_layout)

# This is a display widget to print all Application Messages on the Console
out = widgets.Output(layout={'border':'2px solib black'})

#####This is sample code for a  Jupyter Widgets based UI that can be used for user to select a Date
# Upload some files
# Click Button to trigger an Upload
# Support CSV files with different types of delimiters like '~',';',','
