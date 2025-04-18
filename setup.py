''' The setup.py file will help to packaging and distributing python projects'''

from setuptools import find_packages, setup 
from typing import List 

def get_requirements() -> List[str]:
    requirement_list : List[str] = []
    """ This function will return list of requirements"""
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
            
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_list


print(get_requirements())

setup(
    name = "customer_segmentation",
    version = "0.0.1",
    author = "erandawi",
    author_email= "erandalakshan3567@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)