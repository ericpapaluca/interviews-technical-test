import sys
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the desired folder to sys.path
target_folder = os.path.join(current_dir, 'resources')
sys.path.insert(0, target_folder)
