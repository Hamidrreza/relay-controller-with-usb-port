
// arduino code
// this app is just use pin 13 of arduino (atmega328)
// there also 9 more I/O's to control (code likes below)

const int led=13; 
int value=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
  while(Serial.available()){
    Serial.println('conection ok');
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
    value = Serial.read();
  }
  if (value == '1')
    digitalWrite(led, HIGH);
  else if (value == '0')
    digitalWrite(led, LOW);
}
