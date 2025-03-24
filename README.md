GizmoGalaxy 🛒
A dynamic e-commerce web application built with Django, offering product listings, user authentication, order management, and a seamless shopping experience.

🚀 Features
User Authentication – Sign up, log in, and log out functionality with session-based access.

Product Management – Dynamic product listing with filtering, pagination, and detailed product pages.

Shopping Cart – Add, remove, and update cart items with subtotal, tax, and total price calculations.

Order Processing – Order confirmation system with order history tracking.

Admin Panel – Manage products, orders, and users with search and filter options.

UI/UX Enhancements – Blue-themed styling, rupee symbols near prices, and optimized navigation.

🏗 Tech Stack
Backend: Django, Python, PostgreSQL

Frontend: HTML, CSS, JavaScript

Authentication: Django's built-in auth system

![image](https://github.com/user-attachments/assets/28e8d120-5e8d-4b6a-813c-be61ffe09de4)

📂 Project Structure
bash
Copy
Edit
/gizmogalaxy  
│── /orders  
│── /product  
│── /themes  
│── /customers  
│── /static (CSS, images, JS)  
│── /templates (HTML files)  
│── manage.py  
│── db.sqlite3 (or PostgreSQL)  
🔧 Setup & Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/GizmoGalaxy.git
cd GizmoGalaxy
Set up a virtual environment

bash
Copy
Edit
python -m venv venv_gizmogalaxy  
source venv_gizmogalaxy/bin/activate  # On Windows use: venv_gizmogalaxy\Scripts\activate  
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt  
Apply migrations

bash
Copy
Edit
python manage.py migrate  
Create a superuser (for admin access)

bash
Copy
Edit
python manage.py createsuperuser  
Run the server

bash
Copy
Edit
python manage.py runserver  
Access the project


🤝 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

📜 License
This project is licensed under the MIT License.
