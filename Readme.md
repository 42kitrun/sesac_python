# sesac_python

![Nginx](https://img.shields.io/badge/-Nginx-009639?logo=nginx&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white)
![Node.js](https://img.shields.io/badge/-Node.js-339933?logo=node.js&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-ffffff?logo=langchain&logoColor=green)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white)
![React](https://img.shields.io/badge/-React-61DAFB?logo=react&logoColor=black)

## 📝 프로젝트 소개

새싹(SeSAC) Python 풀스택 개발자 과정에서 학습한 내용을 체계적으로 정리한 저장소입니다. HTML/CSS/JavaScript 기초부터 Python 백엔드 개발, 데이터베이스, API 연동, React까지 풀스택 개발의 전 과정을 다룹니다. 실무 중심의 미니 프로젝트와 실습 예제를 통해 확장 가능하고 유지보수 가능한 웹 애플리케이션 개발 방법을 학습합니다.

## ✨ 주요 학습 내용

- 🌐 프론트엔드 기초 (HTML, CSS, JavaScript)
- ⚛️ React 기반 SPA 개발
- 🐍 Python 백엔드 개발
- 🗄️ 데이터베이스 설계 및 ORM
- 🔌 RESTful API 설계 및 구현
- 🧪 테스트 주도 개발 (TDD)

## 🛠️ 기술 스택

### Frontend
- HTML5, CSS3, JavaScript (ES6+)
- React 19.1.1
- Bootstrap
- Chart.js

### Backend
- Python 3.x
- Flask
- SQLAlchemy (ORM)

### Database
- SQLite
- MySQL
- PostgreSQL

### API & Libraries
- OpenAI API (LangChain)
- Naver API
- Kakao API
- BeautifulSoup (웹 크롤링)

## 📦 주요 의존성

```json
{
  "@testing-library/react": "^16.3.0",
  "react": "^19.1.1",
  "react-dom": "^19.1.1",
  "react-scripts": "5.0.1"
}
```

## 🚀 실행 명령어

- **개발 서버 시작**: `npm start`
- **프로덕션 빌드**: `npm run build`
- **테스트 실행**: `npm test`

## 📁 프로젝트 구조

```
.
├── 1.HTML/                 # HTML 기초 및 시맨틱 마크업
├── 2.CSS/                  # CSS 스타일링 및 레이아웃
├── 3.JS/                   # JavaScript DOM 조작 및 이벤트 처리
├── 4.Python/               # Python 기초 문법 및 고급 개념
├── 5.Project/              # 실무 미니 프로젝트 (CRM, 이미지 검색 등)
├── 6.Flask/                # Flask 웹 프레임워크
├── 7.API/                  # 외부 API 연동 (Naver, Kakao, OpenAI)
├── 8.Node/                 # Node.js 및 React 프로젝트
└── database/               # 데이터베이스 스키마 및 예제 데이터
```

## 🛠️ 개발 환경 설정

### Python 환경
```bash
# Python 3.8 이상 필요
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Node.js 환경
```bash
# Node.js v18 이상 권장
npm install
npm start
```

## 💡 주요 프로젝트

### 1. 데이터 생성기 (`5.Project/1.data_gen`)
사용자, 상점, 주문 데이터를 자동 생성하는 시뮬레이션 도구

### 2. 이미지 검색 앱 (`5.Project/2.pixabay`)
Pixabay API를 활용한 이미지 검색 및 관리 시스템

### 3. Mini CRM (`5.Project/3-4.minicrm`)
고객 및 상점 관리를 위한 경량 CRM 시스템

### 4. 종합 CRM (`5.Project/5.crm`)
사용자, 상점, 주문, 상품을 통합 관리하는 풀스택 CRM 애플리케이션

### 5. RAG 챗봇 (`7.API/3.openai/24.rag_chatbot`)
문서 기반 질의응답이 가능한 AI 챗봇 (LangChain + OpenAI)

## 👥 기여하기

기여는 언제나 환영합니다!

1. 저장소를 **Fork**하세요
2. 새 브랜치를 생성하세요: `git checkout -b feature/your-feature`
3. 변경사항을 커밋하세요: `git commit -am 'Add feature'`
4. 브랜치에 Push하세요: `git push origin feature/your-feature`
5. **Pull Request**를 열어주세요

코드는 프로젝트의 스타일 가이드를 따르며, 필요한 경우 테스트 코드를 포함해주세요.

---
*SeSAC Python 풀스택 개발자 과정 학습 자료*