#!/usr/bin/env python3
"""
GoPhish Campaign Report Generator
Automates data collection from GoPhish API and generates PDF reports.
"""

import requests
import json
from datetime import datetime
from fpdf import FPDF
import argparse
import os

# Configuration - Update these values
API_KEY = "your_api_key_here"  # GoPhish API key
GOPHISH_URL = "http://localhost:3333"  # GoPhish admin URL
OUTPUT_DIR = "reports"  # Directory to save reports

class GoPhishReporter:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        self.ensure_output_dir()
        
    def ensure_output_dir(self):
        """Ensure output directory exists"""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    
    def get_campaigns(self):
        """Fetch all campaigns from GoPhish"""
        url = f"{GOPHISH_URL}/api/campaigns/"
        response = requests.get(url, headers=self.headers, verify=False)
        return response.json()
    
    def get_campaign_details(self, campaign_id):
        """Get detailed results for a specific campaign"""
        url = f"{GOPHISH_URL}/api/campaigns/{campaign_id}/results"
        response = requests.get(url, headers=self.headers, verify=False)
        return response.json()
    
    def generate_report(self, campaign_data, details):
        """Generate PDF report for a campaign"""
        pdf = FPDF()
        pdf.add_page()
        
        # Report header
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Phishing Campaign Report', 0, 1, 'C')
        pdf.ln(10)
        
        # Campaign metadata
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Campaign Overview', 0, 1)
        pdf.set_font('Arial', '', 10)
        
        # Basic campaign info
        pdf.cell(0, 10, f"Name: {campaign_data['name']}", 0, 1)
        pdf.cell(0, 10, f"Created: {campaign_data['created_date']}", 0, 1)
        pdf.cell(0, 10, f"Status: {campaign_data['status']}", 0, 1)
        pdf.ln(5)
        
        # Statistics
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Campaign Statistics', 0, 1)
        pdf.set_font('Arial', '', 10)
        
        stats = [
            ("Total Sent", details['stats']['total']),
            ("Emails Opened", details['stats']['opened']),
            ("Clicked Links", details['stats']['clicked']),
            ("Submitted Data", details['stats']['submitted_data']),
            ("Email Reported", details['stats']['reported'])
        ]
        
        for stat in stats:
            pdf.cell(0, 10, f"{stat[0]}: {stat[1]}", 0, 1)
        pdf.ln(10)
        
        # Results table
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, 'Detailed Results', 0, 1)
        pdf.set_font('Arial', 'B', 10)
        
        # Table header
        col_widths = [40, 40, 60, 30, 20]
        headers = ["First Name", "Last Name", "Email", "Status", "Reported"]
        for i, header in enumerate(headers):
            pdf.cell(col_widths[i], 10, header, 1, 0, 'C')
        pdf.ln()
        
        # Table rows
        pdf.set_font('Arial', '', 8)
        for result in details['results']:
            pdf.cell(col_widths[0], 10, result['first_name'] or '-', 1)
            pdf.cell(col_widths[1], 10, result['last_name'] or '-', 1)
            pdf.cell(col_widths[2], 10, result['email'], 1)
            pdf.cell(col_widths[3], 10, result['status'], 1)
            pdf.cell(col_widths[4], 10, "Yes" if result['reported'] else "No", 1)
            pdf.ln()
        
        # Save the report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{OUTPUT_DIR}/report_{campaign_data['name']}_{timestamp}.pdf"
        pdf.output(filename)
        print(f"Report generated: {filename}")
        
        return filename

def main():
    parser = argparse.ArgumentParser(description='GoPhish Campaign Report Generator')
    parser.add_argument('--all', action='store_true', help='Generate reports for all campaigns')
    parser.add_argument('--campaign', type=int, help='Generate report for specific campaign ID')
    args = parser.parse_args()
    
    reporter = GoPhishReporter()
    
    if args.all:
        campaigns = reporter.get_campaigns()
        for campaign in campaigns:
            details = reporter.get_campaign_details(campaign['id'])
            reporter.generate_report(campaign, details)
    elif args.campaign:
        details = reporter.get_campaign_details(args.campaign)
        campaign = next((c for c in reporter.get_campaigns() if c['id'] == args.campaign), None)
        if campaign:
            reporter.generate_report(campaign, details)
        else:
            print(f"Campaign with ID {args.campaign} not found")
    else:
        print("Please specify either --all or --campaign <ID>")

if __name__ == "__main__":
    main()