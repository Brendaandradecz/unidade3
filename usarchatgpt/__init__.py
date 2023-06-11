import openai

def consultarchatgpt(produto):
   openai.api_key = 'depois coloco'
   model_engine = "text-davinci-003"
   prompt = 'me diga resumidamente o que você acha do ' + produto + ' ?'
   max_tokens = 1024
   completion = openai.Completion.create(
       engine=model_engine,
       prompt=prompt,
       max_tokens=max_tokens,
       temperature=0.5,
       top_p=1,
       frequency_penalty=0,
       presence_penalty=0
   )

   return completion.choices[0].text
