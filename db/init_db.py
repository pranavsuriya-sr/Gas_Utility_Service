import sqlite3
from datetime import datetime

init_script = """
DROP TABLE IF EXISTS "requestData";
DROP TABLE IF EXISTS "serviceData";
DROP TABLE IF EXISTS "customerData";
DROP TABLE IF EXISTS "repData";
DROP TABLE IF EXISTS "adminData";
DROP TABLE IF EXISTS "userAsks";

CREATE TABLE IF NOT EXISTS "adminData" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "firstName" TEXT NOT NULL,
    "lastName" TEXT NOT NULL,
    "email" TEXT UNIQUE NOT NULL,
    "password" TEXT NOT NULL,
    "phoneNumber" TEXT NOT NULL,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "lastUpdatedAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "adminData" ("firstName", "lastName", "email", "password", "phoneNumber") VALUES ('Admin', 'Admin', 'admin@gas.io', 'admin1234', '0000000000');

-- Table for customer support representatives
CREATE TABLE IF NOT EXISTS "repData" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "firstName" TEXT NOT NULL,
    "lastName" TEXT NOT NULL,
    "email" TEXT UNIQUE NOT NULL,
    "password" TEXT NOT NULL,
    "phoneNumber" TEXT NOT NULL,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "lastUpdatedAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing customer details
CREATE TABLE IF NOT EXISTS "customerData" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "firstName" TEXT NOT NULL,
    "lastName" TEXT NOT NULL,
    "email" TEXT UNIQUE NOT NULL,
    "password" TEXT NOT NULL,
    "phoneNumber" TEXT NOT NULL,
    "address" TEXT NOT NULL,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "lastUpdatedAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO "customerData" ("firstName", "lastName", "email", "password", "phoneNumber", "address") VALUES ('UserFirstName', 'UserSecondName', 'user@gmail.com', 'password', '0000000000', 'Chennai');

-- Table for storing service request types
CREATE TABLE IF NOT EXISTS "serviceData" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "typeName" TEXT NOT NULL,
    "description" TEXT,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "lastUpdatedAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS "userAsks" (
    "reqId" INTEGER PRIMARY KEY AUTOINCREMENT,
    "id" INTEGER,
    "typeName" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "address" TEXT NOT NULL,
    "createdAt" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    "approval" TEXT
);

INSERT INTO "serviceData" ("typeName", "description") VALUES ('Gas Refill', 'Refill gas in your gas cylinder');
INSERT INTO "serviceData" ("typeName", "description") VALUES ('Gas Installation', 'Install gas in your home');

-- Table for storing service requests
CREATE TABLE IF NOT EXISTS "requestData" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "customerId" INTEGER NOT NULL,
    "serviceId" INTEGER NOT NULL,
    "requestDetails" TEXT NOT NULL,
    "requestStatus" TEXT DEFAULT 'Pending',
    "createdAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "resolvedAt" TIMESTAMP NULL,
    "repId" INTEGER NULL,
    FOREIGN KEY ("repId") REFERENCES "repData"("id"),
    FOREIGN KEY ("customerId") REFERENCES "customerData"("id"),
    FOREIGN KEY ("serviceId") REFERENCES "serviceData"("id")
);
"""

def reinitializeDatabase():
    try:
        db_connection = sqlite3.connect("./db/db.sqlite3")
        db_cursor = db_connection.cursor()
        db_cursor.executescript(init_script)
        db_connection.commit()
        db_connection.close()

        print("[MESSAGE]: Database reinitialized successfully.")
    except Exception as e:
        f = open("logs/init_db.log", "a")
        f.write(f"[ERROR] {datetime.now()}: {e}\n")
        f.close()
        print("[ERROR]: Error in reinitializing database.")
    finally:
        return