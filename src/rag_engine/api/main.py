from fastapi import FastAPI


app = FastAPI(
    title="AI RAG Engine"
)


@app.get("/")
def home():

    return {
        "message":
        "AI RAG Engine Running"
    }
