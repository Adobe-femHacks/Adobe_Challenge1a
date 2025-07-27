# Intelligent PDF Extractor

## Approach

This solution uses advanced document analysis and pattern recognition to extract true headings and document outlines from PDFs. It avoids hardcoded rules and instead analyzes font sizes, formatting, text patterns, and document structure to distinguish between real headings, form fields, and noise. The extractor combines rule-based and statistical techniques to adapt to a wide variety of document types.

**Detailed Approach:**

- **Text Block Extraction:**  
  Each PDF page is parsed into text blocks, capturing not just the text but also metadata such as font size, font name, bold/italic status, capitalization, position, and indentation. This rich representation allows for nuanced analysis.

- **Document Structure Analysis:**  
  The extractor computes statistics (like median font size) to estimate the "body" text size and identify outliers that may indicate headings. It also analyzes the distribution of font sizes and formatting across the document.

- **Form Field and Noise Filtering:**  
  Using a combination of regular expressions and heuristics, the extractor identifies and ignores form fields (e.g., "Name:", "Date:") and common noise (e.g., page numbers, copyright notices).

- **Multi-layered Heading Detection:**  
  Headings are detected using a combination of:
  - **Pattern Matching:** Recognizes common heading patterns (e.g., "1. Introduction", "Table of Contents").
  - **Formatting Analysis:** Considers font size, boldness, capitalization, centering, and indentation.
  - **Contextual Filtering:** Avoids false positives by checking for sentence length, punctuation, and similarity to the document title.

- **Adaptive Heading Level Assignment:**  
  Heading levels (H1, H2, H3, H4) are assigned based on a combination of formatting cues, detected patterns, and context. For example, larger and bolder text near the top of the first page is likely H1, while indented or smaller bold text may be H3/H4.

- **Deduplication and Outline Construction:**  
  The extractor uses fuzzy matching to avoid duplicate headings and constructs a clean, hierarchical outline. The document title is extracted separately and excluded from the outline.

- **Fallback and Robustness:**  
  If the optional `universal_pdf_extractor` module is available, it is used for even higher accuracy. Otherwise, the built-in intelligent extractor is used, which is robust to a wide range of business and technical document layouts.

**Key features:**
- No hardcoding of document-specific rules.
- Multi-layered heading detection using formatting, position, and text analysis.
- Form field and noise filtering.
- Adaptive heading level assignment (H1/H2/H3/H4) based on context and formatting.

## Models and Libraries Used

- **PyMuPDF (`fitz`)**: For PDF parsing and text extraction.
- **NumPy**: For statistical analysis of font sizes and formatting.
- **Standard Python libraries**: `re`, `json`, `dataclasses`, `collections`, etc.

No machine learning models are used; the approach is based on intelligent heuristics and document analysis.

## Folder Structure

```
.
├── main.py
├── intelligent_pdf_extractor.py
├── requirements.txt
├── Dockerfile
├── pdfs/           # Place your input PDF files here
├── output/         # Extracted JSON results will be saved here
└── README.md
```

## How to Build and Run (with Docker)

1. **Build the Docker image:**
   ```sh
   docker build -t pdf-extractor .
   ```

2. **Prepare your PDFs:**
   - Place all PDF files to be processed in the `pdfs` folder inside the project directory.

3. **Run the extractor:**
   ```sh
   docker run --rm -v "$(pwd)/pdfs:/app/pdfs" -v "$(pwd)/output:/app/output" pdf-extractor
   ```

   - The script will process all PDFs in the `pdfs` folder, extract titles and outlines, and save the results as JSON files in the `output` folder.

4. **Output:**
   - For each PDF, a corresponding `.json` file will be created in the `output` directory, containing the extracted title and outline.

## Notes

- The solution is designed to work out-of-the-box for a wide range of business and technical documents.
- If the optional `universal_pdf_extractor` module is present, it will be used for even higher accuracy; otherwise, the built-in intelligent extractor is used.
