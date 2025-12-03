# Fixed has_converged function for resolved-rate motion control
# Copy this function into your Robot class in the notebook

def has_converged(self, errors_history, threshold=0.001, window=10):
    """
    FIXED: Check if absolute positioning error is below threshold
    Previous version only checked error CHANGE, not absolute error!
    
    Args:
        errors_history: List of positioning errors
        threshold: Maximum acceptable error (m)
        window: Number of recent steps to check
    
    Returns:
        bool: True if converged, False otherwise
    """
    if len(errors_history) < window:
        return False
    
    # Get current absolute error
    current_error = errors_history[-1]
    
    # Check if error has stabilized (not oscillating)
    recent_errors = errors_history[-window:]
    error_stability = np.std(recent_errors)
    
    # Both conditions must be met:
    # 1. Current error is below threshold
    # 2. Error is stable (not oscillating wildly)
    return (current_error < threshold) and (error_stability < threshold * 0.5)


# Also update control parameters in Robot.__init__:
# self.gain = 2.0  # Increased from 1.5 for faster convergence
# self.dumping_factor = 0.05  # Decreased from 0.15 for better precision
