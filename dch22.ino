const int led=9;
int value=0;

void setup() 
   { 
      Serial.begin(9600); 
      pinMode(led, OUTPUT);
      digitalWrite (led, LOW);
      Serial.println("Connection established...");
   }
 
void loop() 
   {
    
           value = Serial.read();
            if (value == '1'){
              digitalWrite (led, HIGH);
              Serial.print("on");
        
            }
     
     
     else if (value == '0')
     {
        digitalWrite (led, LOW);
     }
        }
