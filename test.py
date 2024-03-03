from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requiremet(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

requirements_file = os.path.join(".", "requirements_dev.txt")
get_requirement(requirements_file)