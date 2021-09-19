```
This is used to parse the content for the files being uploaded.
Uses the metadata to find the type of file and then uses eraser value
```


def content_parser():
  typ, content ="",""
  up_value = upload_file.value
  for i in up_value.keys():
    typ = up_value[i]["metadata"]["type"]
    if typ =="text/csv":
      content = up_value[i]["content"]
      content_str = str(content,'utf-8')
      
     if eraser.value != {}:
      for val in eraser.value:
        if val =="tab":
          content_str = content_str.replace("/t","")
         else:
          content_str = content_ste.replace(val,"")
      if content_str != "":
        str_io = StringIO(content_str)
        return str_io
      
                          
