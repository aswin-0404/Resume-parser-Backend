# Resume Parser & Job Matching – Backend

## Overview  
This backend is built using Django and Django REST Framework to power a Resume Parser and Job Matching system.  
It processes resume uploads, extracts structured data, stores candidate information, manages job listings, and computes fitment scores between candidates and jobs.

The system simulates a simplified Applicant Tracking System (ATS) workflow.

---

## Tech Stack & Usage  

### Django & Django REST Framework  
Used to build RESTful APIs and handle core backend logic such as resume parsing, candidate management, and job matching.

### PostgreSQL  
Used as the relational database to store candidate and job data.

### File Storage (Cloudinary / Local Storage)  
Used to store uploaded resumes securely.

### pdfplumber / python-docx  
Used to extract text from PDF and DOCX files.

### Regex & Rule-Based Parsing  
Used to extract structured information such as email, phone number, skills, and experience.

---

## Core Features  

### Resume Upload  
- Upload resumes in PDF/DOCX format  
- File stored on server/cloud storage  
- Candidate record created on upload  

### Resume Parsing  
Extracts:
- Name  
- Email  
- Phone  
- Skills (array)  
- Experience (years)  
- Education  
- Current/Last Company  

Uses:
- Text extraction (pdfplumber/docx)  
- Regex + keyword-based parsing    

---

### Candidate Management  
- Store parsed candidate data  
- Retrieve all candidates  
- View candidate details  

---

### Job Management  
- Seed 3–5 jobs into database  
- Fields:
  - Title  
  - Code  
  - Skills  
  - Experience  
  - Location  
  - Description  

---

#### Experience Check
- Full score if candidate ≥ required experience  
- Partial score if candidate < required  

#### Final Score
- 70% → Skills  
- 30% → Experience  

#### API Response Includes:
- Final score (%)  
- Matched skills  
- Missing skills  
- Experience gap  

---

## API Endpoints  

### Resume APIs  
- `POST /api/upload-resume/` → Upload resume  
- `POST /api/parse-resume/<id>/` → Parse resume  

### Candidate APIs  
- `GET /api/all-candidates/` → List candidates  

### Job APIs  
- `GET /api/list-jobs/` → List jobs  

### Matching API  
- `POST /api/match-job/` → Match candidate with job  

---

## How to Run the Project  

Clone the repository: https://github.com/aswin-0404/Resume-parser-Backend.git

Open the project in Vs Code

Configure the database: Update the connection string in settings if required

Apply migrations to create the database

Run the application

The system evaluates how well a candidate matches a job:

#### Skill Match
