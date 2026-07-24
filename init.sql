CREATE TABLE branches (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE menu_items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price_baht INTEGER NOT NULL
);

CREATE TABLE stock (
    branch_id INTEGER NOT NULL REFERENCES branches(id),
    item_id INTEGER NOT NULL REFERENCES menu_items(id),
    quantity_available INTEGER NOT NULL CHECK (quantity_available >= 0),
    PRIMARY KEY (branch_id, item_id)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    branch_id INTEGER NOT NULL REFERENCES branches(id),
    item_id INTEGER NOT NULL REFERENCES menu_items(id),
    quantity INTEGER NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- seed data, carried over from the original KFSuay CLI (branches/menu names)
INSERT INTO branches (name, address) VALUES
    ('KFSuay Bangkok', '123 main street, square avenue Bangkok'),
    ('KFSuay Chiangmai', '26/85 luck street, north calorie Chiangmai'),
    ('KFSuay Ubon', '659/7 nop street, south western Ubon');

INSERT INTO menu_items (name, price_baht) VALUES
    ('ALL IN ONE BUCKET', 199),
    ('Chick N Share Zabb', 89),
    ('The Box Signature', 159),
    ('Suk Lon Jai', 619);

-- stock per branch/item; ALL IN ONE BUCKET at Bangkok is deliberately low
-- so the concurrency demo has something to contend over
INSERT INTO stock (branch_id, item_id, quantity_available)
SELECT b.id, i.id,
    CASE WHEN b.name = 'KFSuay Bangkok' AND i.name = 'ALL IN ONE BUCKET' THEN 10
         ELSE 100
    END
FROM branches b CROSS JOIN menu_items i;
