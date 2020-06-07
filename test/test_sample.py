#!/usr/bin/env python3
import pathlib
import ytools


def test_sample():
	print(ytools.__version__)
	ytools.validate("test/sampleschema.yaml", ["test/sampledata.yaml"])
	ytools.dump("test/sampledata.yaml", path="$.metrics", yaml_options="default_flow_style: false")


def test_pathlib():
	ytools.validate(pathlib.Path("test/sampleschema.yaml"), [pathlib.Path("test/sampledata.yaml")])
	ytools.dump(pathlib.Path("test/sampledata.yaml"), path="$.metrics", yaml_options="default_flow_style: false")


if __name__ == "__main__":
	test_sample()
