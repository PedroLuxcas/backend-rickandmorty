"""
Global error handlers for the Flask application.
Registers handlers for custom exceptions and common HTTP errors.
"""

from flask import jsonify
from .api_response import ApiResponse
from .exceptions import (
    APIException, NotFoundError, ValidationError, DatabaseError,
    AuthenticationError, PermissionError, BusinessLogicError,
    ConflictError, ServiceUnavailableError, BadRequestError, RateLimitError
)
from sqlalchemy.exc import SQLAlchemyError
import traceback
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def register_error_handlers(app):
    """Register all error handlers with the Flask app"""
    
    @app.errorhandler(APIException)
    def handle_api_exception(error):
        """Handle custom API exceptions"""
        logger.warning(f"API Exception: {error.message} (Status: {error.status_code})")
        return ApiResponse.error(
            message=error.message,
            status_code=error.status_code,
            data=error.data
        )
    
    @app.errorhandler(NotFoundError)
    def handle_not_found(error):
        """Handle not found errors"""
        return ApiResponse.not_found(error.message)
    
    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        """Handle validation errors"""
        return ApiResponse.validation_error(error.data)
    
    @app.errorhandler(DatabaseError)
    def handle_database_error(error):
        """Handle database errors"""
        logger.error(f"Database Error: {error.message}")
        if error.data and error.data.get('detail'):
            logger.error(f"Detail: {error.data['detail']}")
        
        return ApiResponse.error(
            message=error.message,
            status_code=error.status_code,
            data=error.data if app.debug else None
        )
    
    @app.errorhandler(AuthenticationError)
    def handle_authentication_error(error):
        """Handle authentication errors"""
        return ApiResponse.error(
            message=error.message,
            status_code=401
        )
    
    @app.errorhandler(PermissionError)
    def handle_permission_error(error):
        """Handle permission errors"""
        return ApiResponse.error(
            message=error.message,
            status_code=403
        )
    
    @app.errorhandler(BusinessLogicError)
    def handle_business_logic_error(error):
        """Handle business logic errors"""
        return ApiResponse.error(
            message=error.message,
            status_code=400,
            data=error.data
        )
    
    @app.errorhandler(ConflictError)
    def handle_conflict_error(error):
        """Handle conflict errors"""
        return ApiResponse.error(
            message=error.message,
            status_code=409,
            data=error.data
        )
    
    @app.errorhandler(ServiceUnavailableError)
    def handle_service_unavailable(error):
        """Handle service unavailable errors"""
        return ApiResponse.error(
            message=error.message,
            status_code=503,
            data=error.data
        )
    
    @app.errorhandler(BadRequestError)
    def handle_bad_request(error):
        """Handle bad request errors"""
        return ApiResponse.error(
            message=error.message,
            status_code=400,
            data=error.data
        )
    
    @app.errorhandler(RateLimitError)
    def handle_rate_limit(error):
        """Handle rate limit errors"""
        response = ApiResponse.error(
            message=error.message,
            status_code=429,
            data=error.data
        )
        if error.data and error.data.get('retry_after'):
            response[0].headers['Retry-After'] = str(error.data['retry_after'])
        return response
    
    @app.errorhandler(404)
    def handle_404(error):
        """Handle Flask 404 errors"""
        return ApiResponse.error(
            message="Resource not found",
            status_code=404
        )
    
    @app.errorhandler(405)
    def handle_405(error):
        """Handle method not allowed errors"""
        return ApiResponse.error(
            message="Method not allowed",
            status_code=405
        )
    
    @app.errorhandler(500)
    def handle_500(error):
        """Handle internal server errors"""
        logger.error(f"Internal Server Error: {str(error)}")
        logger.error(traceback.format_exc())
        
        if app.debug:
            # In development, show the actual error
            return ApiResponse.error(
                message=f"Internal server error: {str(error)}",
                status_code=500,
                data={"traceback": traceback.format_exc().split('\n')}
            )
        else:
            # In production, hide details
            return ApiResponse.error(
                message="Internal server error",
                status_code=500
            )
    
    @app.errorhandler(SQLAlchemyError)
    def handle_sqlalchemy_error(error):
        """Handle SQLAlchemy database errors"""
        logger.error(f"SQLAlchemy Error: {str(error)}")
        logger.error(traceback.format_exc())
        
        return ApiResponse.error(
            message="Database operation failed",
            status_code=500,
            data={"detail": str(error)} if app.debug else None
        )
    
    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        """Handle any unhandled exception"""
        logger.error(f"Unhandled Exception: {str(error)}")
        logger.error(traceback.format_exc())
        
        return ApiResponse.error(
            message="An unexpected error occurred",
            status_code=500,
            data={"detail": str(error)} if app.debug else None
        )
    
    return app