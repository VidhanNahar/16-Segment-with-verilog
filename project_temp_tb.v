module alphabet_to_16segment (
    input wire [7:0] character,  // ASCII character input
    output reg [15:0] segment,   // 16-bit output for the segment code
    output reg found             // Indicator for whether the character was found or not
);

    reg [7:0] char_array [0:25];   // Array to store ASCII values of A-Z
    reg [15:0] segment_array [0:25]; // Array to store 16-segment codes for A-Z
    integer i;

    initial begin
        // Initialize the character array with ASCII values of A-Z
        char_array[0] = 8'h41; // 'A'
        char_array[1] = 8'h42; // 'B'
        char_array[2] = 8'h43; // 'C'
        char_array[3] = 8'h44; // 'D'
        char_array[4] = 8'h45; // 'E'
        char_array[5] = 8'h46; // 'F'
        char_array[6] = 8'h47; // 'G'
        char_array[7] = 8'h48; // 'H'
        char_array[8] = 8'h49; // 'I'
        char_array[9] = 8'h4A; // 'J'
        char_array[10] = 8'h4B; // 'K'
        char_array[11] = 8'h4C; // 'L'
        char_array[12] = 8'h4D; // 'M'
        char_array[13] = 8'h4E; // 'N'
        char_array[14] = 8'h4F; // 'O'
        char_array[15] = 8'h50; // 'P'
        char_array[16] = 8'h51; // 'Q'
        char_array[17] = 8'h52; // 'R'
        char_array[18] = 8'h53; // 'S'
        char_array[19] = 8'h54; // 'T'
        char_array[20] = 8'h55; // 'U'
        char_array[21] = 8'h56; // 'V'
        char_array[22] = 8'h57; // 'W'
        char_array[23] = 8'h58; // 'X'
        char_array[24] = 8'h59; // 'Y'
        char_array[25] = 8'h5A; // 'Z'

        // Initialize the segment_array with 16-segment codes for A-Z
        segment_array[0] = 16'b1111001111000000;  // A
        segment_array[1] = 16'b1111110001010010;  // B
        segment_array[2] = 16'b1100111100000000;  // C
        segment_array[3] = 16'b1111110000010010;  // D
        segment_array[4] = 16'b1100111111000000;  // E
        segment_array[5] = 16'b1100001111000000;  // F
        segment_array[6] = 16'b1101111101000000;  // G
        segment_array[7] = 16'b0011001111000000;  // H
        segment_array[8] = 16'b1100110000010010;  // I
        segment_array[9] = 16'b1100101000010010;  // J
        segment_array[10] = 16'b0000001110001001; // K
        segment_array[11] = 16'b0000111100000000; // L
        segment_array[12] = 16'b0011001100101000; // M
        segment_array[13] = 16'b0011001100100001; // N
        segment_array[14] = 16'b1111111100000000; // O
        segment_array[15] = 16'b1110001111000000; // P
        segment_array[16] = 16'b1111111100000001; // Q
        segment_array[17] = 16'b1110001111000001; // R
        segment_array[18] = 16'b1101110111000000; // S
        segment_array[19] = 16'b1100000000010010; // T
        segment_array[20] = 16'b0011111100000000; // U
        segment_array[21] = 16'b0000001100001100; // V
        segment_array[22] = 16'b0011001100000101; // W
        segment_array[23] = 16'b0000000000101101; // X
        segment_array[24] = 16'b0000000000101010; // Y
        segment_array[25] = 16'b1100110001000100; // Z
    end

    always @(*) begin
        found = 0;
        segment = 16'b0000000000000000; // Default value for segment
        for (i = 0; i < 26; i = i + 1) begin
            if (character == char_array[i]) begin
                segment = segment_array[i];
                found = 1;
            end
        end
    end

endmodule

module test_alphabet_to_16segment;

    // Inputs
    reg [7:0] character;

    // Outputs
    wire [15:0] segment;
    wire found;

    // Internal variables
    integer input_file, output_file, i;
    reg [7:0] r [5:0];  // Array to store six characters

    // Instantiate the Unit Under Test (UUT)
    alphabet_to_16segment uut (
        .character(character), 
        .segment(segment),
        .found(found)
    );

    initial begin
        // Open the input file and read the characters
        $display("Reading characters from file...");
        input_file = $fopen("character_input.txt", "r");
        
        if (input_file == 0) begin
            $display("Failed to open input file.");
            $stop;
        end
        
        // Read the first 6 characters from the file
        for (i = 0; i < 6; i = i + 1) begin
            r[i] = $fgetc(input_file);
            if (r[i] == 8'hFF) begin  // Ensure it's not the EOF character
                $display("Unexpected end of file.");
                $stop;
            end
        end
        
        $fclose(input_file);

        // Open the file in write mode to overwrite with 16-bit binary codes
        output_file = $fopen("character_input.txt", "w");
        
        if (output_file == 0) begin
            $display("Failed to open output file.");
            $stop;
        end

        // Process and write the 16-bit binary code for each character to the file
        for (i = 0; i < 6; i = i + 1) begin
            character = r[i];
            #1;  // Allow time for UUT to process the character
            if (found) begin
                $fwrite(output_file, "%b\n", segment);
                $display("Character: %c, Segment: %b, Found: %b", character, segment, found);
            end else begin
                $fwrite(output_file, "Character not found\n");
                $display("Character: %c, Segment: N/A, Found: %b", character, found);
            end
        end

        $fclose(output_file);
        $finish;  // End the simulation cleanly
    end

endmodule
