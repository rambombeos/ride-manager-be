## API Documentation

## 1. Superuser Management

#### 1.1 Obtain Token
- **Endpoint**: `/rides/identity/superuser/token/`
- **Method**: POST
- **Description**: Obtain a token for superuser authentication
- **Payload**:
  ```json
  {
    "username": "superuser",
    "password": "superuser_password"
  }
  ```
- **Response**:
  ```json
  {
    "token": "your_superuser_token_here"
  }
  ```

## 2. User Management

#### 2.1 List Users
- **Endpoint**: `rides/identity/users/`
- **Method**: GET
- **Description**: Retrieve a list of users or a specific user
- **Headers**: Authorization: Token your_auth_token_here
- **Response**:
  ```json
  [
    {
      "id_user": 1,
      "role": "rider",
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@example.com",
      "phone_number": "+1234567890"
    },
    {
      "id_user": 2,
      "role": "driver",
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "janedoe@example.com",
      "phone_number": "+0987654321"
    }
  ]
  ```

#### 2.2 Create User
- **Endpoint**: `rides/identity/users/`
- **Method**: POST
- **Description**: Create a new user
- **Headers**: Authorization: Token your_auth_token_here
- **Payload**:
  ```json
  {
    "role": "rider",
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "phone_number": "+1234567890"
  }
  ```
- **Response**: Returns the created user object

#### 2.3 Update User
- **Endpoint**: `rides/identity/users/{id_user}/`
- **Method**: PUT/PATCH
- **Description**: Update an existing user
- **Headers**: Authorization: Token your_auth_token_here
- **Payload**: Same as Create User (fields to update)
- **Response**: Returns the updated user object

#### 2.4 Delete User
- **Endpoint**: `rides/identity/users/{id_user}/`
- **Method**: DELETE
- **Description**: Remove a user
- **Headers**: Authorization: Token your_auth_token_here
- **Response**: 204 No Content

## 3. Rides

#### 3.1 List Rides
- **Endpoint**: `/rides/api/rides/`
- **Method**: GET
- **Description**: Retrieve a list of all rides
- **Headers**: Authorization: Token your_auth_token_here
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `page_size`: Number of items per page (default: 10, max: 100)
  - `status`: Filter rides by status
  - `rider_email`: Filter rides by rider's email
  - `latitude`: Latitude for distance calculation
  - `longitude`: Longitude for distance calculation
  - `ordering`: Order results by specified field (e.g., 'pickup_time', 'distance')
- **Response**:
  ```json
  {
    "success": true,
    "message": "Rides retrieved successfully",
    "data": {
      "count": 100,
      "next": "http://example.com/rides/api/rides/?page=2",
      "previous": null,
      "results": [
        {
          "id_ride": 1,
          "status": "en-route",
          "id_rider": {
            "id_user": 2,
            "role": "rider",
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "phone_number": "+1234567890"
          },
          "id_driver": {
            "id_user": 1,
            "role": "driver",
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "janedoe@example.com",
            "phone_number": "+0987654321"
          },
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
          "id_rider": {
            "id_user": 3,
            "role": "rider",
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alicesmith@example.com",
            "phone_number": "+1122334455"
          },
          "id_driver": {
            "id_user": 4,
            "role": "driver",
            "first_name": "Bob",
            "last_name": "Johnson",
            "email": "bobjohnson@example.com",
            "phone_number": "+5544332211"
          },
          "pickup_latitude": 34.0522,
          "pickup_longitude": -118.2437,
          "dropoff_latitude": 37.7749,
          "dropoff_longitude": -122.4194,
          "pickup_time": "2023-05-21T08:30:00Z",
          "dropoff_time": null,
          "events": []
        }
      ]
    }
  }
  ```

#### 3.2 Create Ride
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
    "success": true,
    "message": "Ride created successfully",
    "data": {
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
  }
  ```

#### 3.3 Retrieve Ride
- **Endpoint**: `/rides/api/rides/{ride_id}/`
- **Method**: GET
- **Description**: Retrieve details of a specific ride
- **Headers**: Authorization: Token your_auth_token_here
- **Response**:
  ```json
  {
    "id_ride": 1,
    "status": "en-route",
    "id_rider": {
      "id_user": 2,
      "role": "rider",
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@example.com",
      "phone_number": "+1234567890"
    },
    "id_driver": {
      "id_user": 1,
      "role": "driver",
      "first_name": "Jane",
      "last_name": "Doe",
      "email": "janedoe@example.com",
      "phone_number": "+0987654321"
    },
    "pickup_latitude": 40.7128,
    "pickup_longitude": -74.0060,
    "dropoff_latitude": 42.3601,
    "dropoff_longitude": -71.0589,
    "pickup_time": "2023-05-20T10:00:00Z",
    "dropoff_time": null,
    "events": []
  }
  ```

#### 3.4 Update Ride
- **Endpoint**: `/rides/api/rides/{ride_id}/`
- **Method**: PUT/PATCH
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
    "success": true,
    "message": "Ride updated successfully",
    "data": {
      "id_ride": 1,
      "status": "dropoff",
      "id_rider": {
        "id_user": 2,
        "role": "rider",
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "phone_number": "+1234567890"
      },
      "id_driver": {
        "id_user": 1,
        "role": "driver",
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "janedoe@example.com",
        "phone_number": "+0987654321"
      },
      "pickup_latitude": 40.7128,
      "pickup_longitude": -74.0060,
      "dropoff_latitude": 42.3601,
      "dropoff_longitude": -71.0589,
      "pickup_time": "2023-05-20T10:00:00Z",
      "dropoff_time": "2023-05-20T11:00:00Z",
      "events": [
        {
          "id_ride_event": 1,
          "description": "Status changed to dropoff",
          "timestamp": "2023-05-20T11:00:00Z"
        }
      ]
    }
  }
  ```

#### 3.5 Delete Ride
- **Endpoint**: `/rides/api/rides/{ride_id}/`
- **Method**: DELETE
- **Description**: Delete a specific ride
- **Headers**: Authorization: Token your_auth_token_here
- **Response**:
  ```json
  {
    "success": true,
    "message": "Ride deleted successfully"
  }
  ```

Note: Replace `your_auth_token_here` with the actual token received after login. All endpoints require authentication using the IsAuthenticated permission class.
