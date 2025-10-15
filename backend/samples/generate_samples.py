# backend/samples/generate_samples.py
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
import os
from datetime import datetime, timedelta
import random

def create_hdfc_sample():
    filename = "backend/samples/hdfc_sample.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Header
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#004C8F'),
        alignment=1,
        spaceAfter=30
    )
    
    story.append(Paragraph("HDFC BANK CREDIT CARD STATEMENT", header_style))
    
    # Customer Info
    customer_data = [
        ['Card Member Name:', 'RAJESH KUMAR', 'Statement Date:', '25-Nov-2024'],
        ['Card Number:', 'XXXX XXXX XXXX 5678', 'Customer ID:', 'HDFC78901234'],
        ['Credit Limit:', '₹2,50,000.00', 'Available Limit:', '₹1,87,432.00']
    ]
    
    customer_table = Table(customer_data, colWidths=[2*inch, 2.5*inch, 1.5*inch, 2*inch])
    customer_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#004C8F')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F0F8FF')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(customer_table)
    story.append(Spacer(1, 20))
    
    # Billing Summary
    story.append(Paragraph("BILLING SUMMARY", styles['Heading2']))
    summary_data = [
        ['Description', 'Amount (₹)'],
        ['Previous Balance', '45,678.00'],
        ['Payments/Credits', '-25,000.00'],
        ['Purchases/Debits', '18,754.00'],
        ['Total Amount Due', '39,432.00'],
        ['Minimum Amount Due', '2,000.00']
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#004C8F')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 1), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#FFFACD')),
        ('FONTNAME', (0, 4), (-1, 4), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Transaction Details
    story.append(Paragraph("TRANSACTION DETAILS", styles['Heading2']))
    transaction_data = [
        ['Date', 'Description', 'Amount (₹)'],
        ['15-Nov-2024', 'AMAZON RETAIL INDIA', '8,456.00'],
        ['18-Nov-2024', 'SWIGGY BANGALORE', '1,234.00'],
        ['20-Nov-2024', 'PETROL PUMP DELHI', '2,500.00'],
        ['22-Nov-2024', 'FLIPKART INTERNET', '4,321.00'],
        ['24-Nov-2024', 'BIG BASKET GROCERIES', '2,243.00']
    ]
    
    transaction_table = Table(transaction_data, colWidths=[1.5*inch, 3*inch, 1.5*inch])
    transaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#004C8F')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(transaction_table)
    story.append(Spacer(1, 20))
    
    # Important Dates
    story.append(Paragraph("IMPORTANT DATES", styles['Heading2']))
    dates_data = [
        ['Statement Period:', '01-Nov-2024 to 30-Nov-2024'],
        ['Payment Due Date:', '15-Dec-2024'],
        ['Late Payment Fee:', '₹500 + GST']
    ]
    
    dates_table = Table(dates_data, colWidths=[2*inch, 3*inch])
    dates_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B6B')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(dates_table)
    
    # Footer note
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.grey,
        alignment=1
    )
    story.append(Spacer(1, 20))
    story.append(Paragraph("This is a sample HDFC Bank credit card statement for testing purposes only", footer_style))
    
    doc.build(story)
    print(f"Created HDFC sample: {filename}")

def create_icici_sample():
    filename = "backend/samples/icici_sample.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Header with orange theme
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#FF6B00'),
        alignment=1,
        spaceAfter=30
    )
    
    story.append(Paragraph("ICICI BANK CREDIT CARD STATEMENT", header_style))
    
    # Customer Info
    customer_data = [
        ['Dear RAJESH KUMAR,', '', 'Statement Date: 25-Nov-2024', ''],
        ['Card No: XXXX-XXXX-XXXX-4321', 'Credit Limit: ₹3,00,000', 'Due Date: 15-Dec-2024', '']
    ]
    
    customer_table = Table(customer_data, colWidths=[2.5*inch, 2*inch, 2*inch, 1*inch])
    customer_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B00')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('SPAN', (0, 0), (1, 0)),
        ('SPAN', (2, 0), (3, 0)),
    ]))
    story.append(customer_table)
    story.append(Spacer(1, 20))
    
    # Amount Summary
    story.append(Paragraph("AMOUNT SUMMARY", styles['Heading2']))
    summary_data = [
        ['Total Amount Due', '₹38,765.00'],
        ['Minimum Amount Due', '₹3,876.00'],
        ['Reward Points Balance', '12,345 Pts']
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B00')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Transaction Details
    story.append(Paragraph("TRANSACTION DETAILS", styles['Heading2']))
    transaction_data = [
        ['Date', 'Transaction Description', 'Amount (₹)'],
        ['14-Nov-2024', 'MYNTRA FASHION ONLINE', '5,678.00'],
        ['16-Nov-2024', 'ZOMATO FOOD DELIVERY', '1,890.00'],
        ['19-Nov-2024', 'BOOKMYSHOW TICKETS', '2,345.00'],
        ['21-Nov-2024', 'APPLE STORE ONLINE', '12,500.00'],
        ['23-Nov-2024', 'UBER RIDES BANGALORE', '856.00']
    ]
    
    transaction_table = Table(transaction_data, colWidths=[1.5*inch, 3*inch, 1.5*inch])
    transaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF6B00')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(transaction_table)
    story.append(Spacer(1, 20))
    
    # Billing Information
    story.append(Paragraph("BILLING INFORMATION", styles['Heading2']))
    billing_data = [
        ['Bill Period:', '01-Nov-2024 to 30-Nov-2024'],
        ['Payment Due Date:', '15-Dec-2024'],
        ['Late Payment Charges:', '₹600 + applicable taxes']
    ]
    
    billing_table = Table(billing_data, colWidths=[2*inch, 3*inch])
    billing_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FFA500')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(billing_table)
    
    doc.build(story)
    print(f"Created ICICI sample: {filename}")

def create_sbi_sample():
    filename = "backend/samples/sbi_sample.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Header with blue theme
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1E88E5'),
        alignment=1,
        spaceAfter=30
    )
    
    story.append(Paragraph("SBI CARD CREDIT CARD STATEMENT", header_style))
    
    # Customer Information
    info_data = [
        ['Customer Name: RAJESH KUMAR', 'Card No: XXXX XXXX XXXX 1234'],
        ['Statement Date: 25-Nov-2024', 'Credit Limit: ₹2,00,000'],
        ['Customer ID: SBI789456123', 'Due Date: 15-Dec-2024']
    ]
    
    info_table = Table(info_data, colWidths=[3*inch, 3*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E88E5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(info_table)
    story.append(Spacer(1, 20))
    
    # Statement Summary
    story.append(Paragraph("STATEMENT SUMMARY", styles['Heading2']))
    summary_data = [
        ['Opening Balance', '₹42,150.00'],
        ['Total Purchases', '₹21,845.00'],
        ['Payments Received', '₹-25,000.00'],
        ['Total Amount Due', '₹38,995.00'],
        ['Minimum Amount Due', '₹3,899.00']
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E88E5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#FFEB3B')),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#FF9800')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Transaction Details
    story.append(Paragraph("TRANSACTION DETAILS", styles['Heading2']))
    transaction_data = [
        ['Date', 'Description', 'Amount (₹)'],
        ['13-Nov-2024', 'AMAZON ONLINE RETAIL', '7,890.00'],
        ['17-Nov-2024', 'BIG BASKET GROCERIES', '3,456.00'],
        ['20-Nov-2024', 'INOX MOVIE TICKETS', '1,234.00'],
        ['22-Nov-2024', 'APPLE MUSIC SUBSCRIPTION', '99.00'],
        ['24-Nov-2024', 'DECATHLON SPORTS', '6,166.00']
    ]
    
    transaction_table = Table(transaction_data, colWidths=[1.5*inch, 3*inch, 1.5*inch])
    transaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E88E5')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(transaction_table)
    story.append(Spacer(1, 20))
    
    # Payment Information
    story.append(Paragraph("PAYMENT INFORMATION", styles['Heading2']))
    payment_data = [
        ['Statement Period:', '01-Nov-2024 to 30-Nov-2024'],
        ['Payment Due Date:', '15-Dec-2024'],
        ['Late Payment Charges:', '₹450 + GST']
    ]
    
    payment_table = Table(payment_data, colWidths=[2*inch, 3*inch])
    payment_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#FF5722')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(payment_table)
    
    doc.build(story)
    print(f"Created SBI sample: {filename}")

def create_axis_sample():
    filename = "backend/samples/axis_sample.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Header with burgundy theme
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#951C76'),
        alignment=1,
        spaceAfter=30
    )
    
    story.append(Paragraph("AXIS BANK CREDIT CARD STATEMENT", header_style))
    
    # Customer Details
    customer_data = [
        ['Card Member: RAJESH KUMAR', 'Card Number: XXXX XXXX XXXX 8765'],
        ['Statement Date: 25-Nov-2024', 'Credit Limit: ₹3,50,000'],
        ['Customer ID: AXIS456789', 'Available Credit: ₹2,89,123']
    ]
    
    customer_table = Table(customer_data, colWidths=[3*inch, 3*inch])
    customer_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#951C76')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(customer_table)
    story.append(Spacer(1, 20))
    
    # Account Summary
    story.append(Paragraph("ACCOUNT SUMMARY", styles['Heading2']))
    summary_data = [
        ['Previous Balance', '₹38,765.00'],
        ['Current Purchases', '₹22,358.00'],
        ['Payments & Credits', '₹-20,000.00'],
        ['Total Amount Due', '₹41,123.00'],
        ['Minimum Amount Due', '₹4,112.00']
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#951C76')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#E1BEE7')),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#CE93D8')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Transaction Details
    story.append(Paragraph("TRANSACTION DETAILS", styles['Heading2']))
    transaction_data = [
        ['Date', 'Merchant/Description', 'Amount (₹)'],
        ['12-Nov-2024', 'FLIPKART ONLINE SHOPPING', '9,876.00'],
        ['15-Nov-2024', 'SWIGGY FOOD DELIVERY', '2,345.00'],
        ['18-Nov-2024', 'INDIANOIL PETROL PUMP', '3,500.00'],
        ['21-Nov-2024', 'MYNTRA FASHION STORE', '4,567.00'],
        ['23-Nov-2024', 'NETFLIX SUBSCRIPTION', '799.00']
    ]
    
    transaction_table = Table(transaction_data, colWidths=[1.5*inch, 3*inch, 1.5*inch])
    transaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#951C76')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(transaction_table)
    story.append(Spacer(1, 20))
    
    # Payment Details
    story.append(Paragraph("PAYMENT DETAILS", styles['Heading2']))
    payment_data = [
        ['Billing Cycle:', '01-Nov-2024 to 30-Nov-2024'],
        ['Payment Due Date:', '15-Dec-2024'],
        ['Late Payment Fee:', '₹550 + applicable taxes']
    ]
    
    payment_table = Table(payment_data, colWidths=[2*inch, 3*inch])
    payment_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#6A1B9A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(payment_table)
    
    doc.build(story)
    print(f"Created Axis sample: {filename}")

def create_citi_sample():
    filename = "backend/samples/citi_sample.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    # Header with blue theme
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#0065A3'),
        alignment=1,
        spaceAfter=30
    )
    
    story.append(Paragraph("CITIBANK CREDIT CARD STATEMENT", header_style))
    
    # Account Information
    account_data = [
        ['Account Holder: RAJESH KUMAR', 'Card Number: XXXX XXXX XXXX 2468'],
        ['Statement Date: 25-Nov-2024', 'Credit Limit: ₹4,00,000'],
        ['Account Number: CITI123456789', 'Reward Points: 15,678']
    ]
    
    account_table = Table(account_data, colWidths=[3*inch, 3*inch])
    account_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0065A3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(account_table)
    story.append(Spacer(1, 20))
    
    # Statement Summary
    story.append(Paragraph("STATEMENT SUMMARY", styles['Heading2']))
    summary_data = [
        ['Previous Statement Balance', '₹35,678.00'],
        ['Payments & Credits', '₹-30,000.00'],
        ['New Purchases & Charges', '₹25,567.00'],
        ['Total Amount Due', '₹31,245.00'],
        ['Minimum Payment Due', '₹3,124.00']
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 2*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0065A3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 3), (-1, 3), colors.HexColor('#B3E5FC')),
        ('BACKGROUND', (0, 4), (-1, 4), colors.HexColor('#4FC3F7')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 20))
    
    # Transaction Details
    story.append(Paragraph("TRANSACTION DETAILS", styles['Heading2']))
    transaction_data = [
        ['Date', 'Transaction Description', 'Amount (₹)'],
        ['11-Nov-2024', 'AMAZON PRIME VIDEO', '1,499.00'],
        ['14-Nov-2024', 'BLOOMINGDALE SHOPPING', '8,765.00'],
        ['17-Nov-2024', 'UBER EATS FOOD DELIVERY', '1,890.00'],
        ['19-Nov-2024', 'APPLE STORE PURCHASE', '10,899.00'],
        ['22-Nov-2024', 'BOOKMYSHOW ENTERTAINMENT', '2,514.00']
    ]
    
    transaction_table = Table(transaction_data, colWidths=[1.5*inch, 3*inch, 1.5*inch])
    transaction_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0065A3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(transaction_table)
    story.append(Spacer(1, 20))
    
    # Payment Information
    story.append(Paragraph("PAYMENT INFORMATION", styles['Heading2']))
    payment_data = [
        ['Statement Period:', '01-Nov-2024 to 30-Nov-2024'],
        ['Payment Due Date:', '15-Dec-2024'],
        ['Late Payment Charges:', '₹700 + GST']
    ]
    
    payment_table = Table(payment_data, colWidths=[2*inch, 3*inch])
    payment_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0288D1')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    story.append(payment_table)
    
    doc.build(story)
    print(f"Created Citi sample: {filename}")

def generate_all_samples():
    """Generate all sample PDFs"""
    os.makedirs("backend/samples", exist_ok=True)
    
    create_hdfc_sample()
    create_icici_sample()
    create_sbi_sample()
    create_axis_sample()
    create_citi_sample()
    
    print("\nAll sample PDFs generated successfully!")
    print("Files created in backend/samples/ directory")

if __name__ == "__main__":
    generate_all_samples()