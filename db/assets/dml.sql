-- Insertar 3 registros en la tabla users
INSERT INTO users (username, email, password, role, phone, address, created_by, created_at, updated_by, updated_at)
VALUES
  ('admin', 'admin@example.com', 'hashed_password', 'admin', '123456789', 'Admin Address', 1, '2023-01-01 10:00:00', 1, '2023-01-01 10:00:00'),
  ('delivery', 'delivery@example.com', 'hashed_password', 'delivery', '987654321', 'Delivery Address', 1, '2023-01-02 10:00:00', 1, '2023-01-02 10:00:00'),
  ('customer1', 'customer1@example.com', 'hashed_password', 'customer', '555555555', 'Customer Address', 1, '2023-01-03 10:00:00', 1, '2023-01-03 10:00:00');

-- Insertar 3 registros en la tabla product
INSERT INTO product (name, description, price, stock, low_stock_threshold, image_url, created_by, created_at, updated_by, updated_at)
VALUES
  ('Chocolate Cake', 'Delicious chocolate cake', 20.00, 50, 5, 'http://example.com/chocolate.jpg', 1, '2023-01-04 10:00:00', 1, '2023-01-04 10:00:00'),
  ('Vanilla Cupcake', 'Tasty vanilla cupcake', 3.50, 100, 10, 'http://example.com/vanilla.jpg', 1, '2023-01-04 11:00:00', 1, '2023-01-04 11:00:00'),
  ('Red Velvet Cake', 'Fresh red velvet cake', 25.00, 30, 3, 'http://example.com/redvelvet.jpg', 1, '2023-01-04 12:00:00', 1, '2023-01-04 12:00:00');

-- Insertar 3 registros en la tabla inventory_movement
INSERT INTO inventory_movement (product_id, movement_type, quantity, description, movement_date, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 'in', 50, 'Initial stock for Chocolate Cake', '2023-01-05 09:00:00', 1, '2023-01-05 09:00:00', 1, '2023-01-05 09:00:00'),
  (2, 'in', 100, 'Initial stock for Vanilla Cupcake', '2023-01-05 09:15:00', 1, '2023-01-05 09:15:00', 1, '2023-01-05 09:15:00'),
  (3, 'in', 30, 'Initial stock for Red Velvet Cake', '2023-01-05 09:30:00', 1, '2023-01-05 09:30:00', 1, '2023-01-05 09:30:00');

-- Insertar 3 registros en la tabla customer
-- Se referencia el único usuario de rol 'customer' (id = 3)
INSERT INTO customer (user_id, name, address, phone, created_by, created_at, updated_by, updated_at)
VALUES
  (3, 'Alice Smith', '123 Main St', '111-222-3333', 1, '2023-01-06 10:00:00', 1, '2023-01-06 10:00:00'),
  (3, 'Bob Johnson', '456 Oak Ave', '222-333-4444', 1, '2023-01-06 10:05:00', 1, '2023-01-06 10:05:00'),
  (3, 'Charlie Davis', '789 Pine Rd', '333-444-5555', 1, '2023-01-06 10:10:00', 1, '2023-01-06 10:10:00');

-- Insertar 3 registros en la tabla route
-- Se utiliza el usuario de id = 2 (delivery) para la asignación de repartidor
INSERT INTO route (name, description, delivery_person_id, created_by, created_at, updated_by, updated_at)
VALUES
  ('Route A', 'Northern route', 2, 1, '2023-01-07 08:00:00', 1, '2023-01-07 08:00:00'),
  ('Route B', 'Central route', 2, 1, '2023-01-07 08:15:00', 1, '2023-01-07 08:15:00'),
  ('Route C', 'Southern route', 2, 1, '2023-01-07 08:30:00', 1, '2023-01-07 08:30:00');

-- Insertar 3 registros en la tabla customer_route
INSERT INTO customer_route (route_id, customer_id, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 1, 1, '2023-01-08 09:00:00', 1, '2023-01-08 09:00:00'),
  (2, 2, 1, '2023-01-08 09:05:00', 1, '2023-01-08 09:05:00'),
  (3, 3, 1, '2023-01-08 09:10:00', 1, '2023-01-08 09:10:00');

