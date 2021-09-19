```
This can be used to expose the metadata of the data that is being uploaded via the Widgets
Mostly its advisable to expose the Data Model of the data and implement validations
```

def describe_datamodel():
  info_level = toggle.value
  if info_level != {}:
    df = df_converter()
    ### you can also use below if you want to use the uploaded file to retrieve the datamodel
    ### pdf = pd.read_csv(file_name, delimiter='~',low_memory=Flase, encoding='unicode_escape',
    #######    usecols=["X","Y","A","B"]   Dictionary of Columns that you want to use to describe
    
    with out:
      out.clear_output()
      print('\n ------ The Model Metadata has been listed below: ------\n'.format(
        info_level))
      if df is not None:
        if info_level =='Info':
          print(df.info(verbose=True))
         elif info_level == 'Stats':
          print (df.describe()
         elif info_level =='Preview':
                 print(df.head(10))
          else:
                 print("There seems to be a problem")
                 
