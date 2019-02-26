
//,                            |КС               |КС
String a8A = ":8A4447646517232C000733330A0A006700000703D1\r\n";
String a85 = ":854447646517232C000033330A0A006700000703E4\r\n";
String a9F = ":9F4447646517232C000733330A0A006700000703CD\r\n";
String a93 = ":934447646517232C000733330A0A006700000703DE\r\n";
String a93b = ":934449006517232C080733330A0A006700000703030C0C000001000B2F09C1\r\n";
String a9349 = ":934449006517232C000733330A0A006700000703030C0C000001000B2F09C9\r\n";

String a8A51 = ":8A44510515000000000200C02B08000000000700000000000000000006000000000000000000000000004E00000000000000B7\r\n";
String a8551 = ":8A44510515000000000200C02B08000000000700000000000000000006000000000000000000000000004E00000000000000B7\r\n";
String a9F51 = ":9F44510515000000000200C02B08000000000700000000000000000006000000000000000000000000004E00000000000000B1\r\n";

int timer = 0;
int lastTimer = 0;

char b[20];
void setup() {
  Serial.begin(115200);

}

void loop() {
  timer = millis();
  if (Serial.available() > 0) {
    Serial.readBytes(b, 17);
    while (Serial.available() > 0) { //очистка остальных поступивших данных
      Serial.read();                 // свыше 17 байт
    }
    if (b[5] == '4' and b[6] == '7' and b[1] == '8' and b[2] == 'A') {
      Serial.print(a8A);
    }
    if (b[5] == '4' and b[6] == '7' and b[1] == '8' and b[2] == '5') {
      Serial.print(a85);
    }
    if (b[5] == '4' and b[6] == '7' and b[1] == '9' and b[2] == '3') {
      Serial.print(a93);
    }
    if (b[5] == '4' and b[6] == '7' and b[1] == '9' and b[2] == 'F') {
      Serial.print(a9F);
    }
    if (b[5] == '5' and b[6] == '1' and b[1] == '8' and b[2] == 'A') {
      Serial.print(a8A51);
    }
    /*if (b[5] == '5' and b[6] == '1' and b[1] == '8' and b[2] == '5') {
        Serial.print(a8551);
      }*/
    if (b[5] == '4' and b[6] == '9' and b[1] == '9' and b[2] == '3') {
      if (timer - lastTimer <= 5000) {
        Serial.print(a9349);
      }else{
        Serial.print(a93b);
      }
    }
    if (b[5] == '5' and b[6] == '1' and b[1] == '9' and b[2] == 'F') {
      Serial.print(a9F51);
    }
  }
  delay(100);
  if (timer - lastTimer >= 10000) {
    lastTimer = timer;
  }
}
