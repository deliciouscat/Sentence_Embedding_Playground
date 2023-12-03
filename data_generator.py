from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain.prompts import PromptTemplate

data = load_dataset("csv", data_files="sample.csv")

#model_id = "DopeorNope/COKAL-DPO_test-v2-13b"        # ko-HellaSwag 1위: 23.12.03 , 비공개
model_id = "DopeorNope/mistralopithecus-v1-dpo-7b"    # ko-HellaSwag 2위: 23.12.03
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    trust_remote_code=True, 
)

template = """ 예시를 참고하여, 주어진 전제 문장에 대해 수반 관계에 있는 가설 문장과 모순 관계의 문장 2개를 만들어줘. 

예시)

전제: 
수반: 
모순: 

전제: 
수반: 
모순: 

전제: 
수반: 
모순: 

주어진 문장)

전제: 

"""

prompt = PromptTemplate(template=template, input_variables=['context'])


data = data.map(format_text)