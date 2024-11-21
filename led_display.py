import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

class SixteenSegmentDisplay:
    def __init__(self, master, position):
        self.canvas = tk.Canvas(master, width=120, height=180, bg='black')
        self.canvas.grid(row=0, column=position, padx=10, pady=10)
        
        # Enhanced colors for better visibility
        self.off_color = '#1a1a1a'  # Dark grey when off
        self.on_color = '#ff0000'   # Bright red when on
        
        # Initialize segments
        self.segments = {}
        self.segment_types = {}  # Track whether segment is line or rectangle
        self.create_segments()
        
        # Turn all segments off initially
        self.clear()
    
    def create_segments(self):
        # Segment coordinates with corrected slopes for j and k
        segments = {
            'a1': [(25, 15, 55, 22)],     # top left horizontal
            'a2': [(65, 15, 95, 22)],     # top right horizontal
            'b': [(95, 22, 102, 87)],     # top right vertical
            'c': [(95, 93, 102, 158)],    # bottom right vertical
            'd1': [(25, 158, 55, 165)],   # bottom left horizontal
            'd2': [(65, 158, 95, 165)],   # bottom right horizontal
            'e': [(18, 93, 25, 158)],     # bottom left vertical
            'f': [(18, 22, 25, 87)],      # top left vertical
            'g1': [(25, 87, 55, 93)],     # middle left horizontal
            'g2': [(65, 87, 95, 93)],     # middle right horizontal
            'h': [(25, 22, 58, 87)],      # diagonal from top left to center
            'i': [(58, 22, 62, 87)],      # middle top vertical
            'j': [(62, 87, 95, 22)],      # diagonal from center to top right (fixed slope)
            'k': [(25, 158, 58, 93)],     # diagonal from center to bottom left (fixed slope)
            'l': [(58, 93, 62, 158)],     # middle bottom vertical
            'm': [(62, 93, 95, 158)]      # diagonal from center to bottom right
        }
        
        for segment, coords_list in segments.items():
            self.segments[segment] = []
            for coords in coords_list:
                if segment in ['h', 'j', 'k', 'm']:  # Diagonal segments
                    segment_id = self.canvas.create_line(
                        coords[0], coords[1], coords[2], coords[3],
                        width=4, fill=self.off_color
                    )
                    self.segment_types[segment_id] = 'line'
                else:
                    segment_id = self.canvas.create_rectangle(
                        coords[0], coords[1], coords[2], coords[3],
                        fill=self.off_color, outline=self.off_color
                    )
                    self.segment_types[segment_id] = 'rectangle'
                self.segments[segment].append(segment_id)

    def set_segment(self, segment, state):
        if segment in self.segments:
            color = self.on_color if state else self.off_color
            for segment_part in self.segments[segment]:
                if self.segment_types[segment_part] == 'line':
                    self.canvas.itemconfig(segment_part, fill=color)
                else:
                    self.canvas.itemconfig(segment_part, fill=color, outline=color)

    def clear(self):
        for segment in self.segments:
            self.set_segment(segment, False)

class LEDDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("16-Segment LED Display")
        self.root.configure(bg='#000000')
        
        # Create custom styles
        self.create_styles()
        
        # Create main frame with black background
        self.main_frame = ttk.Frame(root, style='Black.TFrame')
        self.main_frame.pack(pady=20, padx=20)
        
        # Create title label
        title_font = tkfont.Font(family="Arial", size=16, weight="bold")
        title_label = tk.Label(self.main_frame, 
                             text="16-Segment LED Display Simulator",
                             font=title_font,
                             fg='#00ff00',  # Bright green
                             bg='#000000')
        title_label.pack(pady=(0, 20))
        
        # Create frame for displays
        self.display_frame = ttk.Frame(self.main_frame, style='Black.TFrame')
        self.display_frame.pack(pady=10)
        
        # Create 6 displays
        self.displays = []
        for i in range(6):
            display = SixteenSegmentDisplay(self.display_frame, i)
            self.displays.append(display)
        
        # Create styled input frame
        self.input_frame = ttk.Frame(self.main_frame, style='Black.TFrame')
        self.input_frame.pack(pady=20)
        
        # Create input section with modern design
        input_container = ttk.Frame(self.input_frame, style='Black.TFrame')
        input_container.pack(pady=10)
        
        # Input label with custom font
        label_font = tkfont.Font(family="Arial", size=12)
        self.input_label = tk.Label(input_container, 
                                  text="Enter Text (max 6 chars):",
                                  font=label_font,
                                  fg='#ffffff',
                                  bg='#000000')
        self.input_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Styled entry widget
        self.text_input = tk.Entry(input_container,
                                 width=10,
                                 font=label_font,
                                 bg='#2d2d2d',
                                 fg='#ffffff',
                                 insertbackground='#ffffff',  # Cursor color
                                 relief=tk.FLAT,
                                 justify=tk.CENTER)
        self.text_input.pack(side=tk.LEFT, padx=5)
        
        # Styled display button
        self.display_button = tk.Button(input_container,
                                      text="Display",
                                      command=self.update_display,
                                      font=label_font,
                                      bg='#007bff',  # Blue
                                      fg='#ffffff',
                                      activebackground='#0056b3',  # Darker blue
                                      activeforeground='#ffffff',
                                      relief=tk.FLAT,
                                      padx=20,
                                      pady=5)
        self.display_button.pack(side=tk.LEFT, padx=(10, 0))
        
        # Add instructions
        instruction_font = tkfont.Font(family="Arial", size=10)
        instructions = tk.Label(self.main_frame,
                              text="Supported characters: A-Z and space",
                              font=instruction_font,
                              fg='#888888',
                              bg='#000000')
        instructions.pack(pady=(10, 0))
        
        # Define character patterns
        self.char_patterns = {
            'A': ['a1', 'a2', 'b', 'c', 'f', 'e', 'g1', 'g2'],
            'B': ['a1', 'a2', 'b', 'c', 'd1', 'd2', 'f', 'e', 'g1', 'g2'],
            'C': ['a1', 'a2', 'f', 'e', 'd1', 'd2'],
            'D': ['a1', 'a2', 'b', 'c', 'd1', 'd2', 'i', 'l'],
            'E': ['a1', 'a2', 'f', 'e', 'd1', 'd2', 'g1', 'g2'],
            'F': ['a1', 'a2', 'f', 'e', 'g1', 'g2'],
            'G': ['a1', 'a2', 'c', 'f', 'e', 'd1', 'd2', 'g2'],
            'H': ['b', 'c', 'f', 'e', 'g1', 'g2'],
            'I': ['a1', 'a2', 'i', 'l', 'd1', 'd2'],
            'J': ['b', 'c', 'd1', 'd2'],
            'K': ['f', 'e', 'g1', 'j', 'm'],  # Updated K pattern
            'L': ['f', 'e', 'd1', 'd2'],
            'M': ['f', 'e', 'b', 'c', 'h', 'j'],
            'N': ['f', 'e', 'b', 'c', 'h', 'm'],
            'O': ['a1', 'a2', 'b', 'c', 'd1', 'd2', 'f', 'e'],
            'P': ['a1', 'a2', 'b', 'f', 'e', 'g1', 'g2'],
            'Q': ['a1', 'a2', 'b', 'c', 'd1', 'd2', 'f', 'e', 'm'],
            'R': ['a1', 'a2', 'f', 'e', 'm', 'g1', 'g2','b'],
            'S': ['a1', 'a2', 'f', 'g1', 'g2', 'c', 'd1', 'd2'],
            'T': ['a1', 'a2', 'i', 'l'],
            'U': ['b', 'c', 'e', 'f', 'd1', 'd2'],
            'V': ['f', 'e', 'j', 'k'],
            'W': ['f', 'e', 'b', 'c', 'k', 'm'],
            'X': ['h', 'j', 'k', 'm'],  # Uses all diagonals
            'Y': ['h', 'j', 'l'],
            'Z': ['a1', 'a2', 'j', 'k', 'd1', 'd2'],  
            ' ': []
        }

    def create_styles(self):
        style = ttk.Style()
        style.configure('Black.TFrame', background='black')
        style.configure('White.TLabel', foreground='white', background='black')

    def update_display(self):
        # Clear all displays
        
        for display in self.displays:
            display.clear()
        
        # Get input text
        text = self.text_input.get().upper()[:6]  # Limit to 6 characters
        
        # Update each display
        for i, char in enumerate(text):
            if i < len(self.displays):
                if char in self.char_patterns:
                    for segment in self.char_patterns[char]:
                        self.displays[i].set_segment(segment, True)

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='black')
    app = LEDDisplayApp(root)
    root.mainloop()
