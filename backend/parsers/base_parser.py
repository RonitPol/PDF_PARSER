# backend/parsers/base_parser.py
import pdfplumber
import re
from datetime import datetime
from abc import ABC, abstractmethod

class BaseCreditCardParser(ABC):
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = self._extract_text()
        
    def _extract_text(self):
        """Extract text from PDF"""
        text = ""
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text
    
    def _clean_amount(self, amount_str):
        """Clean and convert amount string to float"""
        if not amount_str:
            return 0.0
        # Remove currency symbols and commas
        cleaned = re.sub(r'[^\d.]', '', str(amount_str))
        try:
            return float(cleaned)
        except ValueError:
            return 0.0
    
    @abstractmethod
    def get_card_holder_name(self):
        pass
    
    @abstractmethod
    def get_card_number_last4(self):
        pass
    
    @abstractmethod
    def get_billing_period(self):
        pass
    
    @abstractmethod
    def get_payment_due_date(self):
        pass
    
    @abstractmethod
    def get_total_amount_due(self):
        pass
    
    def parse(self):
        """Main parsing method"""
        return {
            "card_holder_name": self.get_card_holder_name(),
            "card_number_last4": self.get_card_number_last4(),
            "billing_period": self.get_billing_period(),
            "payment_due_date": self.get_payment_due_date(),
            "total_amount_due": self.get_total_amount_due()
        }