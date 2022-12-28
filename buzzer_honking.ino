int buzzer = 9;
int speed=30;
  void setup()
{
}
void loop()
{
  if(speed>=25)
  tone(buzzer,450);
  delay(5000);
  exit(0);
}
