
// testbench.sv
module sixteen_segment_display_tb;
    logic clk;
    logic rst;
    logic [7:0] char_in;
    logic load;
    logic [15:0] segments;
    logic [2:0] digit_sel;

    // Instantiate the design
    sixteen_segment_display dut (
        .clk(clk),
        .rst(rst),
        .char_in(char_in),
        .load(load),
        .segments(segments),
        .digit_sel(digit_sel)
    );

    // Clock generation
    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    // Test stimulus
    initial begin
        // Initialize signals
        rst = 1;
        char_in = 8'h20;
        load = 0;
        #20;
        
        // Release reset
        rst = 0;
        #20;

        // Test word "HELLO!"
        // Load 'H'
        char_in = "H";
        digit_sel = 0;
        load = 1;
        #10;
        load = 0;
        #10;

        // Load 'E'
        char_in = "E";
        digit_sel = 1;
        load = 1;
        #10;
        load = 0;
        #10;

        // Load 'L'
        char_in = "L";
        digit_sel = 2;
        load = 1;
        #10;
        load = 0;
        #10;

        // Load 'L'
        char_in = "L";
        digit_sel = 3;
        load = 1;
        #10;
        load = 0;
        #10;

        // Load 'O'
        char_in = "O";
        digit_sel = 4;
        load = 1;
        #10;
        load = 0;
        #10;

        // Load '!'
        char_in = "!";
        digit_sel = 5;
        load = 1;
        #10;
        load = 0;

        // Let it run for a while to observe the display
        #1000;
        
        $finish;
    end

    // Monitor the outputs
    initial begin
        $monitor("Time=%0t digit_sel=%0d segments=%16b", $time, digit_sel, segments);
    end

endmodule