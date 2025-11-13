import httpx

JSONPLACEHOLDER = "https://jsonplaceholder.typicode.com/todos/1"

async def fetch_sample():
    async with httpx.AsyncClient() as client:
        r = await client.get(JSONPLACEHOLDER, timeout=10)
        r.raise_for_status()
        return r.json()
