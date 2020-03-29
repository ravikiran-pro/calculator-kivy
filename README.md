### Kivy tutorial  --covid19

kivy is python library used to make multi-platform applications.
My curiosity on doing android application made me try a short solution and landed on kivy.

This repo contains 
            -  A simple calculator application to understand the basic block of kivy
            -  A offline diary made for android
            
#### Directories
- Diary           -- Files for diary applications
- Calculator      -- Calculator.py
- Tutorials       -- Contains tutorials for basic text,buttons,layout,scrollbar,views etc.
- Buildozer       -- Module used to convert kivy to apk

#### Prerequisite
          sudo apt-get install python-kivy
          kivy needs a virtual environment source 
                /var/virtualenv/kivy/bin/activate
          kivy requires cython 
                pip install cython  
          diary requires sqlite3  --pip install sqlite3
          
#### Build
          Download and unzip the git folder or git clone
          cd kivy-application
          Diary     -- python diary/base.py
          calendar  -- python calculator-app/calculator.py
