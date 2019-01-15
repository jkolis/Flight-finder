import pip

def install(package):
    pip.main(['install', package])

install('networkx')
install('pandas')
install('PySide2')
install('xlrd')
