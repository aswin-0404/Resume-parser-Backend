AILOG.md – Resume Parser & AI Job Matching

 ##Project Overview

This project is a full-stack Resume Parser and Job Matching system built using Django (backend) and React + Tailwind CSS (frontend). It simulates a simplified Applicant Tracking System (ATS) where resumes are uploaded, parsed into structured data, and matched against job descriptions using a scoring algorithm.

 ##Role of AI in Development

AI was not just a tool but a co-pilot in the development process. It was used strategically at different stages:

System Design & Architecture  
AI guided the structuring of backend APIs, database schema, and frontend component hierarchy.

Debugging & Optimization  
Assisted in resolving Django REST issues, React state management bugs, and API integration challenges.

Parsing Logic & Matching Algorithm  
Helped design the hybrid parsing strategy and weighted scoring system.

Frontend Structuring  
Suggested reusable React components and Tailwind styling patterns.

 ##Tools & Technologies

Backend
Django + Django REST Framework

PostgreSQL

pdfplumber / python-docx (resume text extraction)


Frontend
React

Tailwind CSS

Axios

AI Tools
ChatGPT – for architecture, debugging, and algorithm design

Google Gemini API – for structured data extraction (later optional fallback)

 ##AI Prompts (Examples)

Resume Parsing Prompt
json
Extract structured data from this resume text.

Return ONLY valid JSON in this format:
{
  "name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "experience": 0,
  "education": "",
  "current_company": ""
}
Prompt Engineering Improvements
Enforced strict JSON-only output

Limited extraction to technical skills

Reduced unnecessary text to avoid parsing errors

 ##Challenges with AI Integration

Gemini API Model Errors

Model not found / version mismatch due to SDK changes

API Quota Limits

Frequent 429 RESOURCE_EXHAUSTED errors on free tier

Inconsistent JSON Output

AI responses included extra text or invalid JSON

Dependency Confusion

Migration from google.generativeai → google.genai caused compatibility issues

 ##Solutions Implemented

Hybrid Parsing Approach

Regex for email & phone

Keyword matching for skills

AI as fallback only

JSON Cleaning

Removed markdown wrappers


Skill Normalization

Lowercased & trimmed skills for consistency

Error Handling

Prevented crashes from API failures

 ##Matching Logic (AI-Assisted)

Skill Match % = (matched skills ÷ required skills) × 100

Experience Match = full score if candidate ≥ required experience, partial otherwise

Weighted Formula:

70% skills

30% experience

API returns:

Final score

Matched skills

Missing skills

Experience gap

 ##Frontend Features

Resume Upload Component – Upload PDF/DOCX → backend parsing → editable candidate form

Job Listing Component – Displays jobs with “Match Against Job” button

Match Result Component – Shows score, matched/missing skills, experience gap (color-coded results)

Candidate List Component – Displays all candidates with details

 ##Final Parsing Strategy

Rule-based parsing (primary)

AI parsing (optional fallback)

Ensures stability, consistent output, and independence from API limits