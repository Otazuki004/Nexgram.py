from Nexgram.types import *
import asyncio

modes = ['polling', 'webhook', 'none']

class Start:
  async def start(
    self,
    mode: str = 'polling',
    webhook_url: str = None,
    webhook_port: int = None,
  ):
    api, url = self.api, self.ApiUrl+"getMe"
    if mode.lower() not in modes:
      raise ValueError(f"Mode must be 'polling' or 'webhook' not '{mode}'")
    self.mode = mode.lower()
    r = await api.get(url)
    if r.get("ok"):
      self.connected = True
      r = r["result"]
      self.me = User(
        client=self,
        id=r['id'],
        first_name=r['first_name'],
        username=r['username'],
        is_self=True,
        is_bot=True,
      )
      log.info(f"Client connected as {self.me.first_name} (@{self.me.username})")
      if mode=='polling' and True:
        asyncio.create_task(self.start_polling())
        log.info("Exp. Feature Started: Loop created.")
      elif mode == "webhook":
        if not webhook_url or not webhook_port:
          raise ValueError("you selected 'webhook' mode. then where is url & port? you should provied it.")
        loop = asyncio.get_event_loop()
        loop.create_task(self.createWebhook())
      return self.me
    raise ValueError("Failed to connect with your bot token. Please make sure your bot token is correct.")