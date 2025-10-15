// frontend/src/App.jsx
import React, { useState, useEffect } from 'react';
import FileUpload from '../../frontend/src/components/FileUpload';
import ResultDisplay from '../../frontend/src/components/ResultDisplay';
import BankInfo from '../../frontend/src/components/BankInfo';
import { uploadStatement, healthCheck } from '../../frontend/src/services/api';
import './App.css';

function App() {
  const [parsedData, setParsedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [apiStatus, setApiStatus] = useState('checking');

  useEffect(() => {
    checkApiHealth();
  }, []);

  const checkApiHealth = async () => {
    try {
      await healthCheck();
      setApiStatus('healthy');
    } catch (err) {
      setApiStatus('unhealthy');
      setError('Backend server is not running. Please start the Flask server on port 5000.');
    }
  };

  const handleFileUpload = async (file) => {
    setLoading(true);
    setError('');
    setParsedData(null);

    try {
      const data = await uploadStatement(file);
      setParsedData(data);
    } catch (err) {
      setError(err.response?.data?.error || err.message || 'Upload failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setParsedData(null);
    setError('');
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1>💳 Credit Card Statement Parser</h1>
          <p>Extract key information from your credit card statements automatically</p>
        
        </div>
      </header>

      <main className="app-main">
        <div className="container">
          <BankInfo />
          
          {!parsedData && (
            <FileUpload 
              onFileUpload={handleFileUpload}
              loading={loading}
            />
          )}

          {error && (
            <div className="error-message">
              <div className="error-icon">⚠️</div>
              <div className="error-content">
                <h4>Error</h4>
                <p>{error}</p>
                <button onClick={handleReset} className="retry-btn">
                  Try Again
                </button>
              </div>
            </div>
          )}

          {parsedData && (
            <ResultDisplay 
              data={parsedData} 
              onReset={handleReset}
            />
          )}
        </div>
      </main>

      <footer className="app-footer">
        <div className="footer-content">
          <p>Supports HDFC, ICICI, SBI, Axis, and Citibank credit card statements</p>
          <p className="footer-note">
            💡 Tip: Upload clear PDF statements for best results. All processing happens locally.
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;