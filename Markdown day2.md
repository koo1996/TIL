# Git 



## 1. Git 이란?

* Git은 **분산버전관리시스템**으로 코드의 버전을 관리하는 도구
* 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율



## 2. 기본 흐름

* Git은 파일을 modifided, staged, committed로 관리

  * modified 는 파일이 수정된 상태

  * staged 는 수정한 파일을 곧 커밋할 것이라고 표시한 상태

  * committed 는  커밋이 된 상태



## 3. $git log

* 현재 저장소에 기록된 커밋을 조회
* 다양한 옵션을 통해 로그를 조회할 수 있음
* $ git log -1 , $ git log --oneline , $ git log -2 --oneline



## 4. $git status

* Git 저장소에 있는 파일의 상태를 확인하기 위하여 활용
  * 파일의 상태를 알 수 있음
* Status로 확인할 수 있는 파일의 상태
  * Tracked : 이전부터 버전으로 관리되고 있는 파일
  * Untracked : 버전으로 관리된 적 없는 파일



## 5. Git 기초 명령어

| 명령어                       | 내용                           |
| ---------------------------- | ------------------------------ |
| git init                     | 로컬 저장소 생성               |
| git add <파일명>             | 특정 파일/폴더의 변경사항 추가 |
| git commit -m '<커밋메시지>' | 커밋(버전 기록)                |
| git status                   | 상태 확인                      |
| git log                      | 버전 확인                      |

* 사용자 정보 (commit author) : 커밋을 하기 위해 반드시 필요
  * git config --global user.name "username"
  * git config --global user.email "이메일 주소"



# 원격저장소 활용하기 GITHUB



## 1. 원격저장소 기본흐름

* 로컬 저장소의 버전(커밋)을 원격저장소로 보낸다.
  * $ git push
* 원격저장소의 버전(커밋)을 로컬 저장소로 가져온다.
  * $ git pull



## 2. GitHub에서 원격 저장소 만들기

* New Repository - 저장소 설정하기 - 확인하기
* 원격 저장소 정보를 로컬 저장소에 추가( 한번만 설정 해주면 된다)
  * $ git remote add origin https://github.com/username/저장소이름
* 원격 저장소의 정보를 확인
  * $ git remote -v
* 원격 저장소로 로컬 저장소 변경 사항(커밋)을 올림(push)
  * $ git push <원격저장소이름><브랜치이름>



## 3. .gitignore 

* 일반적인 개발 프로젝트에서 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생한다. 
* Git 저장소에 .gitignore 파일을 생성하고 해당 내용을 관리한다.



## 4. 참고문헌

* [참고문헌1](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e293555d-5e00-4cf8-9e3f-0db458c254e1/GitHub_기초.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220706T042325Z&X-Amz-Expires=86400&X-Amz-Signature=b8d88647b5213313e4b341d2986e2859b21a6c7ffb93ab188c82cfc792f0840e&X-Amz-SignedHeaders=host&response-content-disposition=filename %3D"GitHub_%EA%B8%B0%EC%B4%88.pdf"&x-id=GetObject)





