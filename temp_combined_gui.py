import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

class SixteenSegmentDisplay:
    def __init__(self, master, position):
        self.canvas = tk.Canvas(master, width=120, height=180, bg='black')
        self.canvas.grid(row=0, column=position, padx=10, pady=10)
        self.off_color = '#1a1a1a'
        self.on_color = '#ff0000'
        self.segments = {}
        self.segment_types = {}
        self.create_segments()
        self.clear()

    def create_segments(self):
        segments = {
            'a1': [(25, 15, 55, 22)],
            'a2': [(65, 15, 95, 22)],
            'b': [(95, 22, 102, 87)],
            'c': [(95, 93, 102, 158)],
            'd1': [(25, 158, 55, 165)],
            'd2': [(65, 158, 95, 165)],
            'e': [(18, 93, 25, 158)],
            'f': [(18, 22, 25, 87)],
            'g1': [(25, 87, 55, 93)],
            'g2': [(65, 87, 95, 93)],
            'h': [(25, 22, 58, 87)],
            'i': [(58, 22, 62, 87)],
            'j': [(62, 87, 95, 22)],
            'k': [(25, 158, 58, 93)],
            'l': [(58, 93, 62, 158)],
            'm': [(62, 93, 95, 158)]
        }

        for segment, coords_list in segments.items():
            self.segments[segment] = []
            for coords in coords_list:
                if segment in ['h', 'j', 'k', 'm']:
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

    def display_binary(self, binary_pattern):
        segments = ['a1', 'a2', 'b', 'c', 'd1', 'd2', 'e', 'f',
                   'g1', 'g2', 'h', 'i', 'j', 'k', 'l', 'm']
        bits = [bit == '1' for bit in binary_pattern]
        for segment, state in zip(segments, bits):
            self.set_segment(segment, state)

class LEDDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("16-Segment LED Display")
        self.root.configure(bg='#000000')

        # Create main frame
        self.main_frame = ttk.Frame(root, style='Black.TFrame')
        self.main_frame.pack(pady=20, padx=20)

        # Create title
        title_font = tkfont.Font(family="Arial", size=16, weight="bold")
        title_label = tk.Label(
            self.main_frame,
            text="Multi 16-Segment LED Display",
            font=title_font,
            fg='#00ff00',
            bg='#000000'
        )
        title_label.pack(pady=(0, 20))

        # Create display frame
        self.display_frame = ttk.Frame(self.main_frame, style='Black.TFrame')
        self.display_frame.pack(pady=10)

        # Create six displays
        self.displays = []
        for i in range(6):
            display = SixteenSegmentDisplay(self.display_frame, i)
            self.displays.append(display)

        # Create label frame for character display
        self.label_frame = ttk.Frame(self.main_frame, style='Black.TFrame')
        self.label_frame.pack(pady=5)
        
        # Create labels for each display
        self.char_labels = []
        for i in range(6):
            label = tk.Label(
                self.label_frame,
                text="",
                font=tkfont.Font(family="Arial", size=12),
                fg='#ffffff',
                bg='#000000',
                width=3
            )
            label.grid(row=0, column=i, padx=10)
            self.char_labels.append(label)

        # Add instructions
        instruction_font = tkfont.Font(family="Arial", size=10)
        instructions = tk.Label(
            self.main_frame,
            text="Displaying patterns from 'character_input.txt'",
            font=instruction_font,
            fg='#888888',
            bg='#000000'
        )
        instructions.pack(pady=(10, 0))

        # Configure style
        style = ttk.Style()
        style.configure('Black.TFrame', background='black')

        # Automatically read patterns when starting
        self.read_binary_file()

    def binary_to_char(self, binary_pattern):
        # Define character patterns (mapping from binary to character)
        char_patterns = {
            '1111111100111111': 'A',
            '1111111111111111': 'B',
            '1111000000111111': 'C',
            '1111110011111111': 'D',
            '1111001111111111': 'E',
            '1111001111110000': 'F',
            '1111000011111111': 'G',
            '0011111111110011': 'H',
            '1111110000001111': 'I',
            '0000110011111111': 'J',
            '0011001111110101': 'K',
            '0011000000111111': 'L',
            '0011111111110111': 'M',
            '0011111111111101': 'N',
            '1111110011111111': 'O',
            '1111111111110000': 'P',
            '1111110011111101': 'Q',
            '1111111111110101': 'R',
            '1111001111111111': 'S',
            '1111110000000000': 'T',
            '0011110011111111': 'U',
            '0011000011110101': 'V',
            '0011110011111101': 'W',
            '0000001111110101': 'X',
            '0000110000001111': 'Y',
            '1111000011110101': 'Z',
            '0000000000000000': ' '
        }
        return char_patterns.get(binary_pattern, '')  # Return empty string instead of '?'

    def read_binary_file(self):
        try:
            with open('character_input.txt', 'r') as file:
                patterns = file.readlines()
                
                # Clear all displays first
                for display in self.displays:
                    display.clear()
                
                # Clear all labels
                for label in self.char_labels:
                    label.config(text="")
                
                # Process up to 6 patterns
                for i, pattern in enumerate(patterns[:6]):
                    pattern = pattern.strip()
                    if len(pattern) == 16 and all(bit in '01' for bit in pattern):
                        self.displays[i].display_binary(pattern)
                        # Update the character label only if we have a valid character
                        char = self.binary_to_char(pattern)
                        if char:  # Only show label if we have a valid character
                            self.char_labels[i].config(text=char)
                    else:
                        print(f"Invalid pattern on line {i+1}: Must be exactly 16 bits (0s and 1s)")
                        
        except FileNotFoundError:
            print("character_input.txt not found")
        except Exception as e:
            print(f"Error reading file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='black')
    app = LEDDisplayApp(root)
    root.mainloop()