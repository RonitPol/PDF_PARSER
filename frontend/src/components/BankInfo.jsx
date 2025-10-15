// frontend/src/components/BankInfo.jsx
import React from 'react';

const BankInfo = () => {
  const supportedBanks = [
    { 
      name: 'HDFC Bank', 
      code: 'hdfc', 
      color: '#004C8F',
      features: ['Regalia', 'Infinia', 'MoneyBack']
    },
    { 
      name: 'ICICI Bank', 
      code: 'icici', 
      color: '#FF6B00',
      features: ['Sapphiro', 'Rubyx', 'Coral']
    },
    { 
      name: 'SBI Card', 
      code: 'sbi', 
      color: '#1E88E5',
      features: ['Elite', 'Prime', 'SimplyCLICK']
    },
    { 
      name: 'Axis Bank', 
      code: 'axis', 
      color: '#951C76',
      features: ['Magnus', 'Select', 'Flipkart']
    },
    { 
      name: 'Citibank', 
      code: 'citi', 
      color: '#0065A3',
      features: ['PremierMiles', 'Rewards', 'Cashback']
    }
  ];

  return (
    <div className="bank-info">
      <h3>🏦 Supported Banks</h3>
      <p className="bank-subtitle">We automatically detect and parse statements from these banks:</p>
      
      <div className="bank-grid">
        {supportedBanks.map((bank, index) => (
          <div 
            key={index} 
            className="bank-card"
            style={{ borderLeftColor: bank.color }}
          >
            <div className="bank-header">
              <h4 style={{ color: bank.color }}>{bank.name}</h4>
            </div>
            <div className="bank-features">
              {bank.features.map((feature, idx) => (
                <span key={idx} className="feature-tag">{feature}</span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BankInfo;