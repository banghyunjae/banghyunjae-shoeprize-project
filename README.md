<img width="1920" alt="스크린샷 2023-08-01 오후 7 02 35" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/bcda0545-b9f9-417c-8cf0-5bee44b49ced">Shoeprize Project
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

* shoeprize 사전과제<br><br>
   
< 7월 28일 (금요일) ><br>
   - DRF APIView를 사용해서 RESTful한 API를 구현<br>
   - 관리자 코멘트는 blank, null = True 설정, 시리얼라이저에 미포함<br>
   - try, except를 활용 존재하지 않는 제조사, 제품의 UUID 가 있다면 404<br>
   - postman을 활용해 테스트

< 8월 1일 (화요일) > update<br>
   - 가격 정보를 담기 위해 currency 모델 추가<br>
   - APIView -> GenericView 변경<br>
   - postgreSQL DB 변경<br><br>

* Postman Create Test
<img width="1920" alt="스크린샷 2023-08-01 오후 6 54 26" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/42c4684b-80e0-4b74-a086-d3552ed2fe79">
<img width="1920" alt="스크린샷 2023-08-01 오후 6 55 08" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/ef5cc132-bb5b-4dda-983e-5e14f8af8604">
<img width="1920" alt="스크린샷 2023-08-01 오후 6 55 30" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/69b6895c-b3bd-4903-b1dd-3ed4cc6633f9">

* Postman List Test
<img width="1920" alt="스크린샷 2023-08-01 오후 6 57 06" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/f1ac8e53-be0f-4682-bf43-1ead1500476a">
<img width="1920" alt="스크린샷 2023-08-01 오후 6 57 21" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/c44490e7-5bb2-4cd8-9b38-87f279a3f831">
<img width="1920" alt="스크린샷 2023-08-01 오후 6 57 31" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/268d88b2-72aa-49c9-b6a1-0743e29c8287">

* Postman Update Test
<img width="1920" alt="스크린샷 2023-08-01 오후 6 58 21" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/71945798-c749-4e27-a945-6185a14d4334">
<img width="1920" alt="스크린샷 2023-08-01 오후 6 58 41" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/d829b557-bdec-4ad5-8caa-5fd82e923289">
<img width="1920" alt="스크린샷 2023-08-01 오후 7 00 58" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/612e4f37-6159-4a11-8084-b6ee07804941">

* sqlite3 -> postgreSQL 변경
<img width="1871" alt="스크린샷 2023-08-01 오후 7 03 03" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/62112ea4-839f-4294-9d85-2f736118ba89">
<img width="1871" alt="스크린샷 2023-08-01 오후 7 03 19" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/1380c613-42c4-46c6-99cf-b24c60006c42">
<img width="1871" alt="스크린샷 2023-08-01 오후 7 03 33" src="https://github.com/banghyunjae/banghyunjae_shoeprize-project/assets/127192957/78e5fd36-3066-41b9-b535-646a8f8804db">


