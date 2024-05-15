def main(model):
    prompt = input()
    response = model.generate_content(prompt)
    assistant_response = response.text
    print(f"Assistant: {assistant_response}")