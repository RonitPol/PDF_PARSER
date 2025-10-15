// frontend/src/components/FileUpload.jsx
import React, { useRef, useState } from 'react';

const FileUpload = ({ onFileUpload, loading }) => {
  const fileInputRef = useRef(null);
  const [isDragOver, setIsDragOver] = useState(false);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      validateAndUpload(file);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    setIsDragOver(false);
    
    const file = event.dataTransfer.files[0];
    if (file) {
      validateAndUpload(file);
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
    setIsDragOver(true);
  };

  const handleDragLeave = (event) => {
    event.preventDefault();
    setIsDragOver(false);
  };

  const validateAndUpload = (file) => {
    if (file.type !== 'application/pdf') {
      alert('Please select a PDF file');
      return;
    }

    if (file.size > 16 * 1024 * 1024) { // 16MB
      alert('File size must be less than 16MB');
      return;
    }

    onFileUpload(file);
  };

  return (
    <div className="file-upload-container">
      <div
        className={`drop-zone ${isDragOver ? 'drag-over' : ''} ${loading ? 'loading' : ''}`}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onClick={() => !loading && fileInputRef.current?.click()}
      >
        {loading ? (
          <div className="loading-content">
            <div className="spinner"></div>
            <p>Processing your statement...</p>
          </div>
        ) : (
          <>
            <div className="upload-icon">📄</div>
            <h3>Upload Credit Card Statement</h3>
            <p>Drag & drop your PDF statement here or click to browse</p>
            <p className="file-requirements">Supports: PDF files only (Max 16MB)</p>
          </>
        )}
      </div>
      
      <input
        type="file"
        ref={fileInputRef}
        onChange={handleFileSelect}
        accept=".pdf"
        style={{ display: 'none' }}
        disabled={loading}
      />
    </div>
  );
};

export default FileUpload;