import os
import zipfile
import sys

def extract_zips(source_folder):
    """Extract ZIP files from source_folder into their own subfolders."""
    if not os.path.isdir(source_folder):
        print(f"Error: '{source_folder}' is not a valid directory.")
        return
    
    extracted_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.zip'):
            zip_path = os.path.join(source_folder, filename)
            folder_name = os.path.splitext(filename)[0]
            
            if not folder_name:
                print(f"Skipping invalid file: {filename}")
                continue
            
            output_folder = os.path.join(source_folder, folder_name)
            
            try:
                os.makedirs(output_folder, exist_ok=True)
                
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(output_folder)
                print(f"Extracted: {filename} -> {folder_name}/")
                extracted_count += 1
                
            except zipfile.BadZipFile:
                print(f"Error: {filename} is not a valid ZIP file")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
    
    print(f"\nOperation complete. Extracted {extracted_count} ZIP file(s).")

if __name__ == "__main__":
    target_folder = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    
    target_folder = os.path.normpath(target_folder)
    
    print(f"Processing ZIP files in: {target_folder}\n" + "-" * 50)
    extract_zips(target_folder)
    print("\nPress Enter to exit...")
    input()