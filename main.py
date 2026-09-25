from fastapi import FastAPI

app = FastAPI(
    title="Mini Blog",
)


@app.get("/")
def read_root():
    return {"message": "Bienevenido a Mini Blog!"}
