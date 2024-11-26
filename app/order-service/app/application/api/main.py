from fastapi import FastAPI


def create_app():
    app = FastAPI(
        title = 'e-commerce',
        docs_url = '/api/docs',
        description = 'e-commerce-platform',
        debug = True,
    )

    return app
