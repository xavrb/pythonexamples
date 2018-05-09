import os

def print_directory_contents(sPath):
    """
    This function takes the name of a directory 
    and prints out the paths files within that 
    directory as well as any files contained in 
    contained directories. 

    This function is similar to os.walk. Please don't
    use os.walk in your answer. We are interested in your 
    ability to work with nested structures. 
    """
    
    for o in os.listdir(sPath):
        
        if not(os.path.isfile(os.path.join(sPath, o))):
            print("I'm on " + str(o) + " now.")
            print_directory_contents(os.path.join(sPath, o))
        else:
            print("File: "+ os.path.join(sPath, o)+"\n")
    return 0




print_directory_contents(input("Ingrese directorio\t>>\t"))
