# **Inventory Management System**

## **Overview**
This project is an **Inventory Management System** designed for a local retail store to automate and streamline inventory tracking and order processing. The system allows the store to manage products, track stock levels, process customer orders, and generate reports. It features a user-friendly graphical interface (GUI) and is built using Python.

---

## **Features**
- **Product Management**: Add, update, and remove products from the inventory.
- **Order Processing**: Track customer orders and update inventory in real-time.
- **Low-Stock Alerts**: Identify products with low stock levels.
- **Reporting**: Generate reports such as low-stock items and sales summaries.
- **User-Friendly GUI**: Built with `tkinter` for easy interaction.

---

## **Classes and UML Diagram**
The system is built around three main classes:
1. **Product**: Manages product details (ID, name, price, quantity).
2. **Inventory**: Handles product storage, updates, and low-stock alerts.
3. **Order**: Tracks customer orders and calculates total costs.

### **UML Class Diagram**
```
+-------------------+       +-------------------+       +-------------------+
|     Product       |       |    Inventory      |       |      Order        |
+-------------------+       +-------------------+       +-------------------+
| - product_id: str |       | - products: dict  |       | - order_id: str   |
| - name: str       |       +-------------------+       | - products: list  |
| - price: float    |       | + add_product()   |       | - total_cost: float|
| - quantity: int   |       | + remove_product()|       +-------------------+
+-------------------+       | + update_product()|       | + add_product()   |
| + __init__()      |       | + get_low_stock() |       | + calculate_cost()|
| + update_quantity()|       | + get_details()  |       | + get_summary()   |
| + get_details()   |       +-------------------+       +-------------------+
+-------------------+
```

---

## **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   cd inventory-management-system
   ```

2. **Install Dependencies**:
   - Ensure Python 3.x is installed.
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application**:
   ```bash
   python main.py
   ```

---

## **Usage**
1. Launch the application.
2. Use the GUI to:
   - Add, update, or remove products.
   - Process customer orders.
   - View low-stock alerts and generate reports.

---

## **Project Structure**
```
inventory-management-system/
├── main.py                # Entry point for the application
├── product.py             # Product class implementation
├── inventory.py           # Inventory class implementation
├── order.py               # Order class implementation
├── gui.py                 # GUI implementation
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

