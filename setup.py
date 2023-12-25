from setuptools import find_packages,setup
from typing import List

END_HYPEN = '-e .'
def get_requirements(file_path:str) -> List[str] :
    '''
    function to return all requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if END_HYPEN in requirements:
        requirements.remove(END_HYPEN)

    return requirements

setup(
    name = 'genericML',
    version = '0.1',
    author = "Mayur Jadhav",
    packages = find_packages(),
    install_required = get_requirements('requirements.txt')
)