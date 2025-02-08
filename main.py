from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
import requests

# 注册插件
@register(name="RestartDockerLangbot", description="通过命令重启langbot的docker", version="0.1", author="魔术柿子")
class RestartDockerLangbotPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        msg = ctx.event.text_message  # 这里的 event 即为 PersonNormalMessageReceived 的对象
        if msg == ".重启":
            ctx.add_return("reply", ["开始重启, {}!".format(ctx.event.sender_id)])
            url = "http://172.17.0.1:8000/restartLangbot"
            requests.get(url)

            # 阻止该事件默认行为（向接口获取回复）
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
