# Game Launcher
Launch all your games, from different launchers, from one page

## Features
* Launchers
  * Supported
    * Steam
    * Origin
* Poster Downloads
  * Direct from Steam (for Steam games)
  * From IGDB (for all other launchers)
* macOS Support

## Planned Features
* Support for other launchers (including Epic Games)
* Better cover downloads (help needed)
* Windows and Linux support
* Web endpoint to download covers (eliminating Running Locally - step #4)
* One-click executable to run the program

## Running Locally
1. Clone the repository to your computer
2. Create a directory named `covers` in the `assets` directory
3. Install the two requirements with `pip3 install -r requirements.txt`
4. Edit the `settings.py` to match your configuration
  * **Note:** Only macOS is supported at this time. To help port this to Windows and Linux, please make a pull request.
5. Run `backend.py` (every time you need to download covers, future support planned to eliminate this)
6. Run the Flask server with `python3 web_interface.py`

## Changelog
* Version 0.1.0 (2020-02-23):
  * Initital support
