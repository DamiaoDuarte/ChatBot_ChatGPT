import openai

api_key = "your_key_here"
openai.api_key = api_key

def send_message(message, list_message=[]):
    list_message.append({"role": "user", "content": message})

    answer = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= list_message,
    )

    return answer["choises"][0]["message"]

list_message = []
while True:
    text = input("Write your message here: ")
    if text == "exit":
        break
    else:
        answer = send_message(text, list_message)
        list_message.append(answer)
        print("ChatBot: ", answer["content"])
