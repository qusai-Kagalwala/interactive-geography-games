# 🗺️ Interactive Geography Games

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org/)
[![Turtle Graphics](https://img.shields.io/badge/Turtle-Graphics-orange.svg)](https://docs.python.org/3/library/turtle.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Educational](https://img.shields.io/badge/Purpose-Educational-purple.svg)](https://github.com/qusai-Kagalwala/interactive-geography-games)

> 🎯 **Interactive map-based geography games with Python Turtle graphics. Learn US states and Indian geography through engaging quizzes with automatic study guide generation.**

---

## 🌟 Features

### 🇺🇸 **US States Game (Course Version)**
- ✅ Interactive map-based learning interface
- 📊 Real-time progress tracking (X/50 states)
- 🎯 Visual feedback on correct answers
- 📝 Automatic study guide generation for missed states
- 🚪 Clean exit mechanism with progress saving

### 🇮🇳 **India States & Union Territories Game (Personal Version)**
- 🗺️ Comprehensive coverage of 28 states + 8 union territories
- 📍 Precise coordinate-based positioning
- 💾 Personalized learning materials export
- 🎮 User-friendly GUI with turtle graphics

### 🛠️ **Coordinate Mapping Tool**
- 🖱️ Click-to-capture coordinate system
- 📋 CSV export functionality
- ⌨️ Keyboard shortcuts for efficiency
- 🧹 Reset and clear functionality

### 📊 **CSV Data Analysis Examples**
- 🐿️ Central Park Squirrel Census analysis
- 🌤️ Weather data processing examples
- 📈 Data visualization and export techniques
- 💡 Pandas DataFrame manipulation tutorials

---

## 🚀 Quick Start

### Prerequisites
```bash
# Required Python packages
pip install pandas turtle
```

### 📥 Installation
```bash
# Clone the repository
git clone https://github.com/qusai-Kagalwala/interactive-geography-games.git
cd interactive-geography-games
```

### 🎮 Running the Games

#### US States Game (Course Version)
```bash
cd 01-course-version
python main.py
```

#### India Geography Game (Personal Version)
```bash
cd 02-personal-version
python main.py
```

#### Coordinate Mapping Tool
```bash
cd 02-personal-version
python co-ordinate.py
```

#### CSV Data Analysis Examples
```bash
cd csv_data_analysis
python main.py
```

---

## 📂 Project Structure

```
interactive-geography-games/
├── 📁 01-course-version/
│   ├── main.py                    # 🇺🇸 US States game (original)
│   ├── 50_states.csv             # 📊 US states coordinate data
│   ├── blank_states_img.gif      # 🗺️ US map image
│   └── states_to_learn.csv       # 📚 Generated study guide
├── 📁 02-personal-version/
│   ├── main.py                    # 🇮🇳 India geography game
│   ├── 28_states_8_u.t.csv      # 📊 Indian states/UTs data
│   ├── co-ordinate.py            # 🛠️ Coordinate mapping tool
│   ├── clicked_coordinates.csv   # 📍 Captured coordinates
│   ├── blank_states_img.gif      # 🗺️ India map image
│   └── states_to_learn.csv       # 📚 Study materials
├── 📁 csv_data_analysis/
│   ├── main.py                   # 🐿️ Squirrel census analysis
│   ├── weather_data.csv          # 🌤️ Sample weather data
│   ├── squirrel_count.csv        # 📈 Analysis results
│   └── new_data.csv              # 📊 Sample DataFrame export
├── LICENSE                       # 📜 MIT License
└── README.md                     # 📖 This file
```

---

## 🎯 How to Play

### 🎮 Game Controls
1. **Start the game** - Run the main.py file
2. **Enter state names** - Type in the popup dialog
3. **View progress** - Track your score in real-time
4. **Exit anytime** - Type "Exit" to generate study materials
5. **Study missed states** - Use the generated CSV files

### ⌨️ Keyboard Shortcuts (Coordinate Tool)
- `S` - Save coordinates to CSV
- `C` - Clear all points and restart
- `Click` - Capture coordinates

---

## 📊 Data Files

| File | Description | Format |
|------|-------------|---------|
| `50_states.csv` | 🇺🇸 US states coordinates | `state,x,y` |
| `28_states_8_u.t.csv` | 🇮🇳 Indian geography data | `state,x,y` |
| `states_to_learn.csv` | 📚 Personalized study guide | Auto-generated |
| `clicked_coordinates.csv` | 📍 Mapped coordinates | `click_number,x,y` |

---

## 🔧 Technical Details

### 🐍 **Core Technologies**
- **Python 3.7+** - Main programming language
- **Turtle Graphics** - Interactive game interface
- **Pandas** - CSV data manipulation and analysis
- **CSV Module** - Coordinate data export

### 🏗️ **Architecture**
- **Event-driven programming** with mouse and keyboard handlers
- **Real-time data processing** with pandas DataFrames
- **Interactive GUI** using turtle graphics
- **Modular design** for easy customization

---

## 🎓 Learning Objectives

This project demonstrates key programming concepts:

- 📊 **Data Analysis** - Working with CSV files using pandas
- 🎮 **GUI Development** - Interactive interfaces with turtle graphics
- 🖱️ **Event Handling** - Mouse clicks and keyboard input
- 💾 **File I/O** - Reading and writing CSV data
- 🔍 **Data Filtering** - Boolean indexing and data manipulation
- 🎯 **Game Logic** - Progress tracking and user interaction

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 **Fork the repository**
2. 🔧 **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push to the branch** (`git push origin feature/AmazingFeature`)
5. 🔀 **Open a Pull Request**

### 💡 **Ideas for Contributions**
- 🌍 Add more countries/regions
- 🎨 Improve UI/UX design
- 📱 Mobile-friendly version
- 🔊 Add sound effects
- 🏆 Implement scoring system
- ⏱️ Add timer functionality

---

## 📋 TODO

- [ ] 🌐 Add world capitals game
- [ ] 🎵 Sound effects and music
- [ ] 🏆 High score leaderboard
- [ ] 📱 Mobile app version
- [ ] 🌙 Dark mode theme
- [ ] 🔄 Difficulty levels
- [ ] 📊 Statistics dashboard
- [ ] 🎯 Achievement system

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Qusai Kagalwala**
- GitHub: [@qusai-Kagalwala](https://github.com/qusai-Kagalwala)
- Project Link: [https://github.com/qusai-Kagalwala/interactive-geography-games](https://github.com/qusai-Kagalwala/interactive-geography-games)

---

## 🙏 Acknowledgments

- 🎓 **Angela Yu's 100 Days of Code** - Python Bootcamp inspiration
- 🗺️ **Open source map data** - Geographic coordinate information
- 🐍 **Python Community** - For excellent libraries and documentation
- 📚 **Educational resources** - Making geography fun and interactive

---

## 📸 Screenshots

> 🖼️ *Add screenshots of your games in action here*

---

<div align="center">

### 🌟 **Star this repository if you found it helpful!** 🌟

**Made with ❤️ and Python**

[![Star History Chart](https://api.star-history.com/svg?repos=qusai-Kagalwala/interactive-geography-games&type=Date)](https://star-history.com/#qusai-Kagalwala/interactive-geography-games&Date)

</div>
