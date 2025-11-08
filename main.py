from fastapi import FastAPI
import uvicorn

app = FastAPI(title="demo app runner", description="this is a demo to run app runner", version="1.0.0")

@app.get("/")
def root():
    return { "message": "OK" }


def main():
    uvicorn.run(app, host="0.0.0.0", port=8080, proxy_headers=True)

if __name__ == "__main__":
    main()
