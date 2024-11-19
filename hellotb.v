module Testbench;
    reg [7:0] char1, char2, char3, char4, char5, char6;
    wire [15:0] seg1, seg2, seg3, seg4, seg5, seg6;

    // Instantiate the display module
    SixLetter16SegmentDisplay uut (
        .char1(char1),
        .char2(char2),
        .char3(char3),
        .char4(char4),
        .char5(char5),
        .char6(char6),
        .seg1(seg1),
        .seg2(seg2),
        .seg3(seg3),
        .seg4(seg4),
        .seg5(seg5),
        .seg6(seg6)
    );

    initial begin
        // Test case: Display "ABCDEF"
        char1 = 8'h41; // 'A'
        char2 = 8'h42; // 'B'
        char3 = 8'h43; // 'C'
        char4 = 8'h44; // 'D'
        char5 = 8'h45; // 'E'
        char6 = 8'h46; // 'F'

        #10; // Wait for signals to propagate

        // Display results
        $display("Segments for 'A': %b", seg1);
        $display("Segments for 'B': %b", seg2);
        $display("Segments for 'C': %b", seg3);
        $display("Segments for 'D': %b", seg4);
        $display("Segments for 'E': %b", seg5);
        $display("Segments for 'F': %b", seg6);

        $finish;
    end
endmodule
