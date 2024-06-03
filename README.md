# SaifaiSmart API

SaifaiSmart API is a Django-based RESTful API for managing grocery products. It provides endpoints for retrieving and adding grocery products to the database.

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/Vaibhavyadav350/SaifaiSmart
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Django server:

```
python manage.py runserver
```

3. To Deploy check `http://0.0.0.0:8000` through 

```
waitress-serve --port=8000 smart.wsgi:application
```

## Usage

### Endpoints

- **GET** `/api/products/get`: Retrieve a list of grocery products in `json` format. 
```json
[
    {
        "_id": "60bd314fc4e76e001b61db9b",
        "name": "Milk",
        "category": "Dairy",
        "price": "2.99",
        "description": "Fresh cow milk"
    },
    {
        "_id": "60bd3165c4e76e001b61db9c",
        "name": "Cheese",
        "category": "Dairy",
        "price": "5.49",
        "description": "Cheddar cheese"
    }
]
```

- **POST** `/api/products/v1/post` : Add a new grocery product to the database.
```json
{
    "name": "Bread",
    "category": "Bakery",
    "price": "1.99",
    "description": "Whole wheat bread"
}
```

- You can filter the products by category by providing the `name` query parameter.
```
GET /api/products/get?name=Bread
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize it further based on your specific needs or preferences! Let me know if you need any further assistance.
