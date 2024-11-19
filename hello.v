module SixLetter16SegmentDisplay(
    input [7:0] char1, // ASCII value of first character
    input [7:0] char2, // ASCII value of second character
    input [7:0] char3, // ASCII value of third character
    input [7:0] char4, // ASCII value of fourth character
    input [7:0] char5, // ASCII value of fifth character
    input [7:0] char6, // ASCII value of sixth character
    output reg [15:0] seg1, // 16-segment output for char1
    output reg [15:0] seg2, // 16-segment output for char2
    output reg [15:0] seg3, // 16-segment output for char3
    output reg [15:0] seg4, // 16-segment output for char4
    output reg [15:0] seg5, // 16-segment output for char5
    output reg [15:0] seg6  // 16-segment output for char6
);

    // Function to map ASCII to 16-segment encoding
    function [15:0] charTo16Segment;
        input [7:0] ascii;
        begin
            case (ascii)
                8'h41: charTo16Segment = 16'b0000_1111_1111_1111; // 'A'
                8'h42: charTo16Segment = 16'b0000_1111_0111_1011; // 'B'
                8'h43: charTo16Segment = 16'b0000_1010_0011_1111; // 'C'
                8'h44: charTo16Segment = 16'b0000_1111_0111_0111; // 'D'
                8'h45: charTo16Segment = 16'b0000_1010_0111_1111; // 'E'
                8'h46: charTo16Segment = 16'b0000_1010_0111_1000; // 'F'
                // Add mappings for other letters and numbers
                default: charTo16Segment = 16'b0000_0000_0000_0000; // Blank or unsupported character
            endcase
        end
    endfunction

    // Assign segment encodings
    always @(*) begin
        seg1 = charTo16Segment(char1);
        seg2 = charTo16Segment(char2);
        seg3 = charTo16Segment(char3);
        seg4 = charTo16Segment(char4);
        seg5 = charTo16Segment(char5);
        seg6 = charTo16Segment(char6);
    end

endmodule
