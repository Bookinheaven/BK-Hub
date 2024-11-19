
const int sensorPin = A0;
void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.pint("Analog Output: ");
  Serial.print(readSensor());
  delay(1000);
}
int readSesor() {
  int sensorValue = digitalRead(sensorPin);
  return sensorValue;
}
