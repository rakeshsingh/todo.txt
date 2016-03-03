clear_pyc:
	find . -name '*.pyc' -delete

tag:
	@t=`python setup.py  --version`;\
	echo v$$t; git tag v$$t

changelog:
	@git log --first-parent --pretty="format:* %b" v`python setup.py --version`..


.PHONY: changelog
