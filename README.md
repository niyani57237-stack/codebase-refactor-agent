# Codebase Refactor Agent

Codebase Refactor Agent is a lightweight multi-agent system for automated Python codebase analysis, refactoring suggestions, test planning and Markdown report generation.

## Project Overview

This project builds a multi-agent workflow for small and medium-sized Python repositories. It can scan local code files, analyze project structure, detect possible code quality issues, generate refactoring suggestions, provide unit test planning ideas, and export a structured Markdown report.

## Core Pain Points

Many small code projects suffer from unclear structure, inconsistent naming, long functions, insufficient comments, lack of testing plans, and low efficiency in manual code review. This project aims to provide an automated assistant that helps developers quickly understand and improve a codebase.

## Multi-Agent Architecture

The system contains several agents:

- Scanner Agent: scans the target codebase and collects Python files.
- Structure Agent: analyzes functions, classes, imports and code scale.
- Quality Agent: detects potential quality issues.
- Refactor Agent: generates refactoring suggestions.
- Test Agent: generates unit test planning suggestions.
- Report Agent: writes the final Markdown report.
- Manager Agent: coordinates the whole workflow.

## Workflow

The core logic flow is:

Code scanning → Structure analysis → Quality diagnosis → Refactoring planning → Test planning → Report generation

## Features

- Automatic Python file scanning
- AST-based structure analysis
- Function and class statistics
- Basic code quality issue detection
- Refactoring recommendation generation
- Unit test suggestion generation
- Markdown report output
- Multi-agent style terminal logs

## How to Run

```bash
python main.py

