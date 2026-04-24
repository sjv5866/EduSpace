DROP TABLE IF EXISTS tles;

CREATE TABLE IF NOT EXISTS tles (
    id SERIAL PRIMARY KEY,
    satellite_id INT NOT NULL,
    satellite_name VARCHAR(100),
    line1 TEXT NOT NULL,
    line2 TEXT NOT NULL,
    source VARCHAR(50) DEFAULT 'TEST',
    inserted_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(satellite_id)
);

INSERT INTO tles(satellite_id, satellite_name, line1, line2)
VALUES (1, 'TEST', 'LINE 1', 'LINE 2')
ON CONFLICT(satellite_id)
DO UPDATE SET 
    inserted_at = NOW();