"""Api class used to post/get from BotApi, I don't like to create code for calling api each time."""
import aiohttp

class Api:
  async def post(self, url, json: dict = None, need_json=True):
    async with aiohttp.ClientSession() as mano:
      async with mano.post(url=url, json=json) as ily:
        if need_json:
          return await ily.json()
        else: return ily

  async def get(self, url, params=None, need_json=True):
    async with aiohttp.ClientSession() as mano:
      async with mano.get(url=url, params=params) as ily:
        if need_json:
          return await ily.json()
        else: return ily