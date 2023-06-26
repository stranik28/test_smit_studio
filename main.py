from fastapi import FastAPI
from src.insurance.router import router as insurance_router
from tortoise.contrib.fastapi import register_tortoise
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": DB_NAME,
                "host": DB_HOST,
                "password": DB_PASS,
                "port": DB_PORT,
                "user": DB_USER
            }
        }
    },
    "apps": {
        "models": {
            "models": ["src.insurance.model"],
            "default_connection": "default"
        }
    }
}



app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # Генерировать схемы базы данных при запуске
    add_exception_handlers=True,
)

app.include_router(insurance_router)