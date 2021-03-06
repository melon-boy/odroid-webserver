from setuptools import setup, find_packages

    
setup(name='ffmpeg_pywrapper',
      version='1.0',
      description='The FFmpeg Python Wrapper',
      long_description='A user-friendly ffmpeg wrapper for Python.',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
      ],
      install_requires=['docutils>=0.3'],
      keywords='ffmpeg ffprobe wrapper video audio enconding decoding transcoding codec stream channel',
      url='http://github.com/themelon-boy/ffmpeg_pywrapper',
      author='Marco Espinosa',
      author_email='marcoantonio.espinosa@gmx.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      package_data={'ffmpeg_pywrapper': ['*.txt'],},
      zip_safe=False)