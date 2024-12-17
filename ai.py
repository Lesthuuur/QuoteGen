import openai
openai.api_key = "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"

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"Generate a quote about feeeling sick"}]
)

print(response)