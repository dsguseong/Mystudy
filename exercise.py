from discord.ext import commands, tasks
from datetime import datetime, timedelta
# discord 라이브러리 사용 선언


import discord
# 반복 작업을 위한 패키지
from discord.ext import tasks
# 현재 시간을 받아와 구조체에 넣어주는 용도로 사용할 패키지
import datetime
# 중복 전송을 방지하기 위해 사용할 패키지
import time


class chatbot(discord.Client):
    # 1초에 한번 수행될 작업
    # 여기 함수는 에러가 나도 에러 메시지가 출력되지 않으므로 주의.
    @tasks.loop(hours=24)
    async def every_hour_notice(self):
        if datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
            await client.get_guild(800662275748266027).get_channel(800662275748266030).send("현재 {}시 {}분 입니다.아 맞다 로그아웃!".format(datetime.datetime.now().hour, datetime.datetime.now().minute))

            # 1초 sleep하여 중복 전송 방지
            time.sleep(1)

    # on_ready는 봇을 다시 구성할 때도 호출 됨 (한번만 호출되는 것이 아님.)
    async def on_ready(self):
        game = discord.Game("TEST")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")

        self.every_hour_notice.start()


if __name__ == "__main__":
    client = chatbot()
    client.run("ODAwNjU4ODAzNjM2NTY4MTEz.YAVVng.FOSiHbK9QEjrufIToVupdXsEp1I")
