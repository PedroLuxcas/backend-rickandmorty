"""
Custom exceptions for the application.
All exceptions inherit from APIException and are handled by error handlers.
"""

class APIException(Exception):
    """Base exception for all API errors"""
    
    def __init__(self, message="An error occurred", status_code=400, data=None):
        self.message = message
        self.status_code = status_code
        self.data = data
        super().__init__(self.message)


class NotFoundError(APIException):
    """Resource not found exception"""
    
    def __init__(self, resource="Resource", identifier=None, message=None):
        if message:
            error_message = message
        elif identifier:
            error_message = f"{resource} not found with identifier: {identifier}"
        else:
            error_message = f"{resource} not found"
        
        super().__init__(message=error_message, status_code=404)


class ValidationError(APIException):
    """Validation error exception"""
    
    def __init__(self, message="Validation error", errors=None):
        super().__init__(message=message, status_code=422, data=errors)


class DatabaseError(APIException):
    """Database operation error"""
    
    def __init__(self, message="Database operation failed", detail=None):
        data = {"detail": detail} if detail else None
        super().__init__(message=message, status_code=500, data=data)


class AuthenticationError(APIException):
    """Authentication error"""
    
    def __init__(self, message="Authentication required"):
        super().__init__(message=message, status_code=401)


class PermissionError(APIException):
    """Permission denied error"""
    
    def __init__(self, message="Permission denied"):
        super().__init__(message=message, status_code=403)


class BusinessLogicError(APIException):
    """Business logic violation error"""
    
    def __init__(self, message="Business rule violated", data=None):
        super().__init__(message=message, status_code=400, data=data)


class ConflictError(APIException):
    """Resource conflict error (e.g., duplicate entry)"""
    
    def __init__(self, message="Resource already exists", data=None):
        super().__init__(message=message, status_code=409, data=data)


class ServiceUnavailableError(APIException):
    """External service unavailable error"""
    
    def __init__(self, message="Service temporarily unavailable", data=None):
        super().__init__(message=message, status_code=503, data=data)


class BadRequestError(APIException):
    """Bad request error"""
    
    def __init__(self, message="Bad request", data=None):
        super().__init__(message=message, status_code=400, data=data)


class RateLimitError(APIException):
    """Rate limit exceeded error"""
    
    def __init__(self, message="Rate limit exceeded", retry_after=None):
        data = {"retry_after": retry_after} if retry_after else None
        super().__init__(message=message, status_code=429, data=data)