
# Llama-2 Chatbot Backend with FastAPI and PostgreSQL

## Description

This project provides a backend implementation for a chatbot using the Llama-2 model, integrated with FastAPI and a PostgreSQL database. It allows users to interact with the chatbot and stores chat data in the database.

## Table of Contents

- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL

### Steps

1. Clone the repository:
   ```sh
   git clone <repository_link>
   ```
2. Navigate to the project directory:
   ```sh
   cd <project_directory>
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Setup the PostgreSQL database and update the connection details in `database_updated.py`.

5. Run the FastAPI application:
   ```sh
   uvicorn main_updated:app --reload
   ```

## Usage

The API provides endpoints to interact with the Llama-2 chatbot and store conversation data in a PostgreSQL database. The detailed API documentation can be accessed at `<your_server_url>/docs` once the server is running.

## Contributing

Contributions, issues, and feature requests are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is [MIT](LICENSE) licensed.
