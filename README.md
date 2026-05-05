# CRUD Web Services

A comprehensive CRUD (Create, Read, Update, Delete) web service built with FastAPI and PostgreSQL, featuring a clean separation of concerns with controllers and routes, along with a simple web UI.

## Features

- **Full CRUD Operations**: Create, read, update, and delete items
- **RESTful API**: Well-structured REST endpoints
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Data Validation**: Pydantic schemas for request/response validation
- **CORS Support**: Cross-origin resource sharing enabled
- **Interactive Documentation**: Swagger UI at `/docs`
- **Web UI**: Simple HTML interface for testing operations
- **Modular Architecture**: Separated controllers and routes for maintainability

## Tech Stack

- **Backend**: FastAPI (Python web framework)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Frontend**: Vanilla HTML/CSS/JavaScript

## Project Structure

```
CRUDWS/
├── app/
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── items.py          # Business logic for item operations
│   ├── routes/
│   │   ├── __init__.py
│   │   └── items.py          # API route definitions
│   ├── __init__.py
│   ├── database.py           # Database configuration
│   ├── main.py               # FastAPI app initialization
│   ├── models.py             # SQLAlchemy models
│   └── schemas.py            # Pydantic schemas
├── ui/
│   └── index.html            # Web interface
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── CRUDWS.postman_collection.json  # Postman collection for API testing
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/arpitklu/CRUDWS.git
   cd CRUDWS
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL database**:
   - Create a database named `crud_db`
   - Create a file named `.env` in the project root
   - Add the database connection string to `.env` 

5. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## Usage

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/docs` | Interactive API documentation |
| POST | `/items` | Create a new item |
| GET | `/items` | Get all items |
| GET | `/items/{item_id}` | Get a specific item by ID |
| PUT | `/items/{item_id}` | Update an existing item |
| DELETE | `/items/{item_id}` | Delete an item |

### Request/Response Examples

**Create Item**:
```bash
POST /items
Content-Type: application/json

{
  "name": "Sample Item",
  "description": "This is a sample item"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "This is a sample item"
}
```

### Web UI

Open `ui/index.html` in your browser to access the web interface for testing CRUD operations.

## Data Model

### Item
- `id`: Integer (Primary Key, Auto-generated)
- `name`: String (Required)
- `description`: String (Required)

## Development

### Running Tests

```bash
# Install test dependencies if any
pip install pytest

# Run tests
pytest
```

### Code Style

Follow PEP 8 guidelines for Python code.

### Database Migrations

The application uses SQLAlchemy's `create_all` for schema creation. For production, consider using Alembic for migrations.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## API Testing

Import `CRUDWS.postman_collection.json` into Postman to test the API endpoints.

## Support

For questions or issues, please open an issue on GitHub.
