import asyncio
import aiohttp
import json


async def request_data(url):
    async with aiohttp.request('GET', url) as resp:
        return await resp.text()


async def get_reddit_top(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    data = await request_data(url)
    json_data = json.loads(data)
    print(f'json parsed\n{json_data}')


async def main():
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    await asyncio.gather(*(get_reddit_top(reddit) for reddit in reddits))


asyncio.run(main())
