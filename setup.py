from setuptools import setup, find_packages

setup(
    name='yomero-image-to-video',
    version='0.1.0',
    description='Converts a sequence of images into a video',
    author='yomero',
    author_email='yomero@gmail.com',
    packages=find_packages(),
    install_requires=[
        line.strip() for line in open('requirements.txt')
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
