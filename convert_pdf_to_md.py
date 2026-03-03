"""
PDF to Markdown Converter
Converts the Belief Dynamics PDF to a markdown file
"""

import pdfplumber
import os

# Define file paths
pdf_path = r"e:\ai_system_design\docs\specifications\Appendix_F_Specs_Reverse_Engineering.pdf"
md_path = r"e:\ai_system_design\docs\specifications\Appendix_F_Specs_Reverse_Engineering.md"

def convert_pdf_to_markdown(pdf_file, output_file):
    """Extract text from PDF and save as markdown"""

    print(f"Opening PDF: {pdf_file}")

    # Check if PDF exists
    if not os.path.exists(pdf_file):
        print(f"Error: PDF file not found at {pdf_file}")
        return False

    try:
        # Open the PDF
        with pdfplumber.open(pdf_file) as pdf:
            print(f"Total pages: {len(pdf.pages)}")

            # Extract text from all pages
            text = ""
            for i, page in enumerate(pdf.pages, 1):
                print(f"Processing page {i}...")
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"

            # Save to markdown file
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"\n✓ Conversion complete!")
            print(f"✓ Markdown file saved to: {output_file}")
            return True

    except Exception as e:
        print(f"Error during conversion: {e}")
        return False

if __name__ == "__main__":
    convert_pdf_to_markdown(pdf_path, md_path)
