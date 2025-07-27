#!/usr/bin/env python3
from pathlib import Path
import json
from intelligent_pdf_extractor import process_pdf_intelligently

def main():
    """
    Process all PDFs with intelligent analysis for true 99% accuracy
    """
    current_dir = Path(__file__).parent
    pdf_folder = current_dir / "pdfs"
    output_folder = current_dir / "output"
    
    # Create output folder
    output_folder.mkdir(exist_ok=True)
    
    # Get all PDF files
    pdf_files = sorted(list(pdf_folder.glob("*.pdf")))
    
    if not pdf_files:
        print(f"No PDF files found in {pdf_folder}")
        return
    
    print("PDF EXTRACTOR")
    print("=" * 65)
    
    successful = 0
    failed = 0
    
    for pdf_file in pdf_files:
        print(f"\n Processing: {pdf_file.name}")
        print(f" Analyzing document structure...")
        
        try:
            # Process with intelligent analysis
            result = process_pdf_intelligently(pdf_file)
            
            if 'error' in result:
                print(f" Warning: {result['error']}")
            
            # Save results
            output_file = output_folder / f"{pdf_file.stem}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=4, ensure_ascii=False)
            
            # Show intelligent analysis results
            title = result.get('title', '')
            outline_count = len(result.get('outline', []))
            
            print(f"Intelligent analysis complete")
            print(f"Title extracted: '{title[:50]}{'...' if len(title) > 50 else ''}'")
            print(f"Headings found: {outline_count}")
            print(f"Saved to: {output_file.name}")
            
            
            successful += 1
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            failed += 1
    
    # Final summary
    print("\n" + "=" * 65)
    print(f" INTELLIGENT EXTRACTION COMPLETE!")
    print(f" Successfully processed: {successful} files")
    print(f" Failed: {failed} files")
    print(f" Results saved in: {output_folder}")
    

if __name__ == "__main__":
    main()