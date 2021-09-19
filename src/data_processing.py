```
On Click of the Button on the UI, the method will be called and it can do potentially a number of things

You can decide to upload a zipped file and this function can first help with pre-processing by unzipping the file
It can also validate the file name and the schema of the data within the file
Once it has passed the validations , it can actually perform data analytics using pandas, arrows etc
Finally, you can decide to write the file to the file system which could be Unix, Windows or Hadoop

```

define data_process():
    
    base_location=Path('/home/base/file/')
    if input_date.value is None:
        with out:
            out.clear_output()
            print("Select an Input Date for which the file needs to be uploaded"
                  
                  ## You can very well decide to retreieve the date from a column in the file. This could then well be coded accordingly where the data from the file is read and a distinct 
                  ## value from pandas dataframe can be used to assign an input date
      else:
        input = input_date.strftime('%Y-%m-%d')
        input_int = int(input.strftime('%Y%m%d'))
        target_location=os.path.join(base_location,input)
                  
        #### Check of the path exists.
        ## Create the required directory if the path doesn't exists
                  
        if not os.path.exists(target_location):
                  os.mkdir(target_location)
         
        ### Above code will create a directory for the specific date and make it ready for the file to be uploaded.
                  
        if upload_file.value ==={}:
            with out:
                print("No File to be uploaded")
         else:
                  filename = upload_file.metadata[0]["name"]
                  file_to_save = os.path.join(target_location,filename)
                  with opne(file_to_save,'wb') as f:
                    f.write(upload_file.data[0])
                
          #### Above code writes the file to the location of your choice
                  
          ### Now check if the file is a zipped/compressed file.
                  ## if Its a compressed file, then unzip it and rename it
                  
                  if zipfile.is_zipfile(file_to_save):
                  
                    zf = ZipFile(file_to_save,'r')
                    for name in zf.namelist():
                    ####Check for the file in zipped files
                  
                        fh = zf.extract(name,target_location)
                        fname = os.path.basename(fh)
                  
                         with out:
                            print("Unzipped File:" + fname)
                  
      
               
                      zf.close()
