# gdpr-validator
The gdpr valdiator aims to validate whether given text, images, or PDFs contain any content that is not compliant with GDPR regulations.
Utilizing Large Language Models (LLMs), the API will allow users to configure custom compliance rules and track any overrides made to standard GDPR rules. 

Validate input data (text, images, PDFs) for GDPR compliance.
Allow users to configure custom compliance rules and override existing ones.

Provide audit trails for any overrides made by users.
Offer a seamless integration experience with other components or services.

This document outlines the functional specifications for a web application architecture comprising a front-end built with React/Next.js, a back-end utilizing Python and FastAPI, and an integrated Large Language Model (LLM) named "LLM-Gemini". The system is designed to facilitate user interactions, process requests, and generate outputs through advanced language processing.

System Components
1. Front-End
Framework: Built using React and Next.js.
User Interaction: Handles all user interactions with the application.
Content Types: Capable of displaying various content formats including:
Text
PDFs
Images
Rules
Audit reports

2. Back-End
Technologies Used:
Python
FastAPI for building APIs.
LangChain and LangGraph for managing language model interactions.
SQLite as the database solution.

Functionalities:
API Access: Expose endpoints for front-end communication.
Workflow Management: Handle user workflows and state management.
Agent Interaction: Manage interactions with various agents or services.
Model Invocation: Trigger calls to the LLM for processing requests.
Rules Configuration: Allow users to define and manage operational rules.
Report Generation: Create and serve reports based on processed data.

3. Large Language Model (LLM)

Model Name: LLM-Gemini.
Purpose: Executes complex language-based tasks such as:
Natural language understanding and generation.
Processing user queries and generating relevant responses or outputs.
Integration: The back-end interacts with the LLM to facilitate advanced processing capabilities.
