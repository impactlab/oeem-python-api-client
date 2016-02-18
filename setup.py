from setuptools import setup

setup(name='oeem_uploader',
      version='0.1',
      description='An OEE datastore API client',
      url='http://github.com/impactlab/oeem_uploader',
      author='Hunter Owens',
      author_email='hunter@theimpactlab.co',
      license='MIT',
      packages=['oeem_uploader'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
