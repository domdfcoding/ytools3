#!/usr/bin/env python3
# stdlib
import pathlib

# this package
import ytools


def test_sample():
	print(ytools.__version__)
	ytools.validate("tests/sampleschema.yaml", ["tests/sampledata.yaml"])
	ytools.dump("tests/sampledata.yaml", path="$.metrics", yaml_options="default_flow_style: false")


def test_pathlib():
	ytools.validate(pathlib.Path("tests/sampleschema.yaml"), [pathlib.Path("tests/sampledata.yaml")])
	ytools.dump(pathlib.Path("tests/sampledata.yaml"), path="$.metrics", yaml_options="default_flow_style: false")


if __name__ == "__main__":
	test_sample()
