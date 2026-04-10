DROP TABLE IF EXISTS tles;

CREATE TABLE IF NOT EXISTS tles (
    id SERIAL PRIMARY KEY,
    satellite_id INT NOT NULL,
    satellite_name VARCHAR(100),
    line1 TEXT NOT NULL,
    line2 TEXT NOT NULL,
    epoch TIMESTAMP NOT NULL,
    source VARCHAR(50) DEFAULT 'Space-Track',
    inserted_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(satellite_id, epoch)
);

INSERT INTO tles(id, satellite_id, satellite_name, line1, line2, epoch)
VALUES (1, 1, 'TEST', 'LINE 1', 'LINE 2', NOW())
ON CONFLICT(id)
DO UPDATE SET 
    epoch = NOW();