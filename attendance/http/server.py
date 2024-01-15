from typing import Any, Callable

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

"""middleware"""


class Middleware:
    def __init__(self, middleware_class: type, **options: Any):
        self.middleware_class = middleware_class
        self.options = options

    def __repr__(self):
        return f"Middleware({self.middleware_class.__name__}, options={self.options})"

    def register(self, app: FastAPI):
        app.add_middleware(self.middleware_class, **self.options)  # type: ignore


def cors():
    return Middleware(
        middleware_class=CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def proxy_headers():
    return Middleware(middleware_class=ProxyHeadersMiddleware)


"""router"""


class Router:
    def __init__(
        self, path: str, methods: list[str], endpoint: Callable, dependencies=[]
    ):
        self._path = path
        self._methods = methods
        self._endpoint = endpoint
        self._dependencies = dependencies

    def __repr__(self):
        return f"Router(path={self._path}, methods={self._methods}, endpoint={self._endpoint.__name__})"

    def register(self, app: FastAPI):
        router = APIRouter()

        router.add_api_route(
            path=self._path,
            methods=self._methods,
            endpoint=self._endpoint,
            dependencies=self._dependencies,
        )

        app.include_router(router)


"""server"""


class Server:
    def __init__(self, name: str):
        self._name = name
        self._app = FastAPI()

        self._middlewares = []
        self._routers = []

    def middleware(self, middleware: Middleware):
        self._middlewares.append(middleware)

    def router(self, router: Router):
        self._routers.append(router)

    def print(self):
        print("=========={}==========".format(self._name))

        for middleware in self._middlewares:
            print(" -{}".format(middleware))

        for router in self._routers:
            print(" -{}".format(router))

    def app(self):
        for middleware in self._middlewares:
            middleware.register(self._app)

        for router in self._routers:
            router.register(self._app)

        return self._app
