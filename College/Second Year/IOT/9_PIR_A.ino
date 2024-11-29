int pirPin = 3;
int ledPin = 2;
void setup() {
  Serial.begin(9600);
  pinMode(pirPin, INPUT);
  pintMode(ledPin, OUTPUT);
}

void loop() {
  int motion = digitalRead(pirPin);
  if(motion == HIGH){
    Serial.println("Motion Detected");
    digitalWrite(ledPin, HIGH);
  } else {
    Serial.println("Motion Not Detected");
    digitalWrite(ledPin, LOW);
  }
  delay(1000)
}
