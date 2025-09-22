# Geometry Dash Song Swapper

A simple desktop application built with Python and CustomTkinter that allows you to swap songs in Geometry Dash by dragging and dropping .mp3 files.

## Features

- **Drag and Drop Interface**: Easily drag and drop .mp3 files into the application
- **Song ID Management**: Specify custom song IDs for your swapped songs
- **File Validation**: Automatically validates .mp3 files and filters out invalid ones
- **Cross-Platform Support**: Works on Windows, macOS, and Linux
- **Visual Feedback**: Progress indicators and status messages for all operations
- **Error Handling**: Comprehensive error handling with user-friendly messages

## Installation

### Prerequisites

- Python 3.7 or higher
- Geometry Dash installed on your system

### Setup

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## Usage

1. **Launch the Application**: Run `python main.py` to start the Geometry Dash Song Swapper

2. **Add Songs**: 
   - Drag and drop .mp3 files onto the blue drop zone
   - OR click the drop zone to browse for .mp3 files
   - Only .mp3 files will be accepted

3. **Set Song ID**: 
   - Enter a numeric song ID in the "Song ID" field
   - This ID will determine where your song appears in Geometry Dash

4. **Swap the Song**:
   - Click the "Swap Song" button to copy the first dropped file to your Geometry Dash songs directory
   - The file will be named `{song_id}.mp3` in the `songs` folder

5. **Manage Files**:
   - Use the "×" button next to each file to remove it from the list
   - Use the "Clear" button to remove all files at once

## Geometry Dash Directory Support

The application automatically detects your Geometry Dash installation directory based on your operating system:

- **Windows**: `%LOCALAPPDATA%/GeometryDash`
- **macOS**: `~/Library/Application Support/GeometryDash`
- **Linux**: `~/.local/share/GeometryDash`

If the directory doesn't exist, the application will show an error message.

## File Structure

```
GDSongSwapper/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # This documentation
└── assets/                # Optional icons/images (future)
```

## Dependencies

- **customtkinter>=5.2.0**: Modern tkinter wrapper for beautiful GUI
- **tkinter**: Built-in Python GUI library (usually comes with Python)
- **pathlib**: Modern path handling (built-in)
- **shutil**: File operations (built-in)
- **os**: Operating system interface (built-in)
- **threading**: Multi-threading support (built-in)
- **platform**: Platform detection (built-in)

## Troubleshooting

### Common Issues

1. **"Geometry Dash directory not found"**
   - Make sure Geometry Dash is installed on your system
   - Check that you have the correct permissions to access the directory

2. **"No valid .mp3 files found"**
   - Ensure you're only dragging .mp3 files
   - Check that the files are not corrupted

3. **"Permission denied"**
   - Run the application as administrator/root if needed
   - Check file permissions on your Geometry Dash installation

4. **Application won't start**
   - Make sure you have Python 3.7 or higher installed
   - Verify all dependencies are installed: `pip install -r requirements.txt`

### Platform-Specific Notes

- **Windows**: The application uses `%LOCALAPPDATA%` which should point to your local app data directory
- **macOS**: You may need to grant accessibility permissions for the application to work properly
- **Linux**: Make sure you have the necessary GUI libraries installed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues and enhancement requests!

## Support

If you encounter any problems or have questions, please open an issue on the GitHub repository.

---

**Note**: This application is not affiliated with RobTop Games or Geometry Dash. Use at your own risk.