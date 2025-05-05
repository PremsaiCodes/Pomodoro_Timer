# Pomodoro Timer Application

## Project Description

The Pomodoro Timer is a productivity application that helps users implement the Pomodoro Technique - a time management method developed by Francesco Cirillo. This technique uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks (5 minutes) and longer breaks (20 minutes) after four work sessions.

### Key Features:

- **Customizable Timer**: Set work sessions (25 mins), short breaks (5 mins), and long breaks (20 mins)
- **Visual Feedback**: Color-coded display for different timer states
- **Progress Tracking**: Checkmark system to track completed work sessions
- **Sound Notifications**: Distinct sounds for session transitions
  - Bell sound for work/short break transitions
  - Clapping sound for long breaks
- **Simple Interface**: Clean, intuitive GUI with start/reset controls

The application is built using Python with Tkinter for the graphical interface and includes system sounds for notifications (Windows) or can be configured with custom sound files for cross-platform use.

## README.md File

```markdown
# Pomodoro Timer Application

![Pomodoro Timer Screenshot](tomato.png)

A productivity timer application implementing the Pomodoro Technique to help you focus and manage your work sessions effectively.

## Features

- 🕒 Customizable work/break intervals
- 🔔 Audio notifications for session transitions
- ✅ Visual progress tracking
- 🎨 Clean, intuitive interface
- 🖱️ Simple start/reset controls

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/PremsaiCodes/Pomodoro_Timer.git
   cd Pomodoro-Timer
   ```

2. Ensure you have Python 3.x installed

3. (Optional) For cross-platform sound support, install playsound:
   ```bash
   pip install playsound
   ```

## Usage

1. Run the application:
   ```bash
   python pomodoro-start.py
   ```

2. Click "Start" to begin your work session

3. The timer will automatically cycle through:
   - 25-minute work sessions
   - 5-minute short breaks
   - 20-minute long breaks (after 4 work sessions)

4. Use "Reset" to stop the current session and clear progress

## Configuration

To customize the timer durations, modify these constants in the code:
```python
WORK_MIN = 25        # Work session duration in minutes
SHORT_BREAK_MIN = 5  # Short break duration in minutes
LONG_BREAK_MIN = 20  # Long break duration in minutes
```

For custom sounds (cross-platform):
1. Add your sound files (MP3 or WAV format) to the project directory
2. Update the sound functions to point to your files

## Dependencies

- Python 3.x
- Tkinter (usually included with Python)
- (Optional) `playsound` package for cross-platform audio support

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---


## Project Structure

```
pomodoro-timer/
├── pomodoro.py         # Main application code
├── README.md           # Project documentation
├── tomato.png          # Tomato image asset
├── requirements.txt    # Python dependencies
├── LICENSE             # License file
└── sounds/             # (Optional) Directory for sound files
    ├── bell.mp3        # Bell sound
    └── clapping.mp3    # Clapping sound
```
