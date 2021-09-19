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

label1=widgets.Label(value="Upload File:",layout=items_layout)
label1_upload= widgets.FileUpload(accept="", multiple=False,layout=items_layout)

delimiters = widgets.RadioButtons(
options =['~',';',','],
description='Seperator',
diabled=False
)

```
This specific code helps implementing the UI controls.
User can upload files, select a date and perform analytics operations
```
header = Button(description='Sample',
         layout=Layout(width='auto',grid_area='header'),
         style=ButtonStyle(button_color='ligtblue'))
box_layout = Layout(display='flex',
                    flex_flow='column',
                    align_items='stretch',
                    border='solid',
                    width='60%')
eraser = widgets.SelectMultiple(
         options=['tab','"'],
         value=['tab'],
         description='Eraser:',
         disabled=False)


rows = widgets.IntSlider(
       value=0,
       step=1,
       description='# of lines:',
       disabled=False,
       continuous_update=False,
       oritentation='horizontal',
       readout=True,
       readout_format='d')

### button_upload = widgets.Button(
#                   description='Upload',
#                   disable='False',
#                   button_style='warning',
#                   tooltip='Click to Upload File',
#                   icon='check')
#button_upload.on_click(upload_clicked)

accordion =widgets.Accordian(children=[
             widgets.VBox([widgets.HBox([prompt_date,input_date]), widgets.HBox([label1,label1_upload])], layout=box_layout),
             widgets.VBox([delimiters, eraser]),
             rows])
accordion.set_title(0,'File Upload')
acordion.set_title(1,'Delimiter Supported')
accordion.set_title(2,'Rows to Skip')
accordion_box = widgets.VBox([
               accordion,
               widgets_HBox([button_upload]),
               out
])
tab 
