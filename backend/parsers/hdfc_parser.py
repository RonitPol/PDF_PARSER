# backend/parsers/hdfc_parser.py
from .base_parser import BaseCreditCardParser
import re
from datetime import datetime

class HDFCParser(BaseCreditCardParser):
    def get_card_holder_name(self):
        # Look for name patterns in HDFC statements
        patterns = [
            r'Dear\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',
            r'Customer\s+Name:\s*([A-Z][a-z]+\s+[A-Z][a-z]+)',
            r'Statement\s+for\s+([A-Z][a-z]+\s+[A-Z][a-z]+)'
        ]
        for pattern in patterns:
            match = re.search(pattern, self.text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        return "Not Found"
    
    def get_card_number_last4(self):
        # HDFC card number patterns
        patterns = [
            r'Card\s+No\.?\s*:\s*\*+\s*(\d{4})',
            r'Card\s+Number\s*:\s*\*+\s*(\d{4})',
            r'Card\s+ending\s+with\s+(\d{4})'
        ]
        for pattern in patterns:
            match = re.search(pattern, self.text)
            if match:
                return match.group(1)
        return "Not Found"
    
    def get_billing_period(self):
        # Billing period patterns
        patterns = [
            r'Statement\s+Period\s*:\s*(\d{2}-\d{2}-\d{4})\s*to\s*(\d{2}-\d{2}-\d{4})',
            r'Billing\s+Period\s*:\s*(\d{2}/\d{2}/\d{4})\s*-\s*(\d{2}/\d{2}/\d{4})',
            r'Period\s*:\s*(\d{2}-\w{3}-\d{4})\s*to\s*(\d{2}-\w{3}-\d{4})'
        ]
        for pattern in patterns:
            match = re.search(pattern, self.text, re.IGNORECASE)
            if match:
                return f"{match.group(1)} to {match.group(2)}"
        return "Not Found"
    
    def get_payment_due_date(self):
        # Payment due date patterns
        patterns = [
            r'Payment\s+Due\s+Date\s*:\s*(\d{2}-\d{2}-\d{4})',
            r'Due\s+Date\s*:\s*(\d{2}/\d{2}/\d{4})',
            r'Pay\s+by\s+(\d{2}-\w{3}-\d{4})'
        ]
        for pattern in patterns:
            match = re.search(pattern, self.text, re.IGNORECASE)
            if match:
                return match.group(1)
        return "Not Found"
    
    def get_total_amount_due(self):
        # Total amount due patterns
        patterns = [
            r'Total\s+Amount\s+Due\s*[:\-]?\s*[₹Rs\.]*\s*([\d,]+\.?\d*)',
            r'Amount\s+Due\s*[:\-]?\s*[₹Rs\.]*\s*([\d,]+\.?\d*)',
            r'Total\s+Due\s*[:\-]?\s*[₹Rs\.]*\s*([\d,]+\.?\d*)'
        ]
        for pattern in patterns:
            match = re.search(pattern, self.text, re.IGNORECASE)
            if match:
                return self._clean_amount(match.group(1))
        return 0.0