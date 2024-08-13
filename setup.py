# from setuptools import find_packages,setup
# from typing  import List
# #meta data information about the entire project

# def get_requirements(file_path:str)->List[str]:#1 what kinda of input parametrer 2.
#     '''
#     this function will  returnn the list of requirements
#     '''
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()# in this line while reaing the text in the requirement.txt it will eventually add the \n in the end of the word so we have to use replace
#         requirements=[req.replace("\n"," ") for req in requirements]
        
        
#         if  "-e ." in requirements:
#             requirements.remove("-e .")
#     return requirements

# setup(
    
#     name="mlproject",
#     version="0.0.1",
#     author = "ARUN",
#     author_email="arunjustin45@gmail.com",
#     packages=find_packages(),
#     install_requires = get_requirements('requirements.txt')
    
# )
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # requirements = [req.strip() for req in requirements]
        
        # if "-e ." in requirements:
        #     requirements.remove("-e .")
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('-e')]

    
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="ARUN",
    author_email="arunjustin45@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
