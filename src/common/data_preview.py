```
This function is used to preview the data of the file being uploaded.
You can add any sort of comparision or dataframe operations as part of preview
This could well may involve a preview if data quality or data comparision between current file and older file

```

def data_preview():
  df = df_converter()
  
  #### Or you can use a pandas dataframe operation to read a csv
  
  with out:
    out.clear_output()
    print('/n ---- Describe the dataframe ------\n')
    if pdf is not None:
      print(pdf.head(10))
     else:
      print("There seems to be an issue with the data")
      
