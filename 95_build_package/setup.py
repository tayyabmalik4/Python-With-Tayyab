# ////////if we want to build own package then we using the setup module and creat over own pakage like sk-learn module tanserflow and pandas, numpy
# ////////definition of setuptools--------Setuptools is a package development process library designed to facilitate packaging Python projects by enhancing the Python standard library distutils (distribution utilities). It includes: Python package and module definitions.
# ////////ther are 2 tools first setup and othe is find_package
# ////////setup module definition------The setup script is the centre of all activity in building, distributing, and installing modules using the Distutils. The main purpose of the setup script is to describe your module distribution to the Distutils, so that the various commands that operate on your modules do the right thing. As we saw in section A Simple Example above, the setup script consists mainly of a call to setup(), and most information supplied to the Distutils by the module developer is supplied as keyword arguments to setup().
# ///////find_package------ if there are many pakcges and we want to setup in just one whell than we use this module
# ////////there are meta-data which we use in the package details
# (1)-Name
# (2)-version
# (3)-author
# (4)-author_email
# (5)-maintainer
# (6)-maintainer_email
# (7)-url
# (8)-description
# (9)-long_discription
# (10)-download_url
# (11)-classifiers
# (12)-platforms
# (13)-keywords
# (14)-license 
# /////first of all we import setup from setuptools than write the code which we want to creat a module than we install 
# after the competion your setup than we install whell using pip
# than the command which we run is------python setup.py bdist_wheel


# //////////readme file definition///////////////A README file contains information about other files in a directory or archive of computer software. A form of documentation, it is usually a simple plain text file called Read Me, READ.ME,[1] README.TXT,[2][1] README.md[1] (for a text file using markdown markup), README.1ST[1]  – or simply README.[1]
#------------- The file's name is generally written in uppercase letters. On Unix-like systems in particular this makes it easily noticed – both because lowercase filenames are more common, and because traditionally the ls command sorts and displays files in ASCII-code order, so that uppercase filenames appear first.[
# /////////licanse file definition-----Public repositories on GitHub are often used to share open source software. For your repository to truly be open source, you'll need to license it so that others are free to use, change, and distribute the software.

from setuptools import setup 
setup(name="packagetayyab",
version="1.0",
description="this is code with tayyab",
long_description="this is the very long description about my package",
author="Tayyab",
# packages=['95_build_package'],
packages=['packagetayyab'],
install_required=[])

