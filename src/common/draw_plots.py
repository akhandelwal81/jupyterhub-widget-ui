```
This function is use to plot the data using 2D views
Allows the user to select the X and Y Axis and then based on the type of Plot selected , a plot is drawn using representative data
```

def draw_plots():
  graph = graph_type.value
  if graph != {}:
    df = df_converter()
    
      ### you can also use below if you want to use the uploaded file to retrieve the datamodel
    ### pdf = pd.read_csv(file_name, delimiter='~',low_memory=Flase, encoding='unicode_escape',
    #######    usecols=["X","Y","A","B"]   Dictionary of Columns that you want to use to describe
    
    x_axis.options = df.columns  # This can be restricted to specific dimensional attributes
    
    y_axis.options = df.columns # This can be restricted to specific measures
    
    with out:
      out.clear_output()
      print('\n ------------Plot ------------\n'.format(graph))
      
      if (df is not None):
        df = df.head(50)
        height = df[y_axis.value]
        
        bars = df[x_axis.(len(height))
        plt.figure(figsize=(10,4))
        
          if graph == 'Bar Chart':
            plt.bar(y_pos,
                    height,
                    color=color.picker.value
                   )
        
            plt.xticks(y_pos,bars)
          
          elif graph =='Line Chart':
                  plt.plot(
                    bars,
                    height,
                    color=color_picker.value,
                    marker='o',
                    linestyle='solid'
                  )
                  
                  plt.xticks(bars)
                  
            plts.show()
                  
                  
                  
                  
                  
                  
                  
                  
          
                  
         
