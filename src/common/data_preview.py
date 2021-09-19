```
This function is used to preview the data of the file being uploaded.
You can add any sort of comparision or dataframe operations as part of preview
This could well may involve a preview if data quality or data comparision between current file and older file

```

def data_preview():
  df = df_converter()
  
    ### you can also use below if you want to use the uploaded file to retrieve the datamodel
    ### pdf = pd.read_csv(file_name, delimiter='~',low_memory=Flase, encoding='unicode_escape',
    #######    usecols=["X","Y","A","B"]   Dictionary of Columns that you want to use to describe
  
  with out:
    out.clear_output()
    print('/n ---- Describe the dataframe ------\n')
    if pdf is not None:
      print(pdf.head(10))
     else:
      print("There seems to be an issue with the data")
      
