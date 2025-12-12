### AI-Powered Adaptive Math Learning Prototype

This project implements an adaptive learning system that adjusts math problem difficulty based on learner performance. It demonstrates how personalized learning can be achieved using simple adaptive logic.

## Overview

The system presents math problems to children aged 5–10 and adapts difficulty based on their accuracy and response time. It highlights the impact of adaptive behavior on maintaining an optimal challenge level.

## Features

- Three difficulty levels: Easy, Medium, Hard

- Automatic difficulty adjustment based on recent performance

- Tracks accuracy and response time

- Generates an end-of-session summary

- Modular and clean Python implementation

## Project Structure
math-adaptive-prototype/
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ main.py
│  ├─ puzzle_generator.py
│  ├─ tracker.py
│  └─ adaptive_engine.py

## Installation and Setup

- Clone the repository:

git clone https://github.com/Murkivishnupriya/math-adaptive-prototype.git
cd math-adaptive-prototype


- Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate

- Install dependencies:

pip install -r requirements.txt

- Running the Application

cd src
python main.py

The application guides the user through choosing a difficulty, solving problems, and viewing the final summary.

## Module Descriptions

puzzle_generator.py — Generates math problems for three difficulty levels using basic arithmetic operations.
tracker.py — Records correctness, response time, and difficulty. Produces a summary containing accuracy and average time.
adaptive_engine.py — Applies rule-based logic to adjust difficulty depending on performance.
main.py — Controls the user flow and integrates all components.

## Future Improvements

Add machine learning–based adaptation

Introduce additional math concepts

Build a graphical or web-based interface

Track long-term user progress

## License

This project is intended for educational and demonstration purposes.

## Developer 

Murki Vishnupriya 
