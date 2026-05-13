# isbn-api-integration

This Python utility provides a terminal interface for querying book titles from the Open Library API using ISBN identifiers. It is built with a focus on system reliability and diagnostic logging, ensuring that all network issues or data discrepancies are recorded for later review.

Features
Dynamic API Integration: Leverages the Open Library JSON API to retrieve real-time book metadata.

Diagnostic Logging: Implements a dedicated error-handling layer that records failures to integration_errors.log.

Resilient Logic: Handles "Empty Payload" scenarios where the API returns a successful connection but no data.

Sanitized Interaction: Uses .strip() to ensure user input is cleaned of accidental whitespace before the request is sent.

Project Structure
isbn_api_integration.py: The primary script containing the request logic and terminal interface.

integration_errors.log: A persistent log file that tracks timestamps, error levels, and specific ISBN failure details.

Technical Specifications
Language: Python 3.x

Key Libraries: requests for HTTP communication and logging for telemetry.

Error Handling: Employs try-except blocks to catch RequestException errors, preventing program crashes during network instability.

Setup and Usage
Dependencies: Ensure the requests library is installed via pip:

Bash
pip install requests
Execution: Run the script from your terminal:

Bash
python3 isbn_api_integration.py
Interaction: Enter an ISBN when prompted. Valid titles will be printed to the console, while errors will be logged silently to the background file.

Developmental Context
This project demonstrates competency in Python scripting, API consumption, and software maintenance—skills directly applicable to my experience as a Learning Ambassador at Amazon and my ongoing studies in Computer Science.
