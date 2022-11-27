# Obfuscated Python Packaging
To convert Python codes to obfuscated python wheel package.<br/>
 
##	PREREQUISITE
Step 1. Install Python 3.8 and the latest PIP and Setuptool.<br/>
Step 2. Install the latest version of Nuitka using following command:<br/>
`$ python3 -m pip install -U nuitka`

3	CREATING BINARY FILE
Step 1. Create a folder as a root, create a file named setup.py, and copy required python modules to the sub folder. Inside IntelliJ IDEA, we created a project for multiple NLP programmes as shown in the below Figure. The folder structure of language module is displayed in the below Figure:
 
** Can be downloaded from: http://git.mimos.local/social-intelligence/engines/python-engine
Step 2. Create an empty python file in the subfolder and name it __init__.py.
Step 3. Change the content of setup.py to (example for language modue):

Step 4. Run the following command:
$ python3 -m nuitka --module <package_name>--include-package=<package_name>
For example, the below command should be used for the language program:
$ python3 -m nuitka --module mimos_language --include-package=mimos_language
After successfully running the above command, mimos_language.cpython-38-x86_64-linux-gnu.so will be created.
4	PACKAGING
Step 1. Create a folder as a root, create setup.py and MANIFEST.in files, and copy your .so file to the folder. Inside IntelliJ IDEA, the folder structure will be similar to the below Figure:
 
** Can be downloaded from: http://git.mimos.local/social-intelligence/engines/python-engine-wheel
Step 2. Create an empty python file in the subfolder and name it __init__.py.
Step 3. Change the content of setup.py (example for language module) to:

Step 4. Change the content of  MANIFEST.in to:
recursive-include mimos_language.cpython-38-x86_64-linux-gnu.so
include *.so
Step 5. Run the following command  in the  root folder of package:

After successfully running the above command, dist/mimos-1.0-py3-none-any.whl will be created.
5	INSTALLING CUSTOMIZED PACKAGE
Step 1. Copy the .whl file from dist folder to your device. 

Step 2.  Run the following command:

 

Example of language module: 
  
6	UTILIZING CUSTOMIZED PACKAGE


Import required functions using import command. For example:


7	LIST OF WARNINGS/ERROR MESSAGES/
ERROR HANDLING
#	Warning/Error Message
1	Error Message:     : libm.so.6: version `GLIBC_xx.xx' not found
	Description:	The version of GNU C Library (glibc) on development device should equal or older than the version of glibc on deployment device. It applies to both Nuitka and PyInstaller.
	Solution:	1-	Run “apt-cache policy libc6” on the deployment device. It displays installed version and the latest candidate version.
2-	If the displayed candidate version is equal or higher that the version of glibc on the development device, run “apt-get install libc6=candidate_version”
3-	If the displayed candidate version is lower that the version of glibc on the development device, the linux distribution should be updated.
	



U
