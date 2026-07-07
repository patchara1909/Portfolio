from pathlib import Path
import sys
from pypdf import PdfReader

pdf_path = Path('PORTFOLIO.pdf')
print('exists', pdf_path.exists())
if not pdf_path.exists():
    sys.exit(1)
reader = PdfReader(str(pdf_path))
print('pages', len(reader.pages))
for i, page in enumerate(reader.pages, 1):
    text = page.extract_text() or ''
    print(f'===== PAGE {i} =====')
    print(text[:8000])
    print()
