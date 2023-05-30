class BarkNotification(RequestContent):
    def __init__(self):
        super().__init__()
        self.token = token
        self.notification_url = "https://api.day.app/push"

    def post_msg(self, text) -> bool:
        data = {"title": "AutoBangumi 番剧更新", "body": text, "device_key": self.token}
        resp = self.post_data(self.notification_url, data)
        logger.debug(f"Bark notification: {resp.status_code}")
        return resp.status_code == 200