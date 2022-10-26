# 22.10.26

* Asynchronous JavaScript
    * 비동기식
        * 병렬적 Task 수행
        * 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐(non-blockinig)
        * 요청을 보내고 응답을 기다리지 않고 다음 코드가 실행됨
        * 결과적으로 변수 todo에는 응답 데이터가 할당되지 않고 빈 문자열이 출력 

* Event Loop 기반 동시성 모델
    * Call Stack
        * 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료 구조
    * Web API(Browser API)
        * JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
        * setTimeout(), DOM events, AJAX
    * Task Queue (Event Queue, Message Queue)
        * 비동기 처리된 callback 함수가 대기하는 Queue(FIFO)형태의 자료 구조
        * main thread가 끝난 후 실행되어 후속 JavaScript 코드가 차단되는 것을 방지
    * Event Loop
        * Call Stack이 비어 있는지 확인
        * 비어  있는 경우 Task Queue에서 실행 대기 중인 callback 함수가 있는지 확인
* AJAX란?
    * Asynchronous JavaScript And XML(비동기식 JavaScript와 XML)
    * 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
    * 이러한 '비동기 통신 웹 개발 기술'을 AJAX라 함
    * 비동기 웹 통신을 위한 라이브러리 중 하나가 Axios
* AJAX 특징
    * 페이지 전체를 reload(새로고침)을 하지 않고서도 수행되는 "비동기성"
    * 서버의 응답에 따라 전체 페이지가 아닌 일부분만을 업데이트 할 수 있음
    1. 페이지 새로고침 없이 서버에 요청
    2. 서버로부터 응답(데이터)을 받아 작업을 수행

* Axios

* 비동기 처리 필요성
* 비동기 처리 원리와 과정
