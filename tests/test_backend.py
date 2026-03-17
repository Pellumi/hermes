from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.backend_services.main import app
from src.backend_services.database import Base, get_db
import pytest

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_user():
    response = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    return data["access_token"]

def test_create_mission():
    token = test_login_user()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post(
        "/missions/",
        json={"title": "Test Mission", "description": "A test mission"},
        headers=headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Mission"
    assert data["status"] == "PENDING"

def test_read_missions():
    token = test_login_user()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/missions/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

if __name__ == "__main__":
    # Manually run tests if pytest is not available
    try:
        test_register_user()
        print("test_register_user PASSED")
        test_create_mission()
        print("test_create_mission PASSED")
        test_read_missions()
        print("test_read_missions PASSED")
    except Exception as e:
        print(f"TEST FAILED: {e}")
