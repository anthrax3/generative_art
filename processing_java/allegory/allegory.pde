////////////////////////////////////////////////////////////////////////////////
// code and images by Aaron Penne
// https://github.com/aaronpenne/generative_art
//
// released under the MIT license (https://opensource.org/licenses/MIT)
////////////////////////////////////////////////////////////////////////////////

int max_frames = 10;

float step = 5;
int radius = 5;

float increment = 0.025;

float z_off = 0.0;
float t_off = 0.0;

float z_increment = 0.02;

boolean record = true;
boolean animate = false;
boolean seeded = true;

int rand_seed = 1138;

OpenSimplexNoise noise;


// Fisk Mississipi maps
color[] pal = new color[7];

                 
String timestamp = String.format("%04d%02d%02d_%02d%02d%02d", year(), month(), day(), hour(), minute(), second());

void setup() {
  // Sets size of canvas in pixels (must be first line)
  size(700, 700);
    
  // Sets resolution dynamically (affects resolution of saved image)
  pixelDensity(displayDensity());  // 1 for low, 2 for high
    
  // Sets color space to Hue Saturation Brightness with max values of HSB respectively
  colorMode(HSB, 360, 100, 100, 100);
        
  // Set the number of frames per second to display
  frameRate(50);
    
  // Keeps text centered vertically and horizontally at (x,y) coords
  textAlign(CENTER, CENTER);
    
  rectMode(CORNERS);
    
  // Stops draw() from running in an infinite loop
  if (!animate) {
   noLoop();
  }
        
  // Sets random seed value for both Python and Processing 
  if (seeded) {
    randomSeed(rand_seed);  // Only applies to the random() Processing function
    noiseSeed(rand_seed);   // Only applies to the noise() Processing function
  }
  
  noise = new OpenSimplexNoise();
  
  pal[0] = color(0,0,100);
  pal[1] = color(0,0,25);
  pal[2] = color(39, 16.9, 92.9);    // tan background
  pal[3] = color(48.8, 27, 92.9);    // yellowish
  pal[4] = color(152, 15.38, 76.47); // blueish
  pal[5] = color(2.7, 40.3, 86.7);   // reddish
  pal[6] = color(60, 18.4, 80.8);   // greenish
         
  background(pal[4]);
}

void draw() {
  stroke(pal[1]);
  fill(pal[1]);
  
  float x, y;
  int r = 200;
  for(int a=0; a<=360; a++) {
    x = r * cos(radians(a));
    y = r * sin(radians(a));
    point(x,y);
  }
  
  
  if (record) {
    String output_filepath = "output/%s_####.png";
    println(String.format("Saving %04d to %s", frameCount, String.format(output_filepath, timestamp)));
    saveFrame(String.format(output_filepath, timestamp));
  }
}
