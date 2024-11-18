// design.sv
module sixteen_segment_display (
    input logic clk,
    input logic rst,
    input logic [7:0] char_in,  // ASCII input
    input logic load,           // Signal to load new character
    output logic [15:0] segments, // 16 segments output
    output logic [2:0] digit_sel  // Select which digit to display (0-5)
);

    // Internal registers
    logic [7:0] display_chars [5:0];  // Store 6 characters
    logic [2:0] current_digit;        // Current digit being displayed
    logic [19:0] refresh_counter;     // Counter for display multiplexing

    // Segment mapping for characters (A-Z)
    function logic [15:0] char_to_segments(input logic [7:0] char);
        case (char)
            "A": return 16'b1110110111101110; // A
            "B": return 16'b1111111111100000; // B
            "C": return 16'b0111110100000000; // C
            "D": return 16'b1111111100000000; // D
            "E": return 16'b0111110111000000; // E
            "F": return 16'b0110110111000000; // F
            "G": return 16'b0111110101001000; // G
            "H": return 16'b1110110111101100; // H
            "I": return 16'b0111111000000000; // I
            "J": return 16'b1111010000000000; // J
            "K": return 16'b0110110111101100; // K
            "L": return 16'b0111110000000000; // L
            "M": return 16'b1110110110101100; // M
            "N": return 16'b1110110110101100; // N
            "O": return 16'b0111110100000000; // O
            "P": return 16'b1110110111100000; // P
            "Q": return 16'b0111110100001000; // Q
            "R": return 16'b1110110111101000; // R
            "S": return 16'b1111110111000000; // S
            "T": return 16'b0110111000000000; // T
            "U": return 16'b1111110000000000; // U
            "V": return 16'b1110110000000000; // V
            "W": return 16'b1110110101000000; // W
            "X": return 16'b1100110011101100; // X
            "Y": return 16'b1100111000000000; // Y
            "Z": return 16'b0111000011001000; // Z
            default: return 16'b0000000000000000; // Blank for invalid characters
        endcase
    endfunction

    // Character loading logic
    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            for (int i = 0; i < 6; i++)
                display_chars[i] <= 8'h20; // Initialize with spaces
            current_digit <= 3'b0;
            refresh_counter <= 20'b0;
        end
        else begin
            if (load)
                display_chars[digit_sel] <= char_in;
                
            refresh_counter <= refresh_counter + 1;
            if (refresh_counter == 20'd833333) begin // ~60Hz refresh rate with 50MHz clock
                refresh_counter <= 20'b0;
                current_digit <= (current_digit == 3'd5) ? 3'd0 : current_digit + 1;
            end
        end
    end

    // Output logic
    always_comb begin
        digit_sel = current_digit;
        segments = char_to_segments(display_chars[current_digit]);
    end

endmodule