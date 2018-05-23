from setuptools import setup, find_packages

setup(name='vmware',
      license='MIT',
      packages=find_packages(where="lib"),
      install_requires=[
            "pyVmomi",
            "suds-jurko",
            "tabulate",
            "lxml",
            "pyOpenSSL"
      ]
)
