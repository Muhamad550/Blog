# Blog Platform - Django REST API

## 📖 Project Overview
A complete Blog Platform built with Django REST Framework that provides full CRUD operations for blog posts, categories, and comments with user authentication.

**Developer:** Muhamad550  
**Email:** ma8287225@gmail.com  
**GitHub Repository:** https://github.com/Muhamad550/Blog.git

## 🚀 Features

### Core Functionality
- User registration, login, and logout
- Create, read, update, delete blog posts
- Category-based post organization
- Comment system for user interaction
- Search and filtering capabilities

### Technical Features
- Token-based authentication
- Session authentication for browsable API
- User permissions and authorization
- RESTful API design

## 🛠 Technologies Used

- Django 5.1.4
- Django REST Framework
- SQLite3
- Token Authentication
- django-cors-headers
- django-filter

## 📁 Project Structure

```
Blog/
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
├── content_platform/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/Muhamad550/Blog.git
cd Blog
pip install -r requirements.txt
```

### Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Run Server
```bash
python manage.py runserver 8001
```

## 🌐 API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `POST /api/login/` - User login
- `POST /api/logout/` - User logout

### Blog Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create new post
- `GET /api/posts/{id}/` - Get specific post
- `PUT /api/posts/{id}/` - Update post
- `DELETE /api/posts/{id}/` - Delete post

### Categories
- `GET /api/categories/` - List all categories
- `GET /api/categories/{id}/posts/` - Posts by category

### Comments
- `GET /api/posts/{id}/comments/` - List post comments
- `POST /api/posts/{id}/comments/` - Create comment
- `GET/PUT/DELETE /api/comments/{id}/` - Comment management

## 🗄 Database Models

### User
- Extends Django's built-in User model

### Category
- `name` - Category name
- `description` - Category description

### BlogPost
- `title` - Post title
- `content` - Post content
- `author` - ForeignKey to User
- `category` - ForeignKey to Category
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

### Comment
- `post` - ForeignKey to BlogPost
- `author` - ForeignKey to User
- `content` - Comment text
- `created_at` - Comment timestamp

## ⚡ Quick Testing

### 1. Access the Application
- **API Browser:** http://127.0.0.1:8001/api/posts/
- **Admin Panel:** http://127.0.0.1:8001/admin/
- **User Registration:** http://127.0.0.1:8001/api/register/

### 2. Register a User
Visit: http://127.0.0.1:8001/api/register/
```json

### 3. Create Blog Post
Visit: http://127.0.0.1:8001/api/posts/
```json

## ⚠️ Troubleshooting

### Common Issues

**"no such table" Error**
```bash
python manage.py migrate
```

**Port Already in Use**
```bash
python manage.py runserver 8001
```

**Page Not Found (404)**
- Use specific endpoints: `/api/posts/`, `/admin/`

## 🔒 Authentication

- Token authentication for API requests
- Session authentication for browser
- Include token in headers: `Authorization: Token <your-token>`

## 📞 Support

- **GitHub:** Muhamad550
- **Email:** ma8287225@gmail.com
- **Repository:** https://github.com/Muhamad550/Blog.git

