#Sentence Embedding Playground🤾‍♀️


## Data Generator

NLI 수반관계의 유형

직접 수반 관계 (Material Implication):
P→Q

"오늘은 토요일이다" "내일은 일요일이다."

충분 조건 (Sufficient Condition):
P는 Q의 충분 조건이다.

"나는 성인이다" "나는 투표할 수 있다."

필요 조건 (Necessary Condition): 
P는 Q의 필요 조건이다.

"감스트는 대한민국 대통령이 될 수 있다" "감스트는 대한민국 국적아다."

상호 수반 관계 (Biconditional or Logical Equivalence):
P↔Q (두 명제가 서로 수반 관계인 경우)

"두 각도의 크기가 같다" "두 각도는 서로 동일하다."

물리학적 수반 관계:
P와 Q 사이에 물리적인 연결이 있다.

"비가 내렸다" "지면이 젖었다."

### 해볼만한 시도들

수반관계는 모델에 지식이 있다는 전제가 필요. 

premise/hypothesis 데이터셋과 함께 context/premise/hypothesis 데이터셋도 만들자. 
- 이 방법이 premise/hypothesis의 관계성 분석 자체는 잘하겠지만, 지식 그 자체는 원본 모델에 비해 degrade될지도 모르겠다.
- QA task로 학습된 모델이 범용성이 있는지 확인해보자.

Entailment: 수반? 함의? 용어 선정 유의하기
Contradiction: 모순.

전제(Premise)와 가설(Hypothesis)의 관계는 역이 성립하는가?
NLI dataset을 생성할 때 few-shot prompt를 어떻게 구성해야 할지에 대한 논의 살펴보기.


## 괜찮은 raw data sourse

- 카카오 브런치: 다양한 주제, 정리된 글. 크롤링 도구: https://velog.io/@denhur62/%EB%B8%8C%EB%9F%B0%EC%B9%98-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0
- 디씨위키: 인터넷의 sentimental한 정보를 잘 반영한다는 측면에서 kcbert 데이터셋도 좋지만, 글의 포맷이 위키라는 장점이 있겠다. 페미위키 <- 이 사이트 정보량 많나? no) 그쪽세계의 유머감각 정보는 딱히 없는듯..
