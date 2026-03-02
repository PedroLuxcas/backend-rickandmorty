## **README.md - Rick and Morty API Backend**

```markdown
# 🚀 Rick and Morty API

A RESTful API built with Flask that serves data from the Rick and Morty universe. This API provides information about characters, episodes, locations, and their relationships.

## 📋 Table of Contents
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running the Application](#-running-the-application)
- [API Endpoints](#-api-endpoints)
- [Response Format](#-response-format)
- [Examples](#-examples)
- [Database Schema](#-database-schema)
- [Contributing](#-contributing)
- [License](#-license)

## 🛠 Technologies

- **Python 3.9+**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM for database interactions
- **Flask-Marshmallow** - Object serialization/deserialization
- **PostgreSQL** - Database
- **python-dotenv** - Environment variables management

## ✨ Features

- ✅ RESTful API design
- ✅ Pagination support (20 items per page default)
- ✅ Complete character information including last episode appearance
- ✅ Location details with residents count
- ✅ Episode information
- ✅ Standardized API responses
- ✅ Clean architecture (Repository/Service/Controller pattern)
- ✅ Marshmallow schemas for data serialization

## 📁 Project Structure

```
backend/
├── app/
│   ├── __init__.py                 # Flask application factory
│   ├── models/                      # Database models
│   │   ├── __init__.py
│   │   ├── character.py
│   │   ├── episode.py
│   │   ├── location.py
│   │   └── character_episode.py     # Association table
│   ├── schemas/                      # Marshmallow schemas
│   │   ├── __init__.py
│   │   ├── character_schema.py
│   │   ├── episode_schema.py
│   │   └── location_schema.py
│   ├── repositories/                  # Data access layer
│   │   ├── __init__.py
│   │   └── character_repository.py
│   ├── services/                       # Business logic layer
│   │   ├── __init__.py
│   │   └── character_service.py
│   ├── controllers/                     # Request handlers
│   │   ├── __init__.py
│   │   └── character_controller.py
│   ├── routes/                           # API routes
│   │   ├── __init__.py
│   │   └── character_routes.py
│   └── utils/                             # Utilities
│       ├── __init__.py
│       └── api_response.py                 # Standardized responses
├── config/
│   ├── __init__.py
│   └── settings.py                         # Configuration classes
├── .env                                     # Environment variables
├── requirements.txt                         # Dependencies
└── run.py                                    # Application entry point
```

## 🔧 Installation

### Prerequisites
- Python 3.9 or higher
- PostgreSQL installed and running
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/PedroLuxcas/rick-and-morty-api.git
cd rick-and-morty-api/backend
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## ⚙ Configuration

1. **Create a `.env` file** in the root directory:
```env
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1

# Database Configuration
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/rickandmorty_db
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=rickandmorty_db
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
```

2. **Create the database**
```bash
# Access PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE rickandmorty_db;

# Exit
\q
```

3. **Import data** (if you have seed data)
```bash
python scripts/populate_database.py
```

## 🚀 Running the Application

```bash
# Make sure you're in the backend directory with venv activated
python run.py
```

The server will start at `http://localhost:5000`

You should see:
```
🚀 Server running at http://localhost:5000
📡 Environment: development
✅ Database synchronized
```

## 📡 API Endpoints

### Characters

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/api/characters/` | List all characters (paginated) | `?page=1&per_page=20` |
| GET | `/api/characters/<id>` | Get character by ID | - |

### Query Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | integer | 1 | Page number |
| `per_page` | integer | 20 | Items per page (max 100) |

## 📦 Response Format

All responses follow a standardized format:

### Success Response
```json
{
    "success": true,
    "message": "Operation successful",
    "data": { ... }
}
```

### Error Response
```json
{
    "success": false,
    "message": "Error message",
    "data": null
}
```

## 📝 Examples

### Get all characters (page 1)
```bash
GET http://localhost:5000/api/characters/?page=1&per_page=20
```

**Response:**
```json
{
    "success": true,
    "message": "Characters retrieved successfully",
    "data": {
        "items": [
            {
                "id": 1,
                "name": "Rick Sanchez",
                "status": "Alive",
                "species": "Human",
                "type": "",
                "gender": "Male",
                "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
                "origin": {
                    "id": 1,
                    "name": "Earth (C-137)",
                    "type": "Planet",
                    "dimension": "Dimension C-137",
                    "residents_count": 42
                },
                "current_location": {
                    "id": 3,
                    "name": "Citadel of Ricks",
                    "type": "Citadel",
                    "dimension": "Unknown",
                    "residents_count": 156
                },
                "last_episode": {
                    "id": 51,
                    "name": "Rick: A Mort Well Lived",
                    "air_date": "September 5, 2021",
                    "episode": "S05E10"
                },
                "total_episodes": 51
            }
            // ... more characters
        ],
        "total": 826,
        "page": 1,
        "pages": 42,
        "per_page": 20,
        "has_next": true,
        "has_prev": false
    }
}
```

### Get character by ID
```bash
GET http://localhost:5000/api/characters/1
```

**Response:**
```json
{
    "success": true,
    "message": "Character retrieved successfully",
    "data": {
        "id": 1,
        "name": "Rick Sanchez",
        "status": "Alive",
        "species": "Human",
        "type": "",
        "gender": "Male",
        "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
        "origin": {
            "id": 1,
            "name": "Earth (C-137)",
            "type": "Planet",
            "dimension": "Dimension C-137",
            "residents_count": 42
        },
        "current_location": {
            "id": 3,
            "name": "Citadel of Ricks",
            "type": "Citadel",
            "dimension": "Unknown",
            "residents_count": 156
        },
        "last_episode": {
            "id": 51,
            "name": "Rick: A Mort Well Lived",
            "air_date": "September 5, 2021",
            "episode": "S05E10"
        },
        "total_episodes": 51
    }
}
```

## 💾 Database Schema

### Tables

**characters**
- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR)
- `status` (VARCHAR)
- `species` (VARCHAR)
- `type` (VARCHAR)
- `gender` (VARCHAR)
- `image` (TEXT)
- `origin_id` (INTEGER, FOREIGN KEY)
- `location_id` (INTEGER, FOREIGN KEY)
- `created_at` (TIMESTAMP)

**episodes**
- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR)
- `air_date` (VARCHAR)
- `episode` (VARCHAR)
- `created_at` (TIMESTAMP)

**locations**
- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR)
- `type` (VARCHAR)
- `dimension` (VARCHAR)
- `created_at` (TIMESTAMP)

**character_episodes** (association table)
- `character_id` (INTEGER, FOREIGN KEY, PRIMARY KEY)
- `episode_id` (INTEGER, FOREIGN KEY, PRIMARY KEY)
- `created_at` (TIMESTAMP)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Pedro Nascimentp - [@PedroLuxcas](https://github.com/PedroLuxcas)

## 🙏 Acknowledgments

- [Rick and Morty API](https://rickandmortyapi.com/) for the data
- Flask community for the excellent documentation
- All contributors and users of this API

---