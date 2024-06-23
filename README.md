# Online Store Inventory and Supplier Management API

This REST API project provides an API for managing inventory items and suppliers for an online store.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/TolulopeJoel/invetory-management.git
   ```

2. Navigate to the project directory:
   ```
   cd invetory-management
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```


4. Activate the virtual environment:
   - For Linux/Mac:
     ```
     source venv/bin/activate
     ```
   - For Windows:
     ```
     venv\Scripts\activate
     ```

5. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Run migrations:
   ```
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Suppliers

- `GET /api/suppliers/`: List all suppliers
- `POST /api/suppliers/`: Create a new supplier
- `GET /api/suppliers/{id}/`: Retrieve a specific supplier
- `PUT /api/suppliers/{id}/`: Update a supplier
- `DELETE /api/suppliers/{id}/`: Delete a supplier

### Inventory Items

- `GET /api/inventory-items/`: List all inventory items
- `POST /api/inventory-items/`: Create a new inventory item
- `GET /api/inventory-items/{id}/`: Retrieve a specific inventory item
- `PUT /api/inventory-items/{id}/`: Update an inventory item
- `DELETE /api/inventory-items/{id}/`: Delete an inventory item

## Example Responses

### `GET /api/suppliers/`

```json
[
    {
        "id": 1,
        "name": "Supplier X",
        "items": [
            {
                "id": 1,
                "name": "Item A"
            },
            {
                "id": 2,
                "name": "Item B"
            }
        ]
    },
    {
        "id": 2,
        "name": "Supplier Y",
        "items": []
    }
]
```

### `GET /api/inventory-items/`

```json
[
    {
        "id": 1,
        "name": "Item A",
        "suppliers": [
            {
                "id": 1,
                "name": "Supplier X"
            }
        ]
    },
    {
        "id": 2,
        "name": "Item B",
        "suppliers": [
            {
                "id": 1,
                "name": "Supplier X"
            },
            {
                "id": 2,
                "name": "Supplier Y"
            }
        ]
    }
]
```

### `POST /api/inventory-items/`

**Request:**
```json
{
    "name": "Item C",
    "supplier_ids": [1, 2]
}
```

**Response:**
```json
{
    "id": 3,
    "name": "Item C",
    "suppliers": [
        {
            "id": 1,
            "name": "Supplier X"
        },
        {
            "id": 2,
            "name": "Supplier Y"
        }
    ]
}
```

### `PUT /api/inventory-items/1/`

**Request:**
```json
{
    "name": "Updated Item A",
    "supplier_ids": [2]
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Updated Item A",
    "suppliers": [
        {
            "id": 2,
            "name": "Supplier Y"
        }
    ]
}
```

## Running Tests

To execute the tests, run:

```bash
python manage.py test
```