-- Insertar 3 registros en la tabla sale
INSERT INTO sale (customer_id, total, payment_status, sale_date, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 20.00, 'pending', '2023-01-09 10:00:00', 1, '2023-01-09 10:00:00', 1, '2023-01-09 10:00:00'),
  (2, 7.00, 'completed', '2023-01-09 10:15:00', 1, '2023-01-09 10:15:00', 1, '2023-01-09 10:15:00'),
  (3, 25.00, 'failed', '2023-01-09 10:30:00', 1, '2023-01-09 10:30:00', 1, '2023-01-09 10:30:00');

-- Insertar 3 registros en la tabla sale_detail
INSERT INTO sale_detail (sale_id, product_id, quantity, unit_price, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 1, 1, 20.00, 1, '2023-01-09 10:05:00', 1, '2023-01-09 10:05:00'),
  (2, 2, 2, 3.50, 1, '2023-01-09 10:20:00', 1, '2023-01-09 10:20:00'),
  (3, 3, 1, 25.00, 1, '2023-01-09 10:35:00', 1, '2023-01-09 10:35:00');

-- Insertar 3 registros en la tabla receipt
INSERT INTO receipt (sale_id, receipt_number, generation_date, file_url, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 'R001', '2023-01-09 10:10:00', 'http://example.com/receipt1.pdf', 1, '2023-01-09 10:10:00', 1, '2023-01-09 10:10:00'),
  (2, 'R002', '2023-01-09 10:25:00', 'http://example.com/receipt2.pdf', 1, '2023-01-09 10:25:00', 1, '2023-01-09 10:25:00'),
  (3, 'R003', '2023-01-09 10:40:00', 'http://example.com/receipt3.pdf', 1, '2023-01-09 10:40:00', 1, '2023-01-09 10:40:00');

-- Insertar 3 registros en la tabla delivery
INSERT INTO delivery (sale_id, delivery_person_id, delivery_status, delivery_date, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 2, 'pending', '2023-01-10 11:00:00', 1, '2023-01-10 11:00:00', 1, '2023-01-10 11:00:00'),
  (2, 2, 'delivered', '2023-01-10 11:15:00', 1, '2023-01-10 11:15:00', 1, '2023-01-10 11:15:00'),
  (3, 2, 'failed', '2023-01-10 11:30:00', 1, '2023-01-10 11:30:00', 1, '2023-01-10 11:30:00');

-- Insertar 3 registros en la tabla payment
INSERT INTO payment (sale_id, amount, payment_date, payment_method, status, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 20.00, '2023-01-10 12:00:00', 'cash', 'pending', 1, '2023-01-10 12:00:00', 1, '2023-01-10 12:00:00'),
  (2, 7.00, '2023-01-10 12:15:00', 'card', 'completed', 1, '2023-01-10 12:15:00', 1, '2023-01-10 12:15:00'),
  (3, 25.00, '2023-01-10 12:30:00', 'cash', 'failed', 1, '2023-01-10 12:30:00', 1, '2023-01-10 12:30:00');

-- Insertar 3 registros en la tabla supplier
INSERT INTO supplier (name, contact, commission, created_by, created_at, updated_by, updated_at)
VALUES
  ('Supplier A', 'Contact A', 5.00, 1, '2023-01-11 09:00:00', 1, '2023-01-11 09:00:00'),
  ('Supplier B', 'Contact B', 7.50, 1, '2023-01-11 09:15:00', 1, '2023-01-11 09:15:00'),
  ('Supplier C', 'Contact C', 10.00, 1, '2023-01-11 09:30:00', 1, '2023-01-11 09:30:00');

-- Insertar 3 registros en la tabla product_supplier
INSERT INTO product_supplier (product_id, supplier_id, cost, created_by, created_at, updated_by, updated_at)
VALUES
  (1, 1, 15.00, 1, '2023-01-12 10:00:00', 1, '2023-01-12 10:00:00'),
  (2, 2, 2.50, 1, '2023-01-12 10:15:00', 1, '2023-01-12 10:15:00'),
  (3, 3, 18.00, 1, '2023-01-12 10:30:00', 1, '2023-01-12 10:30:00');
