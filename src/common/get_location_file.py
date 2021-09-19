```
This is used to define static information about the files when they get uploaded.
You may have a staging location, processed location and may be downstream location
```

def get_location(env):
    if env =='x':
        return {'inbound': '/home/x/k1/y1/',
                 'processed' : '/home/x/k1.y1.p1',
                 'env' : 'env'}
    elif env =='dev':
        return {'inbound': '/home/dev/k1/y1/',
                 'processed' : '/home/dev/k1.y1.p1',
                 'env' : 'env'}
        
