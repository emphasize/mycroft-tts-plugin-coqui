#!/usr/bin/env python3
from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

PLUGIN_ENTRY_POINT = 'coqui_remote = mycroft_tts_plugin_coqui:CoquiRemoteTTSPlugin'
setup(
    name='mycroft-tts-plugin-coqui',
    version='0.1',
    description='A tts plugin for mycroft, connecting to a Coqui TTS server',
    long_description=README,
    long_description_content_type="text/markdown",
    url='http://github.com/emphasize/mycroft-tts-plugin-coqui',
    author='Swen Gross',
    author_email='private@private.org',
    license='Apache-2.0',
    packages=['mycroft_tts_plugin_coqui'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='mycroft plugin tts coqui',
    entry_points={'mycroft.plugin.tts': PLUGIN_ENTRY_POINT}
)