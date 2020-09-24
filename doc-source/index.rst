########
ytools3
########

.. start short_desc

**Library for validating `yaml` files against schema and selectively dumping nodes from `yaml` (or `json`) documents in `yaml` or `json` format.**

.. end short_desc

This is a port of ``ytools`` (https://github.com/yaccob/ytools ), which was Python 2 only, to Python 3.

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |travis| |actions_windows| |actions_macos| |coveralls| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| rtfd-shield::
	:project: ytools3
	:alt: Documentation Build Status

.. |docs_check| actions-shield::
	:workflow: Docs Check
	:alt: Docs Check Status

.. |travis| travis-shield::
	:travis-site: com
	:alt: Travis Build Status

.. |actions_windows| actions-shield::
	:workflow: Windows Tests
	:alt: Windows Tests Status

.. |actions_macos| actions-shield::
	:workflow: macOS Tests
	:alt: macOS Tests Status

.. |requires| requires-io-shield::
	:alt: Requirements Status

.. |coveralls| coveralls-shield::
	:alt: Coverage

.. |codefactor| codefactor-shield::
	:alt: CodeFactor Grade

.. |pypi-version| pypi-shield::
	:project: ytools3
	:version:
	:alt: PyPI - Package Version

.. |supported-versions| pypi-shield::
	:project: ytools3
	:py-versions:
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| pypi-shield::
	:project: ytools3
	:implementations:
	:alt: PyPI - Supported Implementations

.. |wheel| pypi-shield::
	:project: ytools3
	:wheel:
	:alt: PyPI - Wheel

.. |license| github-shield::
	:license:
	:alt: License

.. |language| github-shield::
	:top-language:
	:alt: GitHub top language

.. |commits-since| github-shield::
	:commits-since: v3.0.1
	:alt: GitHub commits since tagged version

.. |commits-latest| github-shield::
	:last-commit:
	:alt: GitHub last commit

.. |maintained| maintained-shield:: 2020
	:alt: Maintenance

.. |pre_commit| pre-commit-shield::
	:alt: pre-commit

.. end shields




Features
---------


* Output ``yaml`` as ``json`` or ``python``

* Output ``json`` as ``yaml`` or ``python`` (provided that there are no duplicate mapping entry in the ``json`` source)

* Extract particular nodes from ``yaml`` and ``json`` files.

	+ If ``yaml`` is used as output format (default) the output is a valid ``yaml`` document.

* Validate ``yaml`` and ``json`` documents.

	+ The ``json-schema`` can be provided in ``yaml`` format as well, which improves readability and writability.

* Preserve order of mapping-keys in ``yaml`` and ``json`` output.

* Multi-document support

	+ Multiple input files

		- ... as well as multiple ``yaml`` documents within a file
		- ... and a combination of both


Installation
---------------

.. start installation

.. installation:: ytools3
	:pypi:
	:github:

.. end installation

.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	API Reference<docs>
	Source
	Building

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/ytools3>`__

.. end links
