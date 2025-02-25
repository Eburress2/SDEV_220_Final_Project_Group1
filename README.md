# **Inventory Management System**

## **Overview**

This project is an **Inventory Management System** designed for a local retail store to automate and streamline inventory tracking and order processing. The system allows the store to manage products, track stock levels, process customer orders, and generate reports. It features a user-friendly web interface and is built using Django.

---

## **Features**

- **Product Management**: Add, update, and remove products from the inventory.
- **Category Management**: Add categories and assign products to a category.
- **Low-Stock Alerts**: Identify products with low stock levels.
- **Reporting**: Generate reports such as low-stock items and sales summaries.
- **User-Friendly Web Interface**: Built with Django for easy interaction.

---

## **Classes and UML Diagram**

The system is built around three main models:

1. **Category**: Manages product categories.
2. **Product**: Manages product details (ID, name, price, category).
3. **Inventory**: Handles product storage, updates, and low-stock alerts.

### **UML Class Diagram**

```
+-------------------+   +-------------------+    +-------------------+
|     Category      |   |     Product       |    |     Inventory     |
+-------------------+   +-------------------+    +-------------------+
| - name: str       |   | - name: str       |    | - product: OneToOne|
+-------------------+   | - price: float    |    | - quantity: int   |
                        | - category: FK    |    | - low_stock_threshold: int|
                        +-------------------+    +-------------------+
                        | + __str__()       |    | + is_low_stock()  |
                        +-------------------+    | + clean()         |
                                                 | + __str__()       |
                                                 +-------------------+
```

---

## **Installation**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Eburress2/SDEV_220_Final_Project_Group1.git
   cd SDEV_220_Final_Project_Group1
   ```

2. **Install Dependencies**:
   - Ensure Python 3.x is installed.
   - Ensure pip is installed.
   - Install the required libraries through requirements.txt:

   ```cmd
   pip install -r requirements.txt
   ```

3. **Apply Migrations:**:

   ```py
   python manage.py migrate
   ```

4. **Load Initial Data** (Optional)

   ```py
   python manage.py loaddata initial_data.json
   ```

5. **Run the Server**

   ```py
   python manage.py runserver
   ```

---

## **Usage**

1. Launch the application by navigating to http://127.0.0.1:8000/inventory in your web browser.
2. Use the web interface to:
   - Add, update, or remove products and categories
   - View low-stock alerts and generate reports.

---

## **Project Structure**

```py
inventory-management-system/
├── manage.py              # Django project management script
├── inventory/             # Inventory app
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS, images)
│   ├── admin.py           # Admin site configuration
│   ├── apps.py            # App configuration
│   ├── models.py          # Data models
│   ├── tests.py           # Tests
│   ├── urls.py            # URL routing
│   ├── views.py           # View functions and classes
│   └── forms.py           # Forms for data input
├── inventory_management/  # Project settings
│   ├── settings.py        # Project settings
│   ├── urls.py            # Project URL routing
│   └── wsgi.py            # WSGI configuration
├── fixtures/              # Initial data for the database
│   └── initial_data.json  # JSON file with initial data
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── docs/                  # Additional documentation (e.g., UML diagram)
```

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
For questions or feedback, please contact:
- **Ethan Burress**  
- **Email**: eburress2@ivytech.edu  
- **GitHub**: eburress2(https://github.com/eburress2)

