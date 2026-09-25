from fastapi import FastAPI

app = FastAPI(
    title="Mini Blog",
)


BLOG_POSTS = [
    {
        "id": 1,
        "title": "Primer Post",
        "content": "Este es el contenido del primer post.",
        "author": "Juan Pérez",
    },
    {
        "id": 2,
        "title": "Segundo Post",
        "content": "Este es el contenido del segundo post.",
        "author": "María López",
    },
    {
        "id": 3,
        "title": "Tercer Post",
        "content": "Este es el contenido del tercer post.",
        "author": "Carlos García",
    },
]


@app.get("/")
def read_root():
    return {"message": "Bienevenido a Mini Blog!"}


@app.get("/posts")
def list_posts():
    return {"data": BLOG_POSTS}
