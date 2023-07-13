import random
import string
import requests
import asyncio
async def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

async def send_new_items(items):
    url = "http://server:8000/new"
    response = requests.post(url, json=items)
    response.raise_for_status()

async def delete_items(count):
    url = f"http://server:8000/{count}"
    response = requests.get(url)
    response.raise_for_status()
    items = response.json()
    for item in items:
        delete_url = f"http://server:8000/{item['uuid']}"
        delete_response = requests.delete(delete_url)
        delete_response.raise_for_status()
    return len(items)


async def main():
    global cnt
    while True:
        items = []
        num_items = random.randint(10, 100)
        for _ in range(num_items):
            item = {"uuid": await generate_random_string(36), "text": await generate_random_string(16)}
            items.append(item)
        await send_new_items(items)
        cnt += await delete_items(1000)
        await asyncio.sleep(0)
async def print_cnt_periodically():
    while True:
        await asyncio.sleep(10)
        global cnt
        print(f"Количество удаленных записей = {cnt}")
        cnt = 0
if __name__ == "__main__":
    cnt = 0
    cnt_lock = asyncio.Lock()
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(print_cnt_periodically())
    loop.run_forever()