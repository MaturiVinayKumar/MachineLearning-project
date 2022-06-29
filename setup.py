from setuptools import find_packages,setup
from typing import List

#Declaring variables for setup functions

PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="M VINAY KUMAR"
DESRCIPTION="This is my first ML project"
#PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    mention in requirements.txt file
    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list= requirement_file.readlines()
        print(requirement_list)
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
        return requirement_list
        
        #we are using find packages which id equivalent to -e . so we removed here


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    package=find_packages(),
    install_requirements=get_requirements_list()
)
