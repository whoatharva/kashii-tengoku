# Kashii Tengoku 樫天国

> **Note:** This project was developed using Test-Driven Development (TDD). All development and commits were maintained locally in a clean, incremental history, and the codebase was pushed to GitHub only after the project was complete and well-structured.

A modern, web-based inventory management system for a Japanese sweet shop, built with Flask. Kashii Tengoku (樫天国) lets you easily add, delete, purchase, restock, search, and sort sweets in your shop. The project is designed for learning, simplicity, and test-driven development (TDD).

---

## Features
- Add, delete, purchase, and restock sweets
- Search and sort sweets by name, price, or quantity
- Prevent purchase if out of stock
- Responsive, Bootstrap-based web interface
- Sample data for quick start
- Test-driven development with pytest

---


## Quickstart

### 1. Clone the repository
```sh
git clone <your-repo-url>
cd kashii-tengoku
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Initialize the database
You can initialize the database and populate it with sample sweets using the Flask CLI:
```sh
flask --app app.py init-db
```
Or, the database will be created automatically when you first run the app.

### 4. Run the application
```sh
python app.py
```
Then open your browser to [http://localhost:5000](http://localhost:5000)

---

## Usage
- **Add Sweet:** Click "Add Sweet" to add a new sweet to the inventory.
- **Purchase/Restock:** Use the buttons in the table to purchase or restock items.
- **Delete:** Remove a sweet from the inventory.
- **Search/Sort:** Use the search bar and sort options to find and organize sweets.

---

## Running Tests
This project uses **pytest** for TDD. To run all tests:
```sh
pytest
```
All core features are covered by tests in the `tests/` directory.

---

## Project Structure
```
Kata_Sweet_Shop/
├── app.py                # Main Flask app and entry point
├── codes/
│   ├── models/           # Database models
│   ├── services/         # Business logic and database operations
│   └── routes/           # Flask route blueprints
├── templates/            # HTML templates
├── static/               # CSS and images
├── tests/                # Automated tests (TDD)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Troubleshooting
- If you see database errors, try running the `init-db` command above.
- The app uses SQLite and creates `sweets.db` in the `instance/` folder.
- For any issues, ensure all dependencies are installed and you are using Python 3.7+.

---

## Contributing
Pull requests and suggestions are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Credits
- Project by [Atharva]
- Inspired by Japanese wagashi (和菓子) culture
- Built with [Flask](https://flask.palletsprojects.com/), [Bootstrap](https://getbootstrap.com/), and [pytest](https://pytest.org/) 