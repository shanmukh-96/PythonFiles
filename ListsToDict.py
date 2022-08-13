# Converting two Lists to dictionary

#input:
#names = ["Ram","Rao","Raj"]
#marks = [98,97,90]

#output:
#{"Ram" : 98, "Rao" : 97, "Raj" : 90}

def list_to_dict():
    names = ["Ram","Rao","Raj"]
    marks = [98,97,90]
    
    output = dict(zip(names, marks))
    
    print(output)
    
list_to_dict()