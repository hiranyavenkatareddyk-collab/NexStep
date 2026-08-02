# NexStep# NexStep

## Overview

NexStep is an AI-powered Exam Eligibility and Tracking Platform designed to help students discover examinations they are eligible for, monitor official notifications, and receive personalized updates.

Instead of requiring students to manually visit multiple official websites and interpret complex eligibility criteria, NexStep automates the process by collecting official notifications, extracting relevant information, verifying changes through an approval workflow, and evaluating each student's eligibility based on their academic profile.

The project combines automation, artificial intelligence, and rule-based decision making to provide accurate and personalized exam recommendations.



## Problem Statement

Students often miss valuable career opportunities because:

- Exam information is scattered across multiple official websites.
- Eligibility criteria are difficult to interpret.
- Official notifications are lengthy and frequently updated.
- Students are unaware of newly announced examinations.
- Important deadlines are missed.
- There is no centralized platform that tells students exactly which exams they are eligible for.

NexStep addresses these challenges by providing a unified platform that continuously tracks official notifications and evaluates eligibility automatically.


## Objectives

- Centralize examination information from official sources.
- Determine student eligibility automatically.
- Track changes in official notifications.
- Notify students about relevant updates and deadlines.
- Reduce manual effort required to search and verify exam information.
- Provide an intelligent assistant for exam-related queries.


## Key Features

### Student

- Account Registration and Authentication
- Profile Management
- Educational Profile Management
- Personalized Eligible Exams
- Non-Eligible Exams with Reasons
- Exam Tracking
- Deadline Reminders
- In-App Notifications
- Email Notifications
- AI Chat Assistant

### Administration

- Review AI-extracted information
- Approve or reject notification updates
- Manage examinations
- Monitor system activity through audit logs

### Automation

- Periodically monitors official examination websites
- Detects newly published notifications
- Downloads official notification documents
- Identifies changes between notification versions

### Artificial Intelligence

- Extracts structured information from official notifications
- Generates concise summaries
- Highlights differences between notification versions
- Assists administrators during verification





## Architecture

The project follows a modular architecture consisting of:

- Frontend
- Backend API
- PostgreSQL Database
- Automation Service
- AI Verification Engine
- Eligibility Engine
- Notification Service

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Frontend

- React
- HTML
- CSS
- JavaScript

### Artificial Intelligence

- Large Language Models
- Prompt Engineering

### Automation

- Selenium
- BeautifulSoup

### Authentication

- JWT Authentication
- Password Hashing

### Development Tools

- Git
- GitHub
- VS Code

## Development Roadmap

- System Analysis
- Database Design
- Backend Development
- Frontend Development
- AI Integration
- Automation Module
- Eligibility Engine
- Notification System
- Testing
- Deployment



## Current Status

Project Phase: Architecture and Planning

Completed

- Problem Analysis
- Requirement Analysis
- System Architecture
- Database Design
- ER Diagram
- Workflow Design

Upcoming

- Backend Development
- Frontend Development
- AI Integration
- Automation Development
- Deployment

## Future Enhancements

- Mobile Application
- OCR Support for Scanned PDFs
- Multi-language Support
- Advanced Recommendation System
- Analytics Dashboard
- Multi-Administrator Support

## License

This project is being developed for educational and research purposes.
