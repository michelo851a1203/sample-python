import sys
from fastapi import FastAPI
from contextlib import asynccontextmanager
# import uvicorn

@asynccontextmanager
async def life_span(_: FastAPI):
    print("Application start up ...", file=sys.stderr)
    yield

app = FastAPI(title="demo app runner", description="this is a demo to run app runner", version="1.0.0", life_span=life_span)

@app.get("/")
def root():
    return { "message": "OK" }

# def main():
#     uvicorn.run(app, host="0.0.0.0", port=8080, proxy_headers=True)
#
# if __name__ == "__main__":
#     main()
