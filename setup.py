

from setuptools import setup, find_packages
  
# reading long description from file 
with open('DESCRIPTION.txt') as file: 
    long_description = file.read() 
  
  
# specify requirements of your package here 
#REQUIREMENTS = [] 
  
# some more details 
CLASSIFIERS = [ 
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers', 
    'Topic :: Internet', 
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    ] 
  
# calling the setup function  
setup(name='wsnFault', 
      version='1.0.0', 
      description='Fault detection', 
      long_description="WSN", 
      url='https://github.com/deepak7376/wsnFault', 
      author='Deepak Yadav', 
      author_email='dky.united@gmail.com', 
      license='MIT', 
      packages=find_packages(), 
      classifiers=CLASSIFIERS, 
      #install_requires=REQUIREMENTS, 
      keywords='wsn fault statistical',
      include_package_data=True,
      zip_safe=False,
      python_requires='>=3'

      ) 


