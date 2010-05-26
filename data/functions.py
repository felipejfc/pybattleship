import os

data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, 'images'))

def filepath(filename):
    return os.path.join(data_dir, filename)

#image.get_size
