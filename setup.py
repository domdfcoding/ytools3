import setuptools
import pathlib

version = "1.0.0"

setuptools.setup(
		name="ytools",
		packages=["ytools"],
		# data_files = [('schema', ['schema/transformatorschema.yaml'])],
		install_requires=pathlib.Path('requirements.txt').absolute().read_text().split("\n"),
		version="1.0.0",
		description=(
				'Command-line tool for selectively dumping nodes from '
				'`yaml` (or `json`) documents in `yaml` or `json` format.'
				),
		long_description=pathlib.Path('README.md').read_text(),
		long_description_content_type="text/markdown",
		author='Jakob Stemberger',
		author_email='yaccob@gmx.net',
		license='Apache 2.0',
		url=f'https://github.com/yaccob/ytools',
		download_url=f'https://github.com/yaccob/ytools/archive/{version}.tar.gz',
		keywords=[
				'yaml',
				'json',
				'transform',
				'xslt',
				'jsonpath',
				'json-path',
				'dump',
				'convert',
				'validate',
				'schema',
				],
		classifiers=['Programming Language :: Python :: 2.7'],
		entry_points={"console_scripts": ['ytools = ytools.__main__:main']},
		)
