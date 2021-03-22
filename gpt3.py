import openai

from fastapi.encoders import jsonable_encoder


class GPT3:
    def query(self, primer, temperature=0.9, stop=None, max_tokens=500, stream=True):
        primer = primer.strip(' ')
        try:
            response = openai.Completion.create(
                engine="davinci", # one of [ada, babbage, curie, davinci]
                prompt=primer,
                max_tokens=max_tokens,
                stop=stop,
                temperature=temperature,
                top_p=1,
                n=1,
                stream=stream,
                logprobs=None,
                frequency_penalty=0.5,
            )
            if stream:
                return self.streamWrapper(response)
            else:
                return response
        except Exception as error:
            return self.errorStream(error._message)


    def streamWrapper(self, response):
        for i in response:
            # print(i)
            yield dict(data=i["choices"][0])

    def errorStream(self, error):
        for i in range(1):
            yield {"data": {"error": error}}
