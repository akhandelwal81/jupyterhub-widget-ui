```
This is is used to read a csv file with different types of delimiter and initialise a pandas dataframe
```

def df_converter():
  
  content = content_parser()
  import pandas as pd
  
  if content is not None:
    
    df = pd.read_csv(content, sep=delimit.value, index_col=False, skiprows=rows.value)
    return df
  
  else:
    return None
  
  
