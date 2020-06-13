#!/usr/bin/env python3
#
#  __init__.py
"""
Library for validating `yaml` files against schema and selectively dumping nodes from `yaml` (or `json`) documents in `yaml` or `json` format.
"""
#
#  Copyright (c) 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#  Copyright (c) Jakob Stemberger <yaccob@gmx.net>

#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

__author__ = "Dominic Davis-Foster"
__copyright__ = "2020 Dominic Davis-Foster"

__license__ = "Apache2.0"
__version__ = "3.0.0"
__email__ = "dominic@davis-foster.co.uk"

# stdlib
import collections
import json
import pathlib
from typing import Callable, Dict, Iterable, Union

# 3rd party
import jsonschema  # type: ignore
import yaml
from jsonpath_ng import ext as jsonpath  # type: ignore
from typing_extensions import TypedDict
from yaml import constructor, resolver

__all__ = ["validate", "dump", "optiondefaults", "__version__"]

optiondefaults = {
		"yaml": "{explicit_start: True, explicit_end: True, allow_unicode: True}",
		"json": "{indent: 2, encoding: utf-8}",
		"python": "{}"
		}


def dict_constructor(loader, node) -> Dict:
	return dict(loader.construct_pairs(node))


def orderedDict_constructor(loader, node, deep=False):
	data = collections.OrderedDict()
	yield data

	if isinstance(node, yaml.MappingNode):
		loader.flatten_mapping(node)

	data.update(collections.OrderedDict(loader.construct_pairs(node, deep)))


class Encoder(TypedDict):
	dumper: Callable
	kwargs: str
	yaml_constructor: Callable


def validate(
		schemafile: Union[str, pathlib.Path],
		datafiles: Iterable[Union[str, pathlib.Path]],
		encoding: str = 'utf-8',
		):
	schemafile = pathlib.Path(schemafile)

	schema = yaml.load(schemafile.read_text(encoding=encoding), Loader=yaml.FullLoader)

	for filename in datafiles:
		for document in yaml.load_all(
				pathlib.Path(filename).read_text(encoding=encoding),
				Loader=yaml.FullLoader,
				):
			try:
				jsonschema.validate(document, schema, format_checker=jsonschema.FormatChecker())
			except jsonschema.exceptions.ValidationError as e:
				e.filename = str(filename)
				raise e


def dump(
		datafile: Union[str, pathlib.Path],
		path: str = '$',
		format: str = 'yaml',
		yaml_options: str = optiondefaults['yaml'],
		json_options: str = optiondefaults['json'],
		encoding: str = 'utf-8',
		):

	encoders: Dict[str, Encoder] = {
			"yaml": {
					"dumper": yaml.dump,
					"kwargs": yaml_options,
					"yaml_constructor": orderedDict_constructor,
					},
			"json": {
					"dumper": json.dumps,
					"kwargs": json_options,
					"yaml_constructor": orderedDict_constructor,
					},
			"python": {
					"dumper": (lambda x, **kwargs: x),
					"kwargs": '{}',
					"yaml_constructor": dict_constructor,
					},
			}

	yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, encoders[format]["yaml_constructor"])

	if format == "json":
		yaml.add_constructor('tag:yaml.org,2002:timestamp', yaml.constructor.SafeConstructor.construct_yaml_str)

	yaml.add_representer(collections.OrderedDict, lambda dumper, data: dumper.represent_dict(data.items()))

	documents = yaml.load_all(
			pathlib.Path(datafile).read_text(encoding=encoding),
			Loader=yaml.FullLoader,
			)

	formatoptions = dict(
			yaml.load(optiondefaults[format], Loader=yaml.FullLoader),
			**yaml.load(encoders[format]["kwargs"], Loader=yaml.FullLoader)
			)

	for document in documents:
		for match in jsonpath.parse(path).find(document):
			print(encoders[format]["dumper"](match.value, **formatoptions))
