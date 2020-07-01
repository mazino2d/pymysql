from setuptools import setup, find_packages

setup(name='tlksql',
      version='0.0.3',
      license='MIT',
      author='Khoi Dang Do',
      author_email='mazino2d@gmail.com',
      url='https://github.com/mazino2d/pymysql',
      description='Easy to query mysql database with lambda function',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      keywords='sql, connection-pool, lambda',
      packages=["tlksql"],
      install_requires=['pymysql-pooling>=1.0.6'],
      python_requires='>=3.5, <4',
)
