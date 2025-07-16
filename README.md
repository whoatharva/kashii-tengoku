# Kata Sweet Shop Management System

A simple Flask web app to manage sweets inventory, including add, delete, purchase, restock, search, and sort features.

## Features
- Add, delete, purchase, and restock sweets
- Search and sort sweets by name, price, or quantity
- Prevent purchase if out of stock
- Simple Bootstrap-based web interface

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the app:
   ```
   python app.py
   ```
3. Open your browser to [http://localhost:5000](http://localhost:5000)

## Running Tests (TDD)
This project uses **pytest** for test-driven development.

To run all tests:
```
pytest
```

All core features (add, delete, purchase, restock, search, sort, etc.) are covered by tests in the `tests/` directory.

## Project Structure
- `app.py` — Main Flask app
- `templates/` — HTML templates
- `requirements.txt` — Python dependencies
- `tests/` — Automated tests (TDD)

## Notes
- Uses SQLite for storage (creates `sweets.db` in the project folder)
- No authentication (for demo purposes) 