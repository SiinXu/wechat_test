import werobot
import openai

openai.api_key = "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"

robot = werobot.WeRoBot()

class RobotConfig(object):
    HOST="172.31.95.5"
    PORT= 80
    TOKEN = "151508" # token是微信公众号用来指定接入当前云服务器的服务的凭证，代表是自己人接入的，等一下就有什么用了

robot.config.from_object(RobotConfig)

def generate_response(prompt):
    response = openai.Completion.create(
    model="gpt-3.5-turbo-0301",
    prompt=prompt,
    temperature=0.7,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    message = response.choices[0].text
    return message.strip()



@robot.handler
def hello (messages):
    print(messages.content)
    return generate_response(messages.content)


if __name__ == "__main__":
    robot.run()
