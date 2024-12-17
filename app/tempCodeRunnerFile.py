
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Generate a quote about feeling {emotion}"}],
            )
            quote_result = response['choices'][0]['message']['content']