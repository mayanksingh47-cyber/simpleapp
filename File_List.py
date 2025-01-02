import os
import streamlit as st

# Function to list files in a directory
def list_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        return [str(e)]

# Function to delete files in a directory
def cleanup_directory(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                os.rmdir(file_path)
        return True
    except Exception as e:
        return str(e)

# Streamlit app
def main():
    st.title("File Listing and Cleanup App")
    
    # Directories to list files from
    directories = [r'C:\temp', r'C:\pythonfolder']
    
    for directory in directories:
        st.subheader(f"Files in {directory}:")
        files = list_files_in_directory(directory)
        
        if files:
            for file in files:
                st.write(file)
        else:
            st.write("No files found or directory not accessible.")
    
    # Cleanup option for C:\temp
    st.subheader("Cleanup Option")
    if st.button("Clean up C:\\temp"):
        result = cleanup_directory(r'C:\temp')
        if result is True:
            st.success("C:\\temp cleaned up successfully.")
        else:
            st.error(f"Failed to clean up C:\\temp: {result}")

if __name__ == "__main__":
    main()
