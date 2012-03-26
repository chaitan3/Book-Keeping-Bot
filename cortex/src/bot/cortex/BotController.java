package bot.cortex;

import android.util.Log;
import android.content.Context;

public class BotController implements Runnable {
  
  private ADKCommunication adk;
  private byte[] buffer = new byte[128];
  private int n_points;
  private int[] pathX, pathY;
  
  public BotController(Context context) {
    adk = new ADKCommunication(context);
    adk.connect();
  }
  
  public void navigate(int points, int[] x, int[] y) {
    n_points = points;
    pathX = x;
    pathY = y;
    Thread thread = new Thread(null, this, "AndroidAdkUsb");
    thread.start();
  }
  
	@Override
	public void run() {
    String resp, command;
    int i;
    
    for(i = 0; i < n_points; i++) {
      command = String.format("GO %4d %4d", pathX[i], pathY[i]);
      sendCommand(command);
      resp = recvResponse();
    }
	}
  
  private void sendCommand(String command) {
    Log.d("ADK", "Sending " + command + " Length " + command.length());
    try {
      adk.write(command.getBytes(), command.length());
    }
    catch(Exception e) {
    }
  }
  
  private String recvResponse() {
    int bytes;
    
    bytes = adk.read(buffer);
    String recvData = new String(buffer, 0, bytes);
    Log.d("ADK", "Received " + recvData + " Length " + bytes);
    
    return recvData;
  }
}
    
