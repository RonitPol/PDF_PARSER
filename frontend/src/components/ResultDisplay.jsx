// frontend/src/components/ResultDisplay.jsx
import React from 'react';

const ResultDisplay = ({ data, onReset }) => {
  const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-IN', {
      style: 'currency',
      currency: 'INR'
    }).format(amount);
  };

  const formatDate = (dateStr) => {
    if (!dateStr || dateStr === 'Not Found') return dateStr;
    return dateStr;
  };

  const getBankColor = (bankName) => {
    const colors = {
      'HDFC': '#004C8F',
      'ICICI': '#FF6B00',
      'SBI': '#1E88E5',
      'Axis': '#951C76',
      'Citi': '#0065A3'
    };
    return colors[bankName] || '#666';
  };

  return (
    <div className="result-container">
      <div className="result-header">
        <h2>📊 Statement Analysis Complete</h2>
        <button onClick={onReset} className="reset-btn">
          Upload Another
        </button>
      </div>
      
      <div className="detected-bank-banner" style={{ backgroundColor: getBankColor(data.detected_bank) }}>
        <span>Detected Bank: {data.detected_bank}</span>
      </div>

      <div className="result-grid">
        <div className="result-card">
          <div className="result-icon">👤</div>
          <div className="result-content">
            <div className="result-label">Card Holder Name</div>
            <div className="result-value">{data.card_holder_name}</div>
          </div>
        </div>

        <div className="result-card">
          <div className="result-icon">💳</div>
          <div className="result-content">
            <div className="result-label">Card Number</div>
            <div className="result-value">**** **** **** {data.card_number_last4}</div>
          </div>
        </div>

        <div className="result-card">
          <div className="result-icon">📅</div>
          <div className="result-content">
            <div className="result-label">Billing Period</div>
            <div className="result-value">{formatDate(data.billing_period)}</div>
          </div>
        </div>

        <div className="result-card">
          <div className="result-icon">⏰</div>
          <div className="result-content">
            <div className="result-label">Payment Due Date</div>
            <div className="result-value due-date">{formatDate(data.payment_due_date)}</div>
          </div>
        </div>

        <div className="result-card highlight">
          <div className="result-icon">💰</div>
          <div className="result-content">
            <div className="result-label">Total Amount Due</div>
            <div className="result-value amount">{formatCurrency(data.total_amount_due)}</div>
          </div>
        </div>
      </div>

      <div className="result-footer">
        <p>✅ Successfully extracted 5 key data points from your statement</p>
      </div>
    </div>
  );
};

export default ResultDisplay;