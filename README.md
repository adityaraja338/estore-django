# estore - Simple Django E-commerce Backend

This is a basic e-commerce backend built with Django and Django REST Framework. It provides API endpoints for products, categories, cart, orders, and user authentication using JWT. Suitable for learning, prototyping, or as a side project.

## Features
- User registration, login, and JWT authentication
- Product and category management
- Shopping cart (add/remove/view items)
- Order placement and order history
- Simple, clean API endpoints for frontend integration

## Tech Stack
- Python 3
- Django 5
- Django REST Framework
- djangorestframework-simplejwt (JWT auth)
- PostgreSQL (default, can use SQLite for dev)

## Setup
1. **Clone the repo:**
   ```sh
   git clone <your-repo-url>
   cd estore
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   # or use Pipenv
   pipenv install
   ```
3. **Configure database:**
   - Edit `estore/settings.py` for your DB settings (PostgreSQL or SQLite).
4. **Run migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser (admin):**
   ```sh
   python manage.py createsuperuser
   ```
6. **Run the server:**
   ```sh
   python manage.py runserver
   ```

## API Endpoints
### Auth
- `POST /api/auth/register/` — Register new user
- `POST /api/auth/login/` — Obtain JWT token
- `POST /api/auth/token/refresh/` — Refresh JWT token
- `GET /api/auth/profile/` — Get current user profile

### Products & Categories
- `GET /api/products/` — List products
- `POST /api/products/` — Create product
- `GET /api/categories/` — List categories
- `POST /api/categories/` — Create category

### Cart
- `GET /api/cart/` — View cart
- `POST /api/cart/add/` — Add product to cart
- `POST /api/cart/remove/` — Remove product from cart

### Orders
- `POST /api/orders/` — Place order
- `GET /api/orders/` — List user orders

## Notes
- All endpoints (except registration/login) require JWT authentication.
- This project is for learning and prototyping, not production use.

---

Feel free to extend or modify as needed! 