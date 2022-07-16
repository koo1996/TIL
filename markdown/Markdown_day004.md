로컬 TIL 저장소

push , 

pull

clone 

$ git clone <주소>

(클론 주의) 원격저장소이름의 폴더가 생성

압축파일과 clone 차이 (master유무)

압축 : 최신버전의 파일/폴더

clone : git 저장소 (분산버전)

'$ git push origin master'

 ' '



Branch 목적 독립적인 버전들을 만들어나갈수 있다.

Branch merge : 작업을 한 이후 이력을 합치기 위해 merge사용

$ git branch  브랜치조회

$ git branch example 브랜치생성

$ git checkout example (master)-(example) 브랜치변경

$ git checkout -b (branch name) 브랜치 생성 하면서 이동

$ git merge example (master일때 merge)

$ git branch -d example 브랜치 삭제

feature branch workflow

shared repositoty model (저장소의 소유권이 있는 경우)



Forking workflow

Fork & Pull Request (저장소의 소유권이 없는 경우)