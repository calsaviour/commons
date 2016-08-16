python_library(
  name = "app-lib",
  sources = globs('*.py'),
  dependencies = [
    "src/python/twitter/common/app",
    "src/python/twitter/3rdparty/python:tornado",
    "src/python/twitter/3rdparty/python:psutil",
  ]
)

python_binary(name="hello_world",
  source="hello_world.py",
  dependencies=[':app-lib']
)
