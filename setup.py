import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-carloancalculator',
    version='0.0.7',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Car Loan Auto Loan Payment Calculator - Calculate financing on a new car including trade-in and taxes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['carloancalculator'],
    packages=['mindpowered_carloancalculator'],
    package_dir={'mindpowered_carloancalculator': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
