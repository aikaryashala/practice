#!/bin/bash

# Simple test script for the Student Management API
# Run this after starting the server with: python app.py

echo "======================================="
echo "Testing Student Management API"
echo "======================================="
echo ""

BASE_URL="http://localhost:5000"

echo "1. Testing GET /api/students (Get all students)"
echo "Command: curl $BASE_URL/api/students"
curl -s $BASE_URL/api/students | python -m json.tool
echo ""
echo "-----------------------------------"
echo ""

echo "2. Testing GET /api/students?grade=A (Filter by grade)"
echo "Command: curl '$BASE_URL/api/students?grade=A'"
curl -s "$BASE_URL/api/students?grade=A" | python -m json.tool
echo ""
echo "-----------------------------------"
echo ""

echo "3. Testing GET /api/students/1 (Get student by ID)"
echo "Command: curl $BASE_URL/api/students/1"
curl -s $BASE_URL/api/students/1 | python -m json.tool
echo ""
echo "-----------------------------------"
echo ""

echo "4. Testing POST /api/students (Add new student)"
echo "Command: curl -X POST -H 'Content-Type: application/json' -d '{...}' $BASE_URL/api/students"
curl -s -X POST $BASE_URL/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Ganesh Iyer","age":23,"grade":"B","email":"ganesh@example.com"}' | python -m json.tool
echo ""
echo "-----------------------------------"
echo ""

echo "5. Testing GET /api/students (Verify new student added)"
echo "Command: curl $BASE_URL/api/students"
curl -s $BASE_URL/api/students | python -m json.tool
echo ""
echo "-----------------------------------"
echo ""

echo "6. Testing GET / (Home page - showing first 30 lines)"
echo "Command: curl $BASE_URL/ | head -30"
curl -s $BASE_URL/ | head -30
echo ""
echo "-----------------------------------"
echo ""

echo "7. Testing Error Case - Missing field"
echo "Command: curl -X POST -H 'Content-Type: application/json' -d '{\"name\":\"Incomplete\"}' $BASE_URL/api/students"
curl -s -X POST $BASE_URL/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Incomplete"}' | python -m json.tool
echo ""
echo "-----------------------------------"
echo ""

echo "8. Testing Error Case - Invalid student ID"
echo "Command: curl $BASE_URL/api/students/999"
curl -s $BASE_URL/api/students/999 | python -m json.tool
echo ""
echo "-----------------------------------"
echo ""

echo "======================================="
echo "All tests completed!"
echo "======================================="
