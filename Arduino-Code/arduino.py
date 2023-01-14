const int DEVICE1 = 2;
const int DEVICE2 = 3;
const int DEVICE3 = 4;
const int DEVICE4 = 5;
const int DEVICE5 = 6;

String textMessage;
String DEVICE1State = "LOW";
String DEVICE2State = "LOW";
String DEVICE3State = "LOW";
String DEVICE4State = "LOW";
String DEVICE5State = "LOW";


void setup() 
{
 
  pinMode(DEVICE1, OUTPUT);
  pinMode(DEVICE2, OUTPUT);
  pinMode(DEVICE3, OUTPUT);
  pinMode(DEVICE4, OUTPUT);
  pinMode(DEVICE5, OUTPUT);
 
  digitalWrite(DEVICE1, LOW);
  digitalWrite(DEVICE2, LOW);
  digitalWrite(DEVICE3, LOW);
  digitalWrite(DEVICE4, LOW);
  digitalWrite(DEVICE5, LOW);
  
  
  Serial.begin(19200);  
  delay(20000);

 
  Serial.print("AT+CMGF=1\r");  
  delay(100);

  Serial.print("AT+CNMI=2,2,0,0,0\r");  
  delay(100);
}

void loop() 
{
  if(Serial.available()>0){
    textMessage = Serial.readString(); 
    textMessage.toUpperCase();   
    delay(10);
  } 
  if(textMessage.indexOf("DEVICE1ON")>=0){
    digitalWrite(DEVICE1, HIGH);
    DEVICE1State = "on"; 
    textMessage = "";   
  }
  if(textMessage.indexOf("DEVICE1OFF")>=0){
    digitalWrite(DEVICE1, LOW);
    DEVICE1State = "off"; 
    textMessage = ""; 
  }
   if(textMessage.indexOf("DEVICE2ON")>=0){
    digitalWrite(DEVICE2, HIGH);
    DEVICE2State = "on"; 
    textMessage = "";   
  }
  if(textMessage.indexOf("DEVICE2OFF")>=0){
    digitalWrite(DEVICE2, LOW);
    DEVICE2State = "off"; 
    textMessage = ""; 
  }
   if(textMessage.indexOf("DEVICE3ON")>=0){
    digitalWrite(DEVICE3, HIGH);
    DEVICE3State = "on"; 
    textMessage = "";   
  }
  if(textMessage.indexOf("DEVICE3OFF")>=0){
    digitalWrite(DEVICE3, LOW);
    DEVICE3State = "off"; 
    textMessage = ""; 
  }
   if(textMessage.indexOf("DEVICE4ON")>=0){
    digitalWrite(DEVICE4, HIGH);
    DEVICE4State = "on"; 
    textMessage = "";   
  }
  if(textMessage.indexOf("DEVICE4OFF")>=0){
    digitalWrite(DEVICE4, LOW);
    DEVICE4State = "off"; 
    textMessage = ""; 
  }
  
   if(textMessage.indexOf("DEVICE5ON")>=0){
    digitalWrite(DEVICE5, HIGH);
    DEVICE5State = "on"; 
    textMessage = "";   
  }
  if(textMessage.indexOf("DEVICE5OFF")>=0){
    digitalWrite(DEVICE5, LOW);
    DEVICE5State = "off"; 
    textMessage = ""; 
  }
if(textMessage.indexOf("ALLDEVICEOFF")>=0){
    digitalWrite(DEVICE1, LOW);
    digitalWrite(DEVICE2, LOW);
    digitalWrite(DEVICE3, LOW);
    digitalWrite(DEVICE4, LOW);
    digitalWrite(DEVICE5, LOW);

    DEVICE1State = "off"; 
    DEVICE2State = "off";
    DEVICE3State = "off";
    DEVICE4State = "off";
    DEVICE5State = "off";

    textMessage = ""; 
  }
  if(textMessage.indexOf("ALLDEVICEON")>=0){
    digitalWrite(DEVICE1, HIGH);
    digitalWrite(DEVICE2, HIGH);
    digitalWrite(DEVICE3, HIGH);
    digitalWrite(DEVICE4, HIGH);
    digitalWrite(DEVICE5, HIGH);
 
    DEVICE1State = "on"; 
    DEVICE2State = "on";
    DEVICE3State = "on";
    DEVICE4State = "on";
    DEVICE5State = "on";

    textMessage = ""; 
  }
 
  if(textMessage.indexOf("DEVICE1STATE")>=0){
    String message = "DEVICE1 is " + DEVICE1State;
    sendSMS(message);
    textMessage = "";
  }
  if(textMessage.indexOf("DEVICE2STATE")>=0){
    String message = "DEVICE2 is " + DEVICE2State;
    sendSMS(message);
    textMessage = "";
  }
  if(textMessage.indexOf("DEVICE3STATE")>=0){
    String message = "DEVICE3 is " + DEVICE3State;
    sendSMS(message);
    textMessage = "";
  }
    if(textMessage.indexOf("DEVICE4STATE")>=0){
    String message = "DEVICE4 is " + DEVICE4State;
    sendSMS(message);
    textMessage = "";
  }
    if(textMessage.indexOf("DEVICE5STATE")>=0){
    String message = "DEVICE5 is " + DEVICE5State;
    sendSMS(message);
    textMessage = "";
  }
}  

void sendSMS(String message)  
{
  
  Serial.print("AT+CMGF=1\r"); 
  delay(100);
  Serial.println("AT + CMGS = \"+917736972033\"");   
  delay(100);
  Serial.println(message); 
  delay(100);
  Serial.println((char)26); 
  delay(100);
  Serial.println();
  delay(5000);  
}
