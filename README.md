Shoeprize Project
=================
* 모델
    * 제조사(제품 생산업체)
        * 제조사명
        * 제조사 영문명
    * 제품
        * 제품명 : 예)에어 맥스 99
        * 제품명 영문 : 예)AIR MAX 99
        * 제품코드: 10자 내외의 문자열 (예 : ABCD-012)
        * 제조사
        * 출시일시
        * 가격 : 달러, 유로, 원, 엔 등의 정보 저장 필요
        * 관리자 코멘트 : 한글 및 유니코드 100자 내외의 문자열
----------------------------------------------------
* API
    * 제조사 등록 API
    * 제조사 조회 API GET /{제조사 모델명}/{UUID}
        * 존재하지 않는 UUID 처리 필수
    * 제품 등록 API
    * 제품 조회 API GET /{제품 모델명}/{UUID}
        * 제품정보와, 제조사 정보를 모두 포함합니다.
        * 관리자 코멘트는 노출하지 않습니다.
        * 출시 일시는 조회하는 국가에 따라 클라이언트에서 표시할 예정입니다.
        * 존재하지 않는 UUID 처리 필수
------------------------------------------------------------
* 참고
    * 모델의 필드 추가 제한 없음
        * API는 RESTfull 규칙을 준수합니다.
------------------------------------------------------------

* shoeprize 사전과제<br>
   - < 7월 28일 (금요일) ><br>
      - DRF APIView를 사용해서 RESTful한 API를 구현<br>
      - 관리자 코멘트는 blank, null = True 설정, 시리얼라이저에 미포함<br>
      - try, except를 활용 존재하지 않는 제조사, 제품의 UUID 가 있다면 404<br>
      - postman을 활용해 테스트

< 8월 1일 (화요일) > update<br>
   - 가격 정보를 담기 위해 currency 모델 추가<br>
   - APIView -> GenericView 변경<br>
   - postgreSQL DB 변경<br>
<img width="1076" alt="스크린샷 2023-08-01 오후 6 41 44" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/b10ea1ea-35d0-4c63-96c3-4c1c528a9e55">
<img width="1060" alt="스크린샷 2023-08-01 오후 6 41 59" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/6cdbebc8-6d96-4d61-94c7-3f049be2edd6">
<img width="1071" alt="스크린샷 2023-08-01 오후 6 42 19" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/efd0f71a-1295-40eb-bf2d-74fd126c0db4">

<img width="1425" alt="스크린샷 2023-08-01 오후 6 47 07" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/36bc171f-97a9-44af-8001-2a7a819abc5a">
<img width="950" alt="스크린샷 2023-08-01 오후 6 45 29" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/aeea98e7-357f-4c2e-9cce-34cbcc99af5a">
<img width="1337" alt="스크린샷 2023-08-01 오후 6 44 37" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/8307d0d6-aded-4c40-8b7f-5d7bf372f26e">


