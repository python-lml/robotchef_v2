pip freeze
pytest tests --cov=robotchef_v2 --cov=robotchef_britishcuisine --cov=robotchef_api --doctest-glob=*.rst && flake8 . --exclude=.moban.d --builtins=unicode,xrange,long
