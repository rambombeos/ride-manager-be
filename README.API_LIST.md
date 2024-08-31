## API Documentation

### 1. User Management

#### 1.1 List Users
- **Endpoint**: `rides/identity/users/`
- **Method**: GET
- **Description**: Retrieve a list of users or a specific user
- **Headers**: Authorization: Token your_auth_token_here
- **Response**:
  ```json
  [
    {
      "id": 1,
      "username": "johndoe",
      "email": "johndoe@example.com",
      "first_name": "John",
      "last_name": "Doe"
    },
    {
      "id": 2,
      "username": "janedoe",
      "email": "janedoe@example.com",
      "first_name": "Jane",
      "last_name": "Doe"
    }
  ]
  ```

#### 1.2 Create User
- **Endpoint**: `rides/identity/users/`
- **Method**: POST
- **Description**: Create a new user
- **Headers**: Authorization: Token your_auth_token_here
- **Payload**:
  ```json
  {
    "username": "newuser",
    "email": "newuser@example.com",
    "first_name": "New",
    "last_name": "User",
    "password": "securepassword123"
  }
  ```
- **Response**: Returns the created user object (excluding password)

#### 1.3 Update User
- **Endpoint**: `rides/identity/users/{id}/`
- **Method**: PUT/PATCH
- **Description**: Update an existing user
- **Headers**: Authorization: Token your_auth_token_here
- **Payload**: Same as Create User (fields to update)
- **Response**: Returns the updated user object (excluding password)

#### 1.4 Delete User
- **Endpoint**: `rides/identity/users/{id}/`
- **Method**: DELETE
- **Description**: Remove a user
- **Headers**: Authorization: Token your_auth_token_here
- **Response**: 204 No Content

Note: The password field is write-only and will not be returned in GET requests.

### 2. Rides

#### 2.1 List Rides
- **Endpoint**: `/rides/api/rides/`
- **Method**: GET
- **Description**: Retrieve a list of all rides
- **Headers**: Authorization: Token your_auth_token_here
- **Response**:
  ```json
  [
    {
      "id_ride": 1,
      "status": "en-route",
      "id_rider": 2,
      "id_driver": 1,
      "pickup_latitude": 40.7128,
      "pickup_longitude": -74.0060,
      "dropoff_latitude": 42.3601,
      "dropoff_longitude": -71.0589,
      "pickup_time": "2023-05-20T10:00:00Z",
      "dropoff_time": null,
      "events": []
    },
    {
      "id_ride": 2,
      "status": "pickup",
      "id_rider": 3,
      "id_driver": 4,
      "pickup_latitude": 34.0522,
      "pickup_longitude": -118.2437,
      "dropoff_latitude": 37.7749,
      "dropoff_longitude": -122.4194,
      "pickup_time": "2023-05-21T08:30:00Z",
      "dropoff_time": null,
      "events": []
    }
  ]
  ```

#### 2.2 Create Ride
- **Endpoint**: `/rides/api/rides/`
- **Method**: POST
- **Description**: Create a new ride
- **Headers**: Authorization: Token your_auth_token_here
- **Payload**:
  ```json
  {
    "status": "en-route",
    "id_rider": 5,
    "id_driver": 6,
    "pickup_latitude": 41.8781,
    "pickup_longitude": -87.6298,
    "dropoff_latitude": 42.3314,
    "dropoff_longitude": -83.0458,
    "pickup_time": "2023-05-22T09:00:00Z"
  }
  ```
- **Response**:
  ```json
  {
    "id_ride": 3,
    "status": "en-route",
    "id_rider": 5,
    "id_driver": 6,
    "pickup_latitude": 41.8781,
    "pickup_longitude": -87.6298,
    "dropoff_latitude": 42.3314,
    "dropoff_longitude": -83.0458,
    "pickup_time": "2023-05-22T09:00:00Z",
    "dropoff_time": null,
    "events": []
  }
  ```

#### 2.3 Retrieve Ride
- **Endpoint**: `/rides/api/rides/{ride_id}/`
- **Method**: GET
- **Description**: Retrieve details of a specific ride
- **Headers**: Authorization: Token your_auth_token_here
- **Response**:
  ```json
  {
    "id_ride": 1,
    "status": "en-route",
    "id_rider": 2,
    "id_driver": 1,
    "pickup_latitude": 40.7128,
    "pickup_longitude": -74.0060,
    "dropoff_latitude": 42.3601,
    "dropoff_longitude": -71.0589,
    "pickup_time": "2023-05-20T10:00:00Z",
    "dropoff_time": null,
    "events": []
  }
  ```

#### 2.4 Update Ride
- **Endpoint**: `/rides/api/rides/{ride_id}/`
- **Method**: PUT
- **Description**: Update details of a specific ride
- **Headers**: Authorization: Token your_auth_token_here
- **Payload**:
  ```json
  {
    "status": "dropoff",
    "dropoff_time": "2023-05-20T11:00:00Z"
  }
  ```
- **Response**:
  ```json
  {
    "id_ride": 1,
    "status": "dropoff",
    "id_rider": 2,
    "id_driver": 1,
    "pickup_latitude": 40.7128,
    "pickup_longitude": -74.0060,
    "dropoff_latitude": 42.3601,
    "dropoff_longitude": -71.0589,
    "pickup_time": "2023-05-20T10:00:00Z",
    "dropoff_time": "2023-05-20T11:00:00Z",
    "events": []
  }
  ```

#### 2.5 Delete Ride
- **Endpoint**: `/rides/api/rides/{ride_id}/`
- **Method**: DELETE
- **Description**: Delete a specific ride
- **Headers**: Authorization: Token your_auth_token_here
- **Response**: 204 No Content

Note: Replace `your_auth_token_here` with the actual token received after login. All endpoints except login require authentication.
