from fastapi import FastAPI

app = FastAPI()

@app.get("\users")
async def list_users():

    pass


@app.get("\users\ {id}")
async def create_user(id: int):

    pass


@app.post("\users")
async def create_user():

    pass


@app.delete("\users\ {id}")
async def list_users(id: int):

    pass


@app.put("\users\ {id}")
async def update_users(id: int):

    pass