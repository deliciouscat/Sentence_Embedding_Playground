import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
#from langchain.prompts import PromptTemplate

data = pd.read_csv("example.csv")

#model_id = "DopeorNope/COKAL-DPO_test-v2-13b"        # ko-HellaSwag 1위: 23.12.03 , 비공개
model_id = "DopeorNope/mistralopithecus-v1-dpo-7b"    # ko-HellaSwag 2위: 23.12.03
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
)

template = """ 예시를 참고하여, 주어진 전제 문장에 대해 수반 관계에 있는 가설 문장과 모순 관계의 문장 2개를 만들어줘. 내용이 창의적이고 다양한 어휘를 사용하면 좋아.

예시)

전제: 심해에서 자란 나무는 잎이 보라색입니다.
수반: 바다 깊은곳에 있는 숲의 풍경은 보랏빛이다.
모순: 나무는 어디에서 키우든 초록색 잎을 가져!

전제: 감스트는 대한민국 대통령이 될 수 있어.
수반: 감스트는 대한민국 국적이다.
모순: 감스트, 그는 국민들의 지지를 받고 있지 않아.

전제: 비가 내렸다.
수반: 지면이 젖었다.
모순: 산불이 번졌어요.

주어진 문장)

전제: 알베르토는 지금 르완다에 있다.

"""

#prompt = PromptTemplate(template=template, input_variables=['context'])


for t in data:
    print(t)
    inputs = tokenizer(template + t, return_tensors='pt').to('cuda')
    generated_ids = model.generate(**inputs)
    outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    print(outputs)
