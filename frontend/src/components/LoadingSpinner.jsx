// frontend/src/components/LoadingSpinner.jsx
import React from 'react';

const LoadingSpinner = ({ message = "Processing your statement..." }) => {
  return (
    <div className="loading-spinner">
      <div className="spinner"></div>
      <p>{message}</p>
    </div>
  );
};

export default LoadingSpinner;