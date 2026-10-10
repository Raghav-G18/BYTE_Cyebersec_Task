# BYTE Steganography Task 2 - Solution & Write-up

A complete technical breakdown and automated resolution for the steganography and file-repair challenge.

## 📁 Repository Structure
- `challenge.png` - The original corrupted task file.
- `repair.png` - The structurally fixed and cleaned output image.
- `repair_and_extract.py` - The end-to-end automation script that cleans, repairs, and processes the file.
- `README.md` - Technical write-up and methodology documentation.

---

## 🛠️ Methodology & Approach

### 1. Handling File Corruption & Trailing Junk Bytes
- **Analysis:** Initial inspection of `challenge.png` showed it failed to render across standard image viewers due to structure corruption and extraneous trailing bytes appended to the EOF (End of File).
- **Resolution:** Developed a binary parser script that locates the official PNG end marker signature (`IEND`: `49 45 4E 44 AE 42 60 82`) and strips all extraneous trailing data, generating a clean payload (`repair.png`).

### 2. Header Normalization & Parsing
- Patched internal chunks and normalized the image matrix using Pillow to ensure cross-platform compatibility and correct rendering.

### 3. Steganography & Flag Extraction
- **Observation:** The hidden text payload was embedded using extremely faint, near-black RGB pixel values blended into a dark background.
- **Extraction:** Applied a contrast-stretching pixel transformation filter (`r * 64`, `g * 64`, `b * 64`) to force the hidden pixels to pop out brightly against the background.

---

## 🎯 Final Flag
> **`flag{g0t 1t in p1ain sight}`**

## 🚀 How to Run the Automation Script
1. Place your target file as `challenge.png` in the root folder.
2. Run the pipeline script via terminal:
   ```bash
   python3 repair_and_extract.py
