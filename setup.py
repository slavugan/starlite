# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlite',
 'starlite.handlers',
 'starlite.openapi',
 'starlite.plugins',
 'starlite.template',
 'starlite.utils']

package_data = \
{'': ['*'], 'starlite': ['starlite.egg-info/*']}

install_requires = \
['openapi-schema-pydantic',
 'orjson',
 'pydantic',
 'pydantic-factories',
 'python-multipart',
 'pyyaml',
 'requests',
 'starlette',
 'typing-extensions']

setup_kwargs = {
    'name': 'starlite',
    'version': '1.0.0',
    'description': 'Light-weight and flexible ASGI API Framework',
    'long_description': '<img alt="Starlite logo" src="static/starlite-hero.svg" width=100%, height="auto">\n\n<div align="center">\n\n![PyPI - License](https://img.shields.io/pypi/l/starlite?color=blue)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/starlite)\n\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)\n[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)\n[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)\n[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_starlite&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_starlite)\n\n[![Discord](https://img.shields.io/discord/919193495116337154?color=blue&label=chat%20on%20discord&logo=discord)](https://discord.gg/X3FJqy8d2j)\n\n</div>\n\n# Starlite\n\nStarlite is a light and flexible ASGI API framework. Using [Starlette](https://github.com/encode/starlette)\nand [pydantic](https://github.com/samuelcolvin/pydantic) as foundations.\n\nCheck out the [Starlite documentation 📚](https://starlite-api.github.io/starlite/)\n\n## Core Features\n\n- 👉 Class based controllers\n- 👉 Decorators based configuration\n- 👉 Extended testing support\n- 👉 Extensive typing support including inference, validation and parsing\n- 👉 Full async (ASGI) support\n- 👉 Layered dependency injection\n- 👉 OpenAPI 3.1 schema generation with [Redoc](https://github.com/Redocly/redoc) UI\n- 👉 Route guards based authorization\n- 👉 Simple middleware and authentication\n- 👉 Support for pydantic models and pydantic dataclasses\n- 👉 Support for standard library dataclasses\n- 👉 Support for SQLAlchemy declarative classes\n- 👉 Plugin system to allow extending supported classes\n- 👉 Ultra-fast json serialization and deserialization using [orjson](https://github.com/ijl/orjson)\n\n## Installation\n\n```shell\npip install starlite\n```\n\n## Relation to Starlette and FastAPI\n\nAlthough Starlite uses the Starlette ASGI toolkit, it does not simply extend Starlette, as FastAPI does. Starlite uses\nselective pieces of Starlette while implementing its own routing and parsing logic, the primary reason for this is to\nenforce a set of best practices and discourage misuse. This is done to promote simplicity and scalability - Starlite is\nsimple to use, easy to learn, and unlike both Starlette and FastAPI - it keeps complexity low when scaling.\n\nAdditionally, Starlite is [faster than both FastAPI and Starlette](https://github.com/Goldziher/api-performance-tests):\n\n![plain text requests processed](static/result-plaintext.png)\n\nLegend:\n\n- a-: async, s-: sync\n- np: no params, pp: path param, qp: query param, mp: mixed params\n\n### Class Based Controllers\n\nWhile supporting function based route handlers, Starlite also supports and promotes python OOP using class based\ncontrollers:\n\n```python title="my_app/controllers/user.py"\nfrom typing import List, Optional\n\nfrom pydantic import UUID4\nfrom starlite import Controller, Partial, get, post, put, patch, delete\nfrom datetime import datetime\n\nfrom my_app.models import User\n\n\nclass UserController(Controller):\n    path = "/users"\n\n    @post()\n    async def create_user(self, data: User) -> User:\n        ...\n\n    @get()\n    async def list_users(self) -> List[User]:\n        ...\n\n    @get(path="/{date:int}")\n    async def list_new_users(self, date: datetime) -> List[User]:\n        ...\n\n    @patch(path="/{user_id:uuid}")\n    async def partially_update_user(self, user_id: UUID4, data: Partial[User]) -> User:\n        ...\n\n    @put(path="/{user_id:uuid}")\n    async def update_user(self, user_id: UUID4, data: User) -> User:\n        ...\n\n    @get(path="/{user_name:str}")\n    async def get_user_by_name(self, user_name: str) -> Optional[User]:\n        ...\n\n    @get(path="/{user_id:uuid}")\n    async def get_user(self, user_id: UUID4) -> User:\n        ...\n\n    @delete(path="/{user_id:uuid}")\n    async def delete_user(self, user_id: UUID4) -> User:\n        ...\n```\n\n### Data Parsing, Type Hints and Pydantic\n\nOne key difference between Starlite and Starlette/FastAPI is in parsing of form data and query parameters- Starlite\nsupports mixed form data and has faster and better query parameter parsing.\n\nStarlite is rigorously typed, and it enforces typing. For example, if you forget to type a return value for a route\nhandler, an exception will be raised. The reason for this is that Starlite uses typing data to generate OpenAPI specs,\nas well as to validate and parse data. Thus typing is absolutely essential to the framework.\n\nFurthermore, Starlite allows extending its support using plugins.\n\n### SQL Alchemy Support, Plugin System and DTOs\n\nStarlite has a plugin system that allows the user to extend serialization/deserialization, OpenAPI generation and other\nfeatures. It ships with a builtin plugin for SQL Alchemy, which allows the user to use SQL Alchemy declarative classes\n"natively", i.e. as type parameters that will be serialized/deserialized and to return them as values from route\nhandlers.\n\nStarlite also supports the programmatic creation of DTOs with a `DTOFactory` class, which also supports the use of plugins.\n\n### OpenAPI\n\nStarlite has custom logic to generate OpenAPI 3.1.0 schema, the latest version. The schema generated by Starlite is\nsignificantly more complete and more correct than those generated by FastAPI, and they include optional generation of\nexamples using the `pydantic-factories` library.\n\n### Dependency Injection\n\nStarlite has a simple but powerful DI system inspired by pytest. You can define named dependencies - sync or async - at\ndifferent levels of the application, and then selective use or overwrite them.\n\n### Middleware\n\nStarlite supports the Starlette Middleware system while simplifying it and offering builtin configuration of CORS and\nsome other middlewares.\n\n### Route Guards\n\nStarlite has an authorization mechanism called `guards`, which allows the user to define guard functions at different\nlevel of the application (app, router, controller etc.) and validate the request before hitting the route handler\nfunction.\n\n### Request Life Cycle Hooks\n\nStarlite supports request life cycle hooks, similarly to Flask - i.e. `before_request` and `after_request`\n\n## Contributing\n\nStarlite is open to contributions big and small. You can always [join our discord](https://discord.gg/X3FJqy8d2j) server\nto discuss contributions and project maintenance. For guidelines on how to contribute, please\nsee [the contribution guide](CONTRIBUTING.md).\n',
    'author': "Na'aman Hirschfeld",
    'author_email': 'nhirschfeld@gmail.com',
    'maintainer': "Na'aman Hirschfeld",
    'maintainer_email': 'nhirschfeld@gmail.com',
    'url': 'https://github.com/starlite-api/starlite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
