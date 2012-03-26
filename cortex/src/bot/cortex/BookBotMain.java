package bot.cortex;

import android.app.Activity;
import android.os.Bundle;
import android.content.Intent;
import android.view.View;
import java.io.*;
import java.io.File;
import android.content.res.AssetManager;
import android.app.ProgressDialog;
import android.util.Log;

public class BookBotMain extends Activity {
  
  static {
    System.loadLibrary("algo");
  }
  
  private static final String path = "/sdcard/bookbot/";
  
  private native int pathplanner(int[] path_x, int[] path_y);
  
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.main);
    
    CopyAssets();
  }
  
  public void startBookScanner(View v) {
    Intent intent = new Intent("bot.cortex.SCAN");
    intent.setPackage("bot.cortex");
    startActivity(intent);
  }
  
  private void CopyAssets() {
    File fpath = new File(path); 
    if(fpath.isDirectory())
      return;
    else
      fpath.mkdir();
    
    final ProgressDialog loading = ProgressDialog.show(BookBotMain.this, "", "Copying files", true, false);
    
    new Thread() {
      public void run() {
        AssetManager assets = getAssets();
        String[] files = null;
        
        try {
          files = assets.list("");
        } 
        catch (IOException e) {
        }
        for(int i=0; i<files.length; i++) {
          try {
            byte[] buffer = new byte[1024];
            int read;
            InputStream in = assets.open(files[i]);
            OutputStream out = new FileOutputStream(path + files[i]);
            while((read = in.read(buffer)) != -1){
              out.write(buffer, 0, read);
            }
            in.close();
            out.flush();
            out.close();
          } 
          catch(Exception e) {
          }       
        }
        loading.dismiss();
      }
    }.start();
  }
  public void exitApp(View v) {
    int[] pathX = new int[256];
    int[] pathY = new int[256];
    
    int points = pathplanner(pathX, pathY);
    
    //finish();
    BotController bot = new BotController(this);
    bot.navigate(points, pathX, pathY);
  }
}
