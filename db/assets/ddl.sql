CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,  -- Password hash
  role VARCHAR(50) NOT NULL DEFAULT 'customer',  -- Roles: 'admin', 'delivery', 'customer'
  phone VARCHAR(20),
  address TEXT,
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP
);

CREATE TABLE product (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price NUMERIC(10,2) NOT NULL,
  stock INTEGER NOT NULL,
  low_stock_threshold INTEGER,  -- Threshold for low stock alert
  image_url VARCHAR(255),
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP
);

CREATE TABLE inventory_movement (
  id SERIAL PRIMARY KEY,
  product_id INTEGER NOT NULL,
  movement_type VARCHAR(20) NOT NULL,  -- Values: 'in', 'out'
  quantity INTEGER NOT NULL,
  description TEXT,  -- Details of the movement (sale, promotion, giveaway, etc.)
  movement_date TIMESTAMP NOT NULL,
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_inventory_product FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE customer (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  name VARCHAR(255) NOT NULL,
  address TEXT NOT NULL,
  phone VARCHAR(20),
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_customer_user FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE route (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  delivery_person_id INTEGER NOT NULL,  -- User with role 'delivery'
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_route_delivery FOREIGN KEY (delivery_person_id) REFERENCES users(id)
);

CREATE TABLE customer_route (
  id SERIAL PRIMARY KEY,
  route_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_customer_route_route FOREIGN KEY (route_id) REFERENCES route(id),
  CONSTRAINT fk_customer_route_customer FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE sale (
  id SERIAL PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  total NUMERIC(10,2) NOT NULL,
  payment_status VARCHAR(20) DEFAULT 'pending',  -- e.g., 'pending', 'completed', 'failed'
  sale_date TIMESTAMP NOT NULL,
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_sale_customer FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE sale_detail (
  id SERIAL PRIMARY KEY,
  sale_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  unit_price NUMERIC(10,2) NOT NULL,
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_sale_detail_sale FOREIGN KEY (sale_id) REFERENCES sale(id),
  CONSTRAINT fk_sale_detail_product FOREIGN KEY (product_id) REFERENCES product(id)
);

CREATE TABLE receipt (
  id SERIAL PRIMARY KEY,
  sale_id INTEGER NOT NULL,
  receipt_number VARCHAR(50) UNIQUE NOT NULL,
  generation_date TIMESTAMP NOT NULL,
  file_url VARCHAR(255),  -- File path of the generated receipt
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_receipt_sale FOREIGN KEY (sale_id) REFERENCES sale(id)
);

CREATE TABLE delivery (
  id SERIAL PRIMARY KEY,
  sale_id INTEGER NOT NULL,
  delivery_person_id INTEGER NOT NULL,  -- User with role 'delivery'
  delivery_status VARCHAR(20) DEFAULT 'pending',  -- e.g., 'pending', 'delivered', 'failed'
  delivery_date TIMESTAMP,
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_delivery_sale FOREIGN KEY (sale_id) REFERENCES sale(id),
  CONSTRAINT fk_delivery_person FOREIGN KEY (delivery_person_id) REFERENCES users(id)
);

CREATE TABLE payment (
  id SERIAL PRIMARY KEY,
  sale_id INTEGER NOT NULL,
  amount NUMERIC(10,2) NOT NULL,
  payment_date TIMESTAMP NOT NULL,
  payment_method VARCHAR(50),  -- e.g., 'cash', 'card'
  status VARCHAR(20) DEFAULT 'pending',
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_payment_sale FOREIGN KEY (sale_id) REFERENCES sale(id)
);

CREATE TABLE supplier (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  contact TEXT,
  commission NUMERIC(5,2),  -- Percentage or fixed amount
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP
);

CREATE TABLE product_supplier (
  id SERIAL PRIMARY KEY,
  product_id INTEGER NOT NULL,
  supplier_id INTEGER NOT NULL,
  cost NUMERIC(10,2) NOT NULL,
  created_by INTEGER,
  created_at TIMESTAMP,
  updated_by INTEGER,
  updated_at TIMESTAMP,
  CONSTRAINT fk_product_supplier_product FOREIGN KEY (product_id) REFERENCES product(id),
  CONSTRAINT fk_product_supplier_supplier FOREIGN KEY (supplier_id) REFERENCES supplier(id)
);
