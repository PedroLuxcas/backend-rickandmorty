from flask import jsonify

class ApiResponse:
    """Class to standardize all API responses"""
    
    @staticmethod
    def success(data=None, message="Operation successful", status_code=200):
        """Standardized success response"""
        response = {
            'success': True,
            'message': message,
            'data': data
        }
        return jsonify(response), status_code
    
    @staticmethod
    def error(message="An error occurred", status_code=400, data=None):
        """Standardized error response"""
        response = {
            'success': False,
            'message': message,
            'data': data
        }
        return jsonify(response), status_code
    
    @staticmethod
    def not_found(resource="Resource"):
        """Standardized response for resource not found"""
        return ApiResponse.error(
            message=f"{resource} not found",
            status_code=404
        )
    
    @staticmethod
    def validation_error(errors):
        """Standardized response for validation errors"""
        return ApiResponse.error(
            message="Validation error",
            status_code=422,
            data=errors
        )