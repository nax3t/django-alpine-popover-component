# Django Components Demo

A basic Django 5 application for exploring django-components.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Available Components

### Popover
An interactive popover menu component built with Alpine.js. Perfect for dropdowns, menus, and tooltips.
[View Popover Documentation](main/components/popover/README.md)

Visit http://127.0.0.1:8000/ to see the application.
