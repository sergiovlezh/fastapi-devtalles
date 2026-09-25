from fastapi import FastAPI, Query

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
def list_posts(
    query: str | None = Query(
        default=None,
        description="Filtra los posts por título o contenido.",
    ),
):

    results = BLOG_POSTS

    if query:
        results = [
            post
            for post in BLOG_POSTS
            if query.lower() in post["title"].lower()
            or query.lower() in post["content"].lower()
        ]

    return {"data": results, "query": query}
